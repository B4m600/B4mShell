import asyncio
import json
import websockets
import requests
import time
import hashlib
import hmac
import random
from hashlib import sha256
import proto
import socket
import threading
from pynput import keyboard
import urllib3

# 禁用SSL警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class GodotTCPClient:
    def __init__(self, host='localhost', port=1145):
        self.host = host
        self.port = port
        self.socket = None
        self.connected = False
        self.running = True
        self.heartbeat_thread = None
        self.data_counter = 0
        self.reconnect_attempts = 0
        self.max_reconnect_attempts = 10000
        
    def connect(self):
        """连接到Godot服务器"""
        try:
            if self.socket:
                self.socket.close()
                
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.settimeout(10)  # 增加超时时间
            
            print(f"尝试连接到 {self.host}:{self.port}")
            self.socket.connect((self.host, self.port))
            self.connected = True
            self.reconnect_attempts = 0
            print("✅ 成功连接到Godot服务器")
            
            self.start_heartbeat()
            return True
            
        except Exception as e:
            print(f"❌ 连接失败: {e}")
            self.connected = False
            return False
    
    def send_data(self, data_dict):
        """发送数据到Godot"""
        if not self.connected:
            print("未连接到Godot服务器，尝试重连...")
            if self.reconnect_attempts < self.max_reconnect_attempts:
                self.reconnect_attempts += 1
                if self.connect():
                    return self.send_data(data_dict)
                else:
                    print(f"重连失败 ({self.reconnect_attempts}/{self.max_reconnect_attempts})")
                    return False
            else:
                print("达到最大重连次数，停止尝试")
                return False
        
        try:
            json_data = json.dumps(data_dict, ensure_ascii=False)
            message = (json_data + '\n').encode('utf-8')
            self.socket.sendall(message)
            
            if data_dict.get("type") != "heartbeat":
                print(f"✅ 成功发送数据 #{self.data_counter} 到Godot")
                self.data_counter += 1
                
            return True
        except Exception as e:
            print(f"❌ 发送数据失败: {e}")
            self.connected = False
            # 尝试立即重连一次
            if self.reconnect_attempts < self.max_reconnect_attempts:
                print("尝试重新连接...")
                return self.send_data(data_dict)
            return False
    
    def start_heartbeat(self):
        """启动心跳线程"""
        def heartbeat_loop():
            heartbeat_counter = 0
            while self.running:
                if not self.connected:
                    time.sleep(1)
                    continue
                    
                try:
                    heartbeat_data = {
                        "type": "heartbeat", 
                        "timestamp": time.time(),
                        "counter": heartbeat_counter
                    }
                    self.send_data(heartbeat_data)
                    heartbeat_counter += 1
                    time.sleep(1)
                except Exception as e:
                    print(f"心跳发送失败: {e}")
                    self.connected = False
                    time.sleep(1)
        
        if self.heartbeat_thread and self.heartbeat_thread.is_alive():
            return
            
        self.heartbeat_thread = threading.Thread(target=heartbeat_loop)
        self.heartbeat_thread.daemon = True
        self.heartbeat_thread.start()
    
    def disconnect(self):
        """优雅断开连接"""
        print("正在断开Godot连接...")
        self.running = False
        self.connected = False
        
        if self.socket:
            try:
                disconnect_msg = {
                    "type": "disconnect", 
                    "timestamp": time.time(),
                    "total_data_sent": self.data_counter
                }
                self.send_data(disconnect_msg)
                time.sleep(0.1)
            except Exception as e:
                print(f"发送断开消息失败: {e}")
            
            try:
                self.socket.close()
                print("✅ Godot Socket已关闭")
            except Exception as e:
                print(f"关闭Godot socket失败: {e}")
            
            self.socket = None
        
        print("✅ 已断开与Godot服务器的连接")

class BiliClient:
    def __init__(self, idCode, appId, key, secret, host, godot_client):
        self.idCode = idCode
        self.appId = appId
        self.key = key
        self.secret = secret
        self.host = host
        self.gameId = ''
        self.godot_client = godot_client
        self.message_counter = 0
        self.running = True
        self.loop = None
        self.websocket = None

    def run(self):
        """在新线程中运行异步循环"""
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        
        try:
            self.loop.run_until_complete(self._async_run())
        except Exception as e:
            print(f"BiliClient运行错误: {e}")
        finally:
            if self.loop:
                self.loop.close()

    async def _async_run(self):
        """异步主函数"""
        try:
            self.websocket = await self.connect()
            if not self.websocket:
                print("BiliClient连接失败")
                return
                
            tasks = [
                asyncio.create_task(self.recvLoop(self.websocket)),
                asyncio.create_task(self.heartBeat(self.websocket)),
                asyncio.create_task(self.appheartBeat()),
            ]
            
            await asyncio.gather(*tasks, return_exceptions=True)
        except Exception as e:
            print(f"BiliClient异步运行错误: {e}")
        finally:
            if self.websocket:
                await self.websocket.close()

    def stop(self):
        """停止BiliClient"""
        self.running = False
        if self.loop and self.loop.is_running():
            self.loop.call_soon_threadsafe(self.loop.stop)

    def sign(self, params):
        """HTTP签名"""
        key = self.key
        secret = self.secret
        md5 = hashlib.md5()
        md5.update(params.encode())
        ts = time.time()
        nonce = random.randint(1, 100000) + time.time()
        md5data = md5.hexdigest()
        headerMap = {
            "x-bili-timestamp": str(int(ts)),
            "x-bili-signature-method": "HMAC-SHA256",
            "x-bili-signature-nonce": str(nonce),
            "x-bili-accesskeyid": key,
            "x-bili-signature-version": "1.0",
            "x-bili-content-md5": md5data,
        }

        headerList = sorted(headerMap)
        headerStr = ''

        for key in headerList:
            headerStr = headerStr + key + ":" + str(headerMap[key]) + "\n"
        headerStr = headerStr.rstrip("\n")

        appsecret = secret.encode()
        data = headerStr.encode()
        signature = hmac.new(appsecret, data, digestmod=sha256).hexdigest()
        headerMap["Authorization"] = signature
        headerMap["Content-Type"] = "application/json"
        headerMap["Accept"] = "application/json"
        return headerMap

    def getWebsocketInfo(self):
        """获取WebSocket连接信息"""
        try:
            postUrl = f"{self.host}/v2/app/start"
            params = json.dumps({"code": self.idCode, "app_id": self.appId})
            headerMap = self.sign(params)
            
            print(f"请求应用启动: {params}")
            response = requests.post(postUrl, headers=headerMap, data=params, verify=False, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            print("应用启动响应:", json.dumps(data, indent=2, ensure_ascii=False))
            
            if data['code'] != 0:
                print(f"应用启动失败: {data['message']}")
                return None, None
                
            self.gameId = str(data['data']['game_info']['game_id'])
            wss_link = data['data']['websocket_info']['wss_link'][0]
            auth_body = data['data']['websocket_info']['auth_body']
            
            print(f"游戏ID: {self.gameId}")
            print(f"WebSocket地址: {wss_link}")
            
            return wss_link, auth_body
        except Exception as e:
            print(f"获取WebSocket信息失败: {e}")
            return None, None

    async def appheartBeat(self):
        """应用心跳"""
        while self.running:
            await asyncio.sleep(20)
            if not self.running:
                break
                
            try:
                postUrl = f"{self.host}/v2/app/heartbeat"
                params = json.dumps({"game_id": self.gameId})
                headerMap = self.sign(params)
                response = requests.post(postUrl, headers=headerMap, data=params, verify=False, timeout=5)
                data = response.json()
                
                if data['code'] == 0:
                    print("✅ 应用心跳发送成功")
                else:
                    print(f"❌ 应用心跳失败: {data['message']}")
            except Exception as e:
                print(f"❌ 应用心跳错误: {e}")

    async def auth(self, websocket, authBody):
        """WebSocket鉴权"""
        try:
            req = proto.Proto()
            req.body = authBody
            req.op = 7
            await websocket.send(req.pack())
            
            buf = await asyncio.wait_for(websocket.recv(), timeout=10)
            resp = proto.Proto()
            resp.unpack(buf)
            respBody = json.loads(resp.body)
            
            if respBody["code"] != 0:
                print(f"❌ 鉴权失败: {respBody}")
                return False
            else:
                print("✅ 鉴权成功")
                return True
        except Exception as e:
            print(f"❌ 鉴权错误: {e}")
            return False

    async def heartBeat(self, websocket):
        """WebSocket心跳"""
        while self.running:
            await asyncio.sleep(20)
            if not self.running or not websocket.open:
                break
                
            try:
                req = proto.Proto()
                req.op = 2
                await websocket.send(req.pack())
                print("✅ WebSocket心跳发送成功")
            except Exception as e:
                print(f"❌ WebSocket心跳错误: {e}")
                break

    def process_and_forward_message(self, resp):
        """处理并转发B站消息到Godot"""
        try:
            print(f"📨 收到B站消息: op={resp.op}, 长度={len(resp.body)}")
            
            # 尝试解析消息体
            try:
                message_data = json.loads(resp.body)
                print(f"📊 消息内容: {json.dumps(message_data, indent=2, ensure_ascii=False)}")
            except:
                message_data = {"raw_data": resp.body[:100] + "..." if len(resp.body) > 100 else resp.body}
                print("⚠️ 消息体不是JSON格式")
            
            # 构建转发给Godot的数据格式
            godot_message = {
                "type": "bili_message",
                "message_id": self.message_counter,
                "timestamp": time.time(),
                "op_code": resp.op,
                "data": message_data
            }
            
            # 发送到Godot
            if self.godot_client.send_data(godot_message):
                self.message_counter += 1
                print(f"✅ 已转发消息 #{self.message_counter} 到Godot")
            else:
                print("❌ 转发到Godot失败")
                
        except Exception as e:
            print(f"❌ 处理消息失败: {e}")

    async def recvLoop(self, websocket):
        """接收消息循环"""
        print("开始接收B站消息...")
        while self.running and websocket.open:
            try:
                recvBuf = await asyncio.wait_for(websocket.recv(), timeout=30.0)
                resp = proto.Proto()
                resp.unpack(recvBuf)
                
                # 处理不同类型的消息
                if resp.op == 5:  # 业务消息
                    self.process_and_forward_message(resp)
                elif resp.op == 3:  # 心跳回复
                    print("💓 收到心跳回复")
                elif resp.op == 8:  # 鉴权回复
                    print("🔑 收到鉴权回复")
                else:
                    print(f"❓ 收到未知消息: op={resp.op}")
                    
            except asyncio.TimeoutError:
                # 检查连接是否仍然活跃
                if websocket.open:
                    continue
                else:
                    print("WebSocket连接已关闭")
                    break
            except Exception as e:
                print(f"❌ 接收消息错误: {e}")
                if not self.running:
                    break
                await asyncio.sleep(1)

    async def connect(self):
        """建立WebSocket连接"""
        addr, authBody = self.getWebsocketInfo()
        if not addr or not authBody:
            print("❌ 获取连接信息失败")
            return None
            
        print(f"连接到: {addr}")
        try:
            websocket = await websockets.connect(addr, ping_interval=20, ping_timeout=10)
            if await self.auth(websocket, authBody):
                print("✅ BiliClient连接成功")
                return websocket
            else:
                await websocket.close()
                return None
        except Exception as e:
            print(f"❌ 连接失败: {e}")
            return None

    def __enter__(self):
        print("初始化BiliClient")
        return self

    def __exit__(self, type, value, trace):
        self.stop()
        if self.gameId:
            try:
                postUrl = f"{self.host}/v2/app/end"
                params = json.dumps({"game_id": self.gameId, "app_id": self.appId})
                headerMap = self.sign(params)
                response = requests.post(postUrl, headers=headerMap, data=params, verify=False, timeout=5)
                print("✅ 应用结束请求已发送")
            except Exception as e:
                print(f"❌ 结束应用失败: {e}")

def main():
    """主函数"""
    print("=== BiliClient to Godot 转发程序 ===")
    
    # 创建Godot客户端
    godot_client = GodotTCPClient(host='localhost', port=1145)
    
    # 尝试连接到Godot
    if not godot_client.connect():
        print("❌ Godot连接失败，程序退出")
        return
    
    # 创建BiliClient
    bili_client = BiliClient(
        idCode="CUI3Z0NBFL6O8",  # 替换为你的主播身份码
        appId=1697831269511,     # 替换为你的应用id
        key="0KJveogr5MBMbvC1Rt1AzSHM",      # 替换为你的access_key
        secret="j7ARTMfm8hmKYAZQfE3FklyXi77WJk",  # 替换为你的access_key_secret
        host="https://live-open.biliapi.com",
        godot_client=godot_client
    )
    
    # 启动BiliClient线程
    bili_thread = threading.Thread(target=bili_client.run, name="BiliClient")
    bili_thread.daemon = True
    bili_thread.start()
    
    print("程序启动完成，等待数据...")
    print("按ESC键退出程序")
    
    try:
        # 简单的键盘监听（替代pynput，避免依赖问题）
        import msvcrt
        while True:
            if msvcrt.kbhit() and msvcrt.getch() == b'\x1b':  # ESC键
                print("\nESC键按下，准备退出...")
                break
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n接收到Ctrl+C信号")
    except ImportError:
        # 如果不是Windows系统，使用简单的等待
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n接收到中断信号")
    except Exception as e:
        print(f"程序运行错误: {e}")
    finally:
        # 清理资源
        print("正在关闭程序...")
        bili_client.stop()
        godot_client.disconnect()
        
        # 等待线程结束
        bili_thread.join(timeout=3)
        print("程序退出")

if __name__ == '__main__':
    main()