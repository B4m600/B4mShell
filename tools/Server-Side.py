import socket,threading

def SERVER(localhost,port,name):
  # localhost=socket.gethostbyname(socket.gethostname())
  # localhost="47.93.35.56"
  break_service=1
  temp_once_service=0
  server_sk = socket.socket()
  print(f"|>>服务端建立成功,使客户端输入本机ip:{localhost}即可开启对话进程,此前请等待对方的连接.")

  server_sk.bind((localhost, port))
  server_sk.listen()
  conn, address = server_sk.accept()

  def Input():
    global break_service
    while True:
        Inp = f"[{name}]>>"+input(f"[{name}]<<")
        if Inp==f"[{name}]>>"+'exit':
            conn.sendall(bytes("|>>服务端已断开连接.", encoding='utf-8'))
            break_service=0
            break
        else:
            try:
                conn.sendall(bytes(Inp, encoding='utf-8'))
            except:
                print("|>>对方已终止程序.")
                break
    print("*>>断开连接成功.")
    server_sk.close()
  T2=threading.Thread(target=Input)




  while break_service == 1:
    if temp_once_service == 0:
        temp_once_service = 1
        conn.sendall(bytes("|>>连接成功,通过指令'exit'退出.", encoding='utf-8'))
        T2.start()
    try:
        msg_client = str(conn.recv(1024), encoding='utf-8')
        if msg_client == 'exit':
            print("|>>远程主机已断开连接,即将终止服务端.")
            break
        else:
            print("\033[9D"+msg_client+f"\n[{name}]<<",end="")
    except:
        print("|>>远程主机已断开连接,即将终止服务端.")
        break

SERVER("10.7.43.115",140,"Giao")

