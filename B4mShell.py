import os, sys

if not os.path.exists("config"):
    os.mkdir("config")
if not os.path.exists("target"):
    os.mkdir("target")
sysMode = "Linux"
if os.path.exists("config/sysMode"):
    with open("config/sysMode", "r")as f:
        if f.read() == "Windows":
            sysMode = "Windows"
        elif f.read() == "Linux":
            sysMode = "Linux"
        else:
            print("Error(读取sysMode失败);")
else:
    Choice = input("# >是否使用Windows系统模式？(Y/n):")
    if Choice == "Y" or Choice == "y":
        sysMode = "Windows"
        with open("config/sysMode", "w")as f:
            f.write(sysMode)
    elif Choice == "N" or Choice == "n":
        sysMode = "Linux"
        with open("config/sysMode", "w")as f:
            f.write(sysMode)
    elif Choice == "e" or Choice == "E":
        sys.exit(0)
    else:
        print("# >已默认使用Linux系统模式,下次启用再次询问。")
if sysMode == "Windows":
    usePsutil = True
else:
    usePsutil = False

import datetime, time, re, hashlib, shutil
import random, base64, urllib, requests, datetime, json, math
if usePsutil:
    import psutil
username = "南竹"
if os.path.exists("config/username"):
    with open("config/username", "r", encoding="u8")as f:
        username = f.read()
else:
    username = input("# >输入用户名(之后可使用username指令修改):")
    with open("config/username", "w", encoding="u8")as f:
        f.write(username)
path = os.path.realpath('.')
Path = path
Color = "\033[32m"
BgColor = "\033[40m"
SystemCommands = ["python", "node", "pip", "npm", "pnpm", "docker", "ping", "subl", "md", "cmd",
                  "calc", "osk", "mmc", "mstsc", "dvdplay", "system.cpl", "regedit", "resmon",
                  "cleanmgr", "snippingtool", "magnify", "git", "nano", "chmod", "curl"]
MediaExt = ["jpg", "jpeg", "webp", "png", "gif", "JPEG", "mp3", "wav", "mp4", "m4a"]
var = ""
DownloadConfig = {
    "pip": "https://pypi.tuna.tsinghua.edu.cn/simple",
    "git": "https://ghproxy.com"
}

if os.path.exists("config/var"):
    with open("config/var", "r", encoding="u8")as f:
        var = f.read()
def MyShell(command):
    global Path, path, Color, var, username, MediaExt 
    if command.startswith("print:"):
        Vars = globals()
        command_msg = command[6:]
        if command_msg in Vars:
            print(f"{command_msg}:{eval(command_msg)}")
        else:
            print(f"{command_msg}:None")
        return True
    elif command.startswith("exec:"):
        command_msg = command[5:]
        try:
            exec(command_msg)
        except Exception as E:
            print(f"Error({E})")
    elif command.startswith("md5:"):
        command_msg = command[4:]
        try:
            md = hashlib.md5()
            md.update(command_msg.encode('utf-8'))
            print(md.hexdigest())
        except:
            print(f"Error({command_msg});")
    elif command.startswith("b64:"):
        command_msg = command[4:]
        try:
            print(base64.b64encode(command_msg.encode('utf-8')).decode('utf-8'))
        except Exception as E:
            print(f"Error(`{command_msg}`, `{E}`)")
    elif command.startswith("b64d:"):
        command_msg = command[5:]
        try:
            print(base64.b64decode(command_msg).decode('utf-8'))
        except Exception as E:
            print(f"Error(`{command_msg}`, `{E}`)")
    elif command.startswith("url:"):
        command_msg = command[4:]
        try:
            print(urllib.parse.quote(command_msg))
        except Exception as E:
            print(f"Error(`{command_msg}`, `{E}`)")
    elif command.startswith("urld:"):
        command_msg = command[5:]
        try:
            print(urllib.parse.unquote(command_msg))
        except Exception as E:
            print(f"Error(`{command_msg}`, `{E}`)")
    elif command.startswith("hex:"):
        command_msg = command[4:]
        try:
            print(str(hex(int(command_msg))).replace("0x", "", 1))
        except Exception as E:
            print(f"Error(`{command_msg}`, `{E}`);")
    elif command.startswith("bin:"):
        command_msg = command[4:]
        try:
            print(str(bin(int(command_msg))).replace("0b", "", 1))
        except Exception as E:
            print(f"Error(`{command_msg}`, `{E}`);")
    elif command.startswith("echo:") or command.startswith("echo "):
        command_msg = command[5:]
        res = re.sub(r'&#(\d+);', lambda x: chr(int(x.group(1))), command_msg).replace("&amp;", "&")
        res = re.sub(r'&#(\d+);', lambda x: chr(int(x.group(1))), res)
        print(res)
    elif command.startswith("utf8:"):
        command_msg = command[5:]
        try:
            print(str(command_msg.encode("u8"))[2:-1].replace("\\x", ""))
        except Exception as E:
            print(f"Error(`{command_msg}`, `{E}`);")
    elif command.startswith("gbk:"):
        command_msg = command[4:]
        try:
            print(str(command_msg.encode("gbk"))[2:-1].replace("\\x", ""))
        except Exception as E:
            print(f"Error(`{command_msg}`, `{E}`);")
    elif command.startswith("unic:"):
        command_msg = command[5:]
        try:
            print(str(command_msg.encode("unicode_escape"))[2:-1].replace("\\x", ""))
        except Exception as E:
            print(f"Error(`{command_msg}`, `{E}`);")
    elif command.startswith("CN:"):
        command_msg = command[3:]
        try:
            print(re.sub(r"[^\u4e00-\u9fa5]", "", command_msg))
        except Exception as E:
            print(f"Error({E});")
    elif command.startswith("bcd:"):
        command_msg = command[4:]
        try:
            print(bcd(int(command_msg)))
        except Exception as E:
            print(f"Error({E});")
    elif command.startswith("bcdd:"):
        command_msg = command[5:]
        try:
            print(bcdd(command_msg))
        except Exception as E:
            print(f"Error({E});")
    elif command.startswith("len:"):
        command_msg = command[4:]
        print(len(command_msg))
    elif command.startswith("comp:"):
        command_msg = command[5:]
        print("{:b}".format(int(command_msg) & 0b11111111111111111111))
    elif command.startswith("m4a:"):
        command_msg = command[4:]
        com = f'{path}\\ffmpeg\\bin\\ffmpeg.exe -i \"{path}\\{command_msg}.m4a\" -y -acodec libmp3lame -aq 0 \"{command_msg}.mp3\"'
        os.system(com)
        print(com)
    elif command.startswith("cd:") or command.startswith("cd "):
        command_msg = command[3:]
        try:
            if (os.path.isdir(command_msg)):
                os.chdir(command_msg)
                Path = os.getcwd()
            else:
                print(f"Error(路径异常:{command_msg});")
        except Exception as E:
            print(f"Erorr({E});")
    elif command.startswith("C:") or command.startswith("D:") or command.startswith("E:") or command.startswith("F:"):
        command_msg = command
        if (os.path.isdir(command_msg)):
            os.chdir(command_msg)
            Path = os.getcwd()
        else:
            print(f"Error(路径异常:{command_msg})")
    elif command.startswith("trans:"):
        command_msg = command[6:]
        try:
            print(trans(command_msg))
        except Exception as E:
            print(f"Error({E});")
    elif command.startswith("vim:"):
        command_msg = command[4:]
        os.system(f"start {path}/vim82/vim.exe {Path}/{command_msg}")
    elif command.startswith("vim "):
        command_msg = command[4:]
        os.system(f"{path}/vim82/vim.exe {Path}/{command_msg}")
    elif command.startswith("hx:"):
        command_msg = command[3:]
        os.system(f"start {path}/helix/hx.exe {Path}/{command_msg}")
    elif command.startswith("hx "):
        command_msg = command[3:]
        os.system(f"{path}/helix/hx.exe {Path}/{command_msg}")
    elif command.startswith("get "):
        command_msg = command[4:]
        try:
            res = requests.get(command_msg).text
            with open("target\\Get.html", "w", encoding="u8")as f:
                f.write(res)
            os.system(f"{path}/vim82/vim.exe target\\Get.html")
        except Exception as E:
            print(f"Error({E});")
    elif command.startswith("http:") or command.startswith("https:"):
        try:
            command_msg = re.sub("\?.*", "", command)
            # Ext = ["jpg", "jpeg", "webp", "png", "gif", "JPEG"]
            if True in [command_msg.endswith(i) for i in MediaExt]:
                res = requests.get(command).content
                if "?" in command:
                    file = re.search(r'/([^/]+(' + '|'.join(MediaExt) + '))$', command_msg).group(1)
                else:
                    file = re.search(r'/([^/]+(' + '|'.join(MediaExt) + '))$', command).group(1)
                with open(f"target\\{file}", "wb")as f:
                    f.write(res)
                size = os.path.getsize(f"target\\{file}") / (1024*1024)
                print(f"\033[36mSuccessfully Download To 'target\\{file}'({format(size, '0.2f')}MB){Color}")
            else:
                res = requests.get(command).text
                with open("target\\Get.html", "w", encoding="u8")as f:
                    f.write(res)
                os.system(f"{path}/vim82/vim.exe target\\Get.html")
        except Exception as E:
            print(f"Error({E});")
    elif command.startswith("rm "):
        command_msg = command[3:]
        if os.path.exists(command_msg):
            if os.path.isdir(command_msg):
                try:
                    os.rmdir(command_msg)
                except:
                    print("Error(目标文件夹不是空文件夹，可使用rd指令移除);")
            else:
                os.remove(command_msg)
            dir()
        else:
            print(f"Error(路径异常:{command_msg})")
    elif command.startswith("md "):
        command_msg = command[3:]
        try:
            os.mkdir(command_msg)
            dir(command_msg)
        except Exception as E:
            print(f"Error({E});")
    elif command.startswith("rd "):
        command_msg = command[3:]
        try:
            if os.path.isdir(command_msg):
                shutil.rmtree(command_msg)
                dir()
            else:
                print(f"Error(路径异常:{command_msg});")
        except Exception as E:
            print(f"Error({E});")
    elif command.startswith("sqlmap"):
        command_msg = command[6:]
        os.system(f"python {path}/sqlmap/sqlmap.py{command_msg}")
    elif True in [command.startswith(i) for i in SystemCommands]:
        os.system(command)
    elif command.startswith("var:") or command.startswith("var "):
        command_msg = command[4:]
        var = command_msg
        with open(f"{path}/config/var", "w", encoding="u8")as f:
            f.write(var)
    elif command.startswith("chat:") or command.startswith("chat "):
        command_msg = command[5:]
        print(Chat(command_msg))
    elif command.startswith("username ") or command.startswith("username:"):
        username = command[9:]
        with open(f"{path}/config/username", "w", encoding="u8")as f:
            f.write(username)
    elif command.startswith("cookie:"):
        command_msg = command[7:]
        try:
            cookie = CookieTrans(command_msg)
            print("{")
            for key in cookie: 
                print(f"    '{key}': '{cookie[key]}',")
            print("}")
        except Exception as E:
            print(f"Error({E});")
    elif command.startswith("clone "):
        command_msg = command[6:]
        os.system(f"git clone {DownloadConfig['git']}/{command_msg}")
    elif command.startswith("install "):
        command_msg = command[8:]
        os.system(f"pip install -i {DownloadConfig['pip']} {command_msg}")
    elif command.startswith("mpv ") or command.startswith("mpv:"):
        command_msg = command[4:]
        if os.path.exists(command_msg):
            os.system(f"{path}/tools/mpv.exe {command_msg}")
        else:
            print(f"Error(路径异常:{command_msg})")
    else:
        match command:
            case "test":
                print("[test]")
            case "file":
                os.system(f"start notepad {__file__}")
            case "e":
                sys.exit(0)
            case "exit":
                sys.exit(0)
            case "path":
                print(sys.executable)
            case "home":
                Path = path
                os.chdir(path)
            case "~":
                Path = path
                os.chdir(path)
            case "qq":
                print("2656980584")
            case "sdh":
                os.system("shutdown /h")
            case "sda":
                os.system("shutdown /a")
            case "sds":
                os.system("shutdown /s /t 0")
            case "sdr":
                os.system("shutdown /r /t 0")
            case "./":
                os.system(f"explorer {Path}")
            case ".":
                os.system("explorer .")
            case "。":
                os.system("explorer .")
            case "disk":
                if usePsutil:
                    disk=psutil.disk_usage('./')
                    print(f"[{disk.percent}%]-[{disk.used/1E9} GB/{disk.total/1E9} GB]-[Free:{disk.free/1E9} GB]")
                else:
                    print("Error('未启用');")
            case "power":
                if usePsutil:
                    try:
                        battery = psutil.sensors_battery()
                        print(f"{battery.percent}% Plugged:{battery.power_plugged}")
                    except Exception as E:
                        print(f"Error({E});")
                else:
                    print("Erorr('未启用');")
            case "date":
                print(datetime.date.today())
            case "timestamp":
                print(time.time())
            case "time":
                print(datetime.datetime.now().strftime("%H:%M:%S")) 
            case "abspath":
                print(os.path.abspath("."))
            case "realpath":
                print(os.path.realpath("."))
            case "cls":
                if sysMode == "Windows":
                    os.system("cls")
                else:
                    os.system("clear")
            case "dir":
                dir()
            case "ls":
                for i in os.listdir(Path):
                    color = '\033[37m' if os.path.isdir(os.path.join(path, i)) else '\033[36m'  
                    print(f"{color}{i}{Color}")
            case "lock":
                os.system("rundll32.exe user32.dll LockWorkStation")
            case "face":
                lis_eye = ["0","o","-","=","c","Q",chr(1021),chr(2406),chr(3120),chr(3360),chr(1505),chr(1496),chr(3566),chr(5054)]
                print(f"{random.choice(lis_eye)}.{random.choice(lis_eye)}")
            case "goodnight":
                print(f'现在是{datetime.date.today()} {datetime.datetime.now().strftime("%H:%M:%S")},祝你做个好梦,晚安。')
                if sysMode == "Windows":
                    os.system("shutdown /s /t 30")
            case "hi":
                print(f"Hello, [{username}]")
            case "task":
                os.system("taskmgr")
            case "temp":
                os.system("explorer %temp%")
            case "local":
                os.system("explorer %localappdata%")
            case "hosts":
                os.system("explorer C:\\Windows\\System32\\drivers\\etc")
            case "distance":
                try:
                    print(math.sqrt((float(input("X1:")) - float(input("X2:")))**2 + (float(input("Y1:")) - float(input("Y2:")))**2))
                except Exception as E:
                    print(f"Error({E});")
            case "vim":
                os.system(f"{path}/vim82/vim.exe")
            case "code":
                os.system(f"{path}/vim82/vim.exe B4mShell.py")
            case "Disk":
                os.system(f"start python {path}/tools/Disk.py")
            case "Time":
                os.system(f"start python {path}/tools/Time.py")
            case "v":
                os.system(f"{path}/tools/v.exe")
            case "Firework":
                os.system(f"{path}/tools/Firework.exe")
            case "Rain":
                os.system(f"{path}/tools/Rain.exe")
            case "help":
                os.system(f"{path}/vim82/vim.exe README.md")
            case "getcwd":
                print(os.getcwd())
            case "whoami":
                print(username)
            case "reset":
                confirm = input("# >是否清空配置文件以及全部缓存文件？(Y/n)")
                if confirm == "y" or confirm == "Y":
                    try:
                        shutil.rmtree("target")
                        shutil.rmtree("config")
                        dir() 
                    except Exception as E:
                        print(f"Error({E});")
            case "restart":
                if sysMode == "Windows":
                    os.system("cls")
                elif sysMode == "Linux":
                    os.system("clear")
                os.system("python B4mShell.py")
                sys.exit(0)
            case "rs":
                if sysMode == "Windows":
                    os.system("cls")
                elif sysMode == "Linux":
                    os.system("clear")
                os.system("python B4mShell.py")
                sys.exit(0)
            case "var":
                var = ""
            case "":
                pass
            case _:
                return False
        return True

def bcdd(data: str) -> int:
    """BCD码转十进制正整数
    Args:
        data (str): 二进制BCD码，如"10101101"
    Raises:
        TypeError: 输入非字符串！
        ValueError: 输入非二进制字符串！
    Returns:
        int: 返回十进制正整数
    """

    if not isinstance(data, str):
        raise TypeError("输入非字符串！")
    for num in data:
        if num not in ["0", "1"]:
            raise ValueError("输入非二进制字符串！")
    dec = 0
    # 计算二进制转十六进制后的位数
    digits = len(data) // 4 + 1
    # 按权相加法BCD转十进制整数
    for bit in range(1, digits + 1):
        dec += (int(data, 2) >> ((digits - bit) * 4) & 0x0F) * 10 ** (
            digits - bit
        )
    return dec

def bcd(dec: int, lenth: int = 19) -> str:
    """十进制正整数转指定长度BCD码
    Args:
        data (int): 十进制正整数
        lenth (int, optional): 指定长度(高位补0). Defaults to 19.
    Raises:
        TypeError: 输入非正整数！
        OverflowError: 输入十进制数过大，超过BCD码指定长度
    Returns:
        str: 返回BCD码字符串
    """

    if not isinstance(dec, int) or dec < 0:
        raise TypeError("输入非正整数！")
    bcd = 0
    for index, char in enumerate(str(dec)[::-1]):
        bcd += int(char) * 16**index
    # 转化为二进制字符串，高位补0
    pattern = f"{bcd:0{lenth}b}"
    if len(pattern) > lenth:
        raise OverflowError("输入十进制数过大，超过BCD码指定长度")
    return "".join(code for code in pattern)

	
def baidu(st0):
    url = "https://fanyi.baidu.com/sug"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    data_0 = {"kw": st0}
    try:
        res1 = requests.post(url=url, headers=headers, data=data_0, timeout=5)
    except Exception as E:
        return f"Error:{E}"
    res2 = res1.content.decode()
    json1 = json.loads(res2)
    data_1 = json1['data'][0]['v']
    return data_1.replace("\n", "")


def youdao(msg):
    a = (msg)
    content = a
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15812376682056'
    data['sign'] = 'a1246b257926af8432be022564ff79f5'
    data['ts'] = '1581237668205'
    data['bv'] = '656f750600466990f874a839d9f5ad23'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data = urllib.parse.urlencode(data).encode('utf-8')
    try:
        response = urllib.request.urlopen(url, data, timeout=5)
    except Exception as E:
        return f"Error:{E}"
    html = response.read().decode('utf-8')
    target = json.loads(html)
    s = ("%s" % (target['translateResult'][0][0]['tgt']) + "\n")
    return s.replace("\n", "")

def trans(text):
    try:
        return baidu(text)
    except Exception as E:
        return youdao(text)

def dir(file=""):
    color = ""
    print("", end=f"\033[43m {BgColor} ")
    for i in os.listdir(Path):
        if i == file:
            color = '\033[35m'
        elif os.path.isdir(os.path.join(path, i)):
            color = '\033[37m'  
        else:
            color = '\033[36m'
        print(f"{color}{i}{Color}", end=f" \033[43m {BgColor} ")
    print()

def MFZN(msg, prompt=""):
    api = "https://api.xn--9kqc40tsudv9iv0e30d65lqnh8rd27vpo0bfyr1l7clwq.com/api/chat-process"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '252',
        'Content-Type': 'application/json',
        'Host': 'api.xn--9kqc40tsudv9iv0e30d65lqnh8rd27vpo0bfyr1l7clwq.com',
        'Origin': 'https://mfzn.xn--9kqc40tsudv9iv0e30d65lqnh8rd27vpo0bfyr1l7clwq.com',
        'Referer': 'https://mfzn.xn--9kqc40tsudv9iv0e30d65lqnh8rd27vpo0bfyr1l7clwq.com/',
        'Sec-Ch-Ua': '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
    }
    data={
        "prompt": f"{msg}",
        "options": {},
        "systemMessage": f"{prompt}",
        "temperature": 0.8,
        "top_p": 1
    }
    res = requests.post(api, headers=headers, json=data).text.split("\n")[-1]
    try:
        return json.loads(res)['text']
    except Exception as E:
        return f"Error({E});"

Chat = MFZN

def CookieTrans(msg):
    cookie = {}
    for line in msg.split(';'):
        key,value = line.split('=',1)
        value = re.sub(r"^\s*", "", value).replace("'", "\\'")
        key = re.sub(r"^\s*", "", key).replace("'", "\\'")
        cookie[key] = value
    return cookie






if __name__ == "__main__":
    Banner_1 = """
 ____  _  _   __  __  __    ___   ___  
| __ )| || | |  \/  |/ /_  / _ \ / _ \ 
|  _ \| || |_| |\/| | '_ \| | | | | | |
| |_) |__   _| |  | | (_) | |_| | |_| |
|____/   |_| |_|  |_|\___/ \___/ \___/ 
                                         
    """
    Banner_2 = """
oooooooooo.        .o   ooo        ooooo     .ooo     .oooo.     .oooo.   
`888'   `Y8b     .d88   `88.       .888'   .88'      d8P'`Y8b   d8P'`Y8b  
 888     888   .d'888    888b     d'888   d88'      888    888 888    888 
 888oooo888' .d'  888    8 Y88. .P  888  d888P"Ybo. 888    888 888    888 
 888    `88b 88ooo888oo  8  `888'   888  Y88[   ]88 888    888 888    888 
 888    .88P      888    8    Y     888  `Y88   88P `88b  d88' `88b  d88' 
o888bood8P'      o888o  o8o        o888o  `88bod8'   `Y8bd8P'   `Y8bd8P'  
    """

    if sysMode == "Windows":
        os.system("color 9")
        print(Banner_2)
    elif sysMode == "Linux":
        print(Banner_1)
    else:
        print("Error(系统模式配置异常,已改用Linux系统模式);")
        with open("target\\sysMode", "w")as f:
            f.write("Linux")
        sysMode = "Linux"
    print("\"" + random.choice([
    "你想堕落没人拦你，但是你想出人头地？那拦你的人就多了。",
    "正因为你有能力跨越，这个考验才会降临。",
    "登高望远，不是为了让整个世界看见，而是为了看见整个世界。",
    "惟沉默是最高的轻蔑。",
    "任何消耗自己的人和事，多看一眼都是你的不对。",
    ]) + "\"")
    Red = "\033[31m"
    Cyan = "\033[36m"
    Yellow = "\033[33m"
    Purple = "\033[35m"
    Clear = "\033[0m"
    Back = "\033[46m"
    while True:
        if usePsutil:
            try:
                battery = psutil.sensors_battery()
                storageC = psutil.disk_usage('C:/').free / 1E9
                storageD = psutil.disk_usage('D:/').free / 1E9
                if var == "":
                    command = input(f'{Color}{Path} C:{Red if storageC<1 else Color}{format(storageC, "0.2f")}{Color}GB D:{Red if storageD<1 else Color}{format(storageD, "0.2f")}{Color}GB---[{username}] \033[47m\033[30m{datetime.date.today()} {datetime.datetime.now().strftime("%H:%M:%S")}{Clear}{Color} {Yellow + "⚡" if battery.power_plugged else ""}{Red if battery.percent<=10 else Cyan if battery.percent>90 else Color}{battery.percent}%{Yellow}\n$ >{Color}')
                else:
                    command = input(f'{Color}{Path} C:{Red if storageC<1 else Color}{format(storageC, "0.2f")}{Color}GB D:{Red if storageD<1 else Color}{format(storageD, "0.2f")}{Color}GB---[{username}] \033[47m\033[30m{datetime.date.today()} {datetime.datetime.now().strftime("%H:%M:%S")}{Clear}{Color} {Yellow + "⚡" if battery.power_plugged else ""}{Red if battery.percent<=10 else Cyan if battery.percent>90 else Color}{battery.percent}% {Purple}{var}{Yellow}\n$ >{Color}')
            except:
                usePsutil = False
        else:
            if var == "":
                command = input(f'{Color}{Path}---[{username}] \033[47m\033[30m{datetime.date.today()} {datetime.datetime.now().strftime("%H:%M:%S")}{Clear}{Color} {Yellow}\n$ >{Color}')
            else:
                command = input(f'{Color}{Path}---[{username}] \033[47m\033[30m{datetime.date.today()} {datetime.datetime.now().strftime("%H:%M:%S")}{Clear}{Purple} {var}{Yellow}\n$ >{Color}')
        command = command.replace("{var}", var).replace("{path}", path)
        Fix = command[-2:]
        if Fix.startswith("*"):
            try:
                num = int(Fix[1:])
                for i in range(num):
                    MyShell(command[:-2])
            except Exception as E:
                print(f"Error({E});")
        elif MyShell(command):
            pass
        else:
            try:
                exec(f"print({command})")
            except:
                pass
