import socket,threading,re,sys,importlib
name="DEMO"
# module=importlib.import_module("ChatTerminal5")
#name=module.name
sys.path.append("../")
# from ChatTerminal5 import name
print(name)

def CLIENT(IP,port,name):
  global break_client
  if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',IP):
    while True:
        if IP == 'exit' or IP == 'exit()':
            exit()
        else:
            if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',IP):
                break
            else:
                IP=input("IP格式错误,请再次输入(输入exit退出):")
  break_client=1
  temp_once_client=0
  client_sk = socket.socket()

  client_sk.connect((IP, port))

  def Print():
    global break_client
    while True:
        try:
            msg_server = str(client_sk.recv(1024), encoding='utf-8')
            print("\033[9D"+msg_server+f"\n[{name}]<<",end="")
            if msg_server == '|>>服务端已断开连接.':
                client_sk.sendall(bytes("exit", encoding='utf-8'))
                print("|>>已断开连接(2).")
                break_client = 0
                break
        except:
            break_client = 0
            print("|>>已断开连接(1).")
            break
    print(f"|>>已断开连接(3),mode={break_client}.")

  T=threading.Thread(target=Print)

  while break_client == 1:
    if temp_once_client == 0:
        temp_once_client=1
        client_sk.sendall(bytes(f"[{name}]已连接成功.", encoding='utf-8'))
        T.start()
    inp = f"[{name}]>>"+input(f"[{name}]<<")


    if inp == f"[{name}]>>"+'exit':
        client_sk.sendall(bytes(f"[{name}]已断开连接.", encoding='utf-8'))
        break_client=0
        client_sk.close()
        break
    else:
        client_sk.sendall(bytes(inp, encoding='utf-8'))
  print("*>>断开连接成功")
  client_sk.close()

try:
    # CLIENT(input("|>>请正确输入局域网内已启动服务器端程序的用户IP(输入exit退出):"),139,name)
    CLIENT("Client-Side.py",140,"TEST")
except:
    print("连接失败,请确保所输入IP有效且已运行'Server-Side'程序,并且位于局域网内.")
    exit()
