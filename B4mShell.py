import os, sys

path = os.path.dirname(__file__)
Path = path
Color = "\033[32m"
BgColor = "\033[40m"
Red = "\033[31m"
Cyan = "\033[36m"
Yellow = "\033[33m"
Blue = "\033[34m"
Purple = "\033[35m"
Clear = "\033[0m"
Back = "\033[46m"
White = "\033[37m"
def error(msg):
    print(f"\033[31mError({msg});{Color}")
def warning(msg):
    print(f"\033[33mWarning({msg});{Color}")

if not os.path.exists(f"{path}/config"):
    os.mkdir(f"{path}/config")
if not os.path.exists(f"{path}/target"):
    os.mkdir(f"{path}/target")
sysMode = "Linux"
if os.path.exists(f"{path}/config/sysMode"):
    with open(f"{path}/config/sysMode", "r")as f:
        if f.read() == "Windows":
            sysMode = "Windows"
        elif f.read() == "Linux":
            sysMode = "Linux"
        else:
            error("读取sysMode失败")
else:
    Choice = input("# >是否使用Windows系统模式？(Y/n):")
    if Choice == "Y" or Choice == "y":
        sysMode = "Windows"
        with open(f"{path}/config/sysMode", "w")as f:
            f.write(sysMode)
    elif Choice == "N" or Choice == "n":
        sysMode = "Linux"
        with open(f"{path}/config/sysMode", "w")as f:
            f.write(sysMode)
    elif Choice == "e" or Choice == "E":
        sys.exit(0)
    else:
        print("# >已默认使用Linux系统模式,下次启用再次询问。")
if sysMode == "Windows":
    usePsutil = True
else:
    usePsutil = False

import datetime, time, re, hashlib, shutil, socket
import random, base64, urllib, requests, datetime, json, math, sympy
try:
    from PIL import Image
except Exception as E:
    error(E)
try:
    from tools import netifaces
except Exception as E:
    error(E)
if usePsutil:
    import psutil
username = socket.gethostname()
if os.path.exists(f"{path}/config/username"):
    with open(f"{path}/config/username", "r", encoding="u8")as f:
        username = f.read()
else:
    username = input("# >输入用户名(之后可使用username指令修改):")
    with open(f"{path}/config/username", "w", encoding="u8")as f:
        f.write(username)

SystemCommands = ["python", "java", "javac", "node", "pip", "npm", "pnpm", "docker", "ping", "subl", "cmd",
                  "calc", "osk", "mmc", "mstsc", "dvdplay", "system.cpl", "regedit", "resmon",
                  "cleanmgr", "snippingtool", "magnify", "git", "nano", "chmod", "curl", "curl", "javadoc", "jar",
                  "telnet", "ssh", "gradle", "color", 
                 ]
BusyBoxCommands = ["ar", "arch", "ascii", "ash", "awk", "base32", "base64", "basename", "bash", "bc",
                   "bunzip2", "busybox", "bzcat", "bzip2", "cal", "cat", "cdrop", "chattr", "chmod", 
                   "cksum", "clear", "cmp", "comm", "cp", "cpio", "crc32", "cut",
                   "date", "dc", "dd", "df", "diff", "dirname", "dos2unix", "dpkg", "dpkg-deb", 
                   "drop", "du", "echo", "ed", "egrep", "env", "expand", "expr", "factor", "false", 
                   "fgrep", "find", "fold", "free", "fsync", "ftpget", "ftpput", "getopt", "grep", 
                   "groups", "gunzip", "gzip", "hd", "head", "hexdump", "httpd", "iconv", "id", "inotifyd", 
                   "install", "ipcalc", "jn", "kill", "killall", "less", "link", "ln", "logname", "ls", 
                   "lsattr", "lzcat", "lzma", "lzop", "lzopcat", "make", "man", "md5sum", "mkdir", 
                   "mktemp", "mv", "nc", "nl", "nproc", "od", "paste", "patch", "pdpmake", "pdrop", 
                   "pgrep", "pidof", "pipe_progress", "pkill", "printenv", "printf", "ps", "pwd", 
                   "readlink", "realpath", "reset", "rev", "rm", "rmdir", "rpm", "rpm2cpio", 
                   "sed", "seq", "sh", "sha1sum", "sha256sum", "sha3sum", "sha512sum", "shred", "shuf", 
                   "sleep", "sort", "split", "ssl_client", "stat", "strings", "su", "sum", "sync", "tac", 
                   "tail", "tar", "tee", "test", "time", "timeout", "touch", "tr", "true", "truncate", 
                   "ts", "tsort", "ttysize", "uname", "uncompress", "unexpand", "uniq", "unix2dos", "unlink", 
                   "unlzma", "unlzop", "unxz", "unzip", "uptime", "usleep", "uudecode", "uuencode", "vi",
                    "watch", "wc", "wget", "which", "whoami", "whois", "xargs", "xxd", "xz", "xzcat", "yes", "zcat",
                  ]
MediaExt = ["jpg", "jpeg", "webp", "png", "gif", "JPEG", "mp3", "wav", "mp4", "m4a"]
var = ""
UserVars = {"this": f"B4mShell.py",
            "hostname": socket.gethostname(),
            "host": socket.gethostbyname(socket.gethostname()),
            "date": datetime.date.today(),
            "timestamp": time.time(),
            "time": datetime.datetime.now().strftime("%H:%M:%S"),
            }
UrlConfig = {
    "pip": "https://pypi.tuna.tsinghua.edu.cn/simple",
    "git": "https://ghproxy.com",
    "getip": "http://ifconfig.me/ip",
    "myip": "https://myip.ipip.net",
}
welcom = [
        "你想堕落没人拦你，但是你想出人头地？那拦你的人就多了。",
        "正因为你有能力跨越，这个考验才会降临。",
        "登高望远，不是为了让整个世界看见，而是为了看见整个世界。",
        "惟沉默是最高的轻蔑。",
        "任何消耗自己的人和事，多看一眼都是你的不对。",
        "自律不是束缚自己，而是保证自己不被束缚。",
        "永远没有正确的选择，而要让选择变得正确。",
        "钟表可以回到原点，但再也不是昨天。",
        "今天不想跑，所以才去跑。",
]
dic_formula = {'X': '(x)', '[': '(', ']': ')', 'S': 'sin', 'C': 'cos', 'T': 'tan',
               'As': 'arcsin', 'At': 'arctan', 'Ac': 'arccos',
               '...': '(x)', '..': 'x', 'P': '\\pi', '---': '$', '***': '^',
}
data = {}
cookies = {}
headers = {}
last = ""
if os.path.exists("config/var"):
    with open("config/var", "r", encoding="u8")as f:
        var = f.read()
def MyShell(command, mode=0):
    global Path, path, Color, var, username, MediaExt, data, cookies
    if command.startswith("print:"):
        Vars = globals()
        cmd = command[6:]
        if cmd in Vars:
            print(f"{cmd}:{eval(cmd)}")
        else:
            print(f"{cmd}:None")
        return True
    elif command.startswith("exec:"):
        cmd = command[5:]
        try:
            exec(cmd)
        except Exception as E:
            error(E)
    elif command.startswith("md5:"):
        cmd = command[4:]
        try:
            md = hashlib.md5()
            md.update(cmd.encode('utf-8'))
            print(md.hexdigest())
        except:
            error(cmd)
    elif command.startswith("b64:"):
        cmd = command[4:]
        try:
            print(base64.b64encode(cmd.encode('utf-8')).decode('utf-8'))
        except Exception as E:
            error(f"`{cmd}`, `{E}`")
    elif command.startswith("b64d:"):
        cmd = command[5:]
        try:
            print(base64.b64decode(cmd).decode('utf-8'))
        except Exception as E:
            error(f"`{cmd}`, `{E}`")
    elif command.startswith("url:"):
        cmd = command[4:]
        try:
            print(urllib.parse.quote(cmd))
        except Exception as E:
            error(f"`{cmd}`, `{E}`")
    elif command.startswith("urld:"):
        cmd = command[5:]
        try:
            print(urllib.parse.unquote(cmd))
        except Exception as E:
            error(f"`{cmd}`, `{E}`")
    elif command.startswith("hex:"):
        cmd = command[4:]
        try:
            print(str(hex(int(cmd))).replace("0x", "", 1))
        except Exception as E:
            error(f"`{cmd}`, `{E}`")
    elif command.startswith("bin:"):
        cmd = command[4:]
        try:
            print(str(bin(int(cmd))).replace("0b", "", 1))
        except Exception as E:
            error(f"`{cmd}`, `{E}`")
    elif command.startswith("oi:"):
        cmd = command[3:]
        try:
            print(str(bin(int(cmd))).replace("0b", "", 1).replace("0","o").replace("1","i"))
        except Exception as E:
            error(f"`{cmd}`, `{E}`")
    elif command.startswith("echo "):
        cmd = command[5:]
        res = re.sub(r'&#(\d+);', lambda x: chr(int(x.group(1))), cmd).replace("&amp;", "&")
        res = re.sub(r'&#(\d+);', lambda x: chr(int(x.group(1))), res)
        print(res)
    elif command.startswith("utf8:"):
        cmd = command[5:]
        try:
            print(str(cmd.encode("u8"))[2:-1].replace("\\x", ""))
        except Exception as E:
            error(f"`{cmd}`, `{E}`")
    elif command.startswith("gbk:"):
        cmd = command[4:]
        try:
            print(str(cmd.encode("gbk"))[2:-1].replace("\\x", ""))
        except Exception as E:
            error(f"`{cmd}`, `{E}`")
    elif command.startswith("unic:"):
        cmd = command[5:]
        try:
            print(str(cmd.encode("unicode_escape"))[2:-1].replace("\\x", ""))
        except Exception as E:
            error(f"`{cmd}`, `{E}`")
    elif command.startswith("cn:"):
        cmd = command[3:]
        try:
            print(re.sub(r"[^\u4e00-\u9fa5]", "", cmd))
        except Exception as E:
            error(E)
    elif command.startswith("bcd:"):
        cmd = command[4:]
        try:
            print(bcd(int(cmd)))
        except Exception as E:
            error(E)
    elif command.startswith("bcdd:"):
        cmd = command[5:]
        try:
            print(bcdd(cmd))
        except Exception as E:
            error(E)

    elif command.startswith("len:"):
        cmd = command[4:]
        print(len(cmd))
    elif command.startswith("comp:"):
        cmd = command[5:]
        print("{:b}".format(int(cmd) & 0b11111111111111111111))
    elif command.startswith("m4a "):
        cmd = command[4:]
        com = f'{path}\\ffmpeg\\bin\\ffmpeg.exe -i \"{cmd}\" -y -acodec libmp3lame -aq 0 \"{cmd}.mp3\"'
        os.system(com)
        print(com)
    elif command.startswith("webp "):
        cmd = command[5:]
        com = f'{path}\\ffmpeg\\bin\\ffmpeg.exe -i \"{cmd}\" \"{cmd}.png\"'
        os.system(com)
        print(com)
    elif command.startswith("cd "):
        cmd = command[3:]
        if cmd == "~":
            cmd = path
        try:
            if (os.path.isdir(cmd)):
                os.chdir(cmd)
                Path = os.getcwd()
            else:
                error(f"路径异常:{cmd}")
        except Exception as E:
            error(E)
    elif command.startswith("C:") or command.startswith("D:") or command.startswith("E:") or command.startswith("F:"):
        cmd = command
        if (os.path.isdir(cmd)):
            os.chdir(cmd)
            Path = os.getcwd()
        else:
            error(f"路径异常:{cmd}")
    elif command.startswith("trans "):
        cmd = command[6:]
        try:
            print(trans(cmd))
        except Exception as E:
            error(E)
    elif command.startswith("vim "):
        cmd = command[4:]
        os.system(f"{path}/vim82/vim.exe {Path}/{cmd}")
    elif command.startswith("hx "):
        cmd = command[3:]
        os.system(f"{path}/helix/hx.exe {Path}/{cmd}")
    elif command.startswith("get "):
        cmd = command[4:]
        try:
            session = requests.Session()
            if "-data " in cmd:
                cmd = cmd.replace("-data ", "")
                session.data = data
                if len(data) == 0:
                    warning(f"data为空")
            if "-cookies " in cmd:
                cmd = cmd.replace("-cookies ", "")
                session.cookies = cookies
                if len(cookies) == 0:
                    warning(f"cookies为空")
            if "-headers " in cmd:
                cmd = cmd.replace("-headers ", "")
                session.headers = headers
                if len(headers) == 0:
                    warning(f"headers为空")
            res = session.get(cmd).text
            with open("target\\Get.html", "w", encoding="u8")as f:
                f.write(res)
            os.system(f"{path}/vim82/vim.exe target\\Get.html")
        except Exception as E:
            error(E)
    elif command.startswith("post "):
        cmd = command[5:]
        try:
            session = requests.Session()
            if "-data " in cmd:
                cmd = cmd.replace("-data ", "")
                session.data = data
                if len(data) == 0:
                    warning(f"data为空")
            if "-cookies " in cmd:
                cmd = cmd.replace("-cookies ", "")
                session.cookies = cookies
                if len(cookies) == 0:
                    warning(f"cookies为空")
            if "-headers " in cmd:
                cmd = cmd.replace("-headers ", "")
                session.headers = headers
                if len(headers) == 0:
                    warning(f"headers为空")
            res = session.post(cmd).text
            with open("target\\Post.html", "w", encoding="u8")as f:
                f.write(res)
            os.system(f"{path}/vim82/vim.exe target\\Post.html")
        except Exception as E:
            error(E)
    elif command.startswith("http:") or command.startswith("https:"):
        try:
            cmd = re.sub("\?.*", "", command)
            # Ext = ["jpg", "jpeg", "webp", "png", "gif", "JPEG"]
            if True in [cmd.endswith(i) for i in MediaExt]:
                res = requests.get(command).content
                if "?" in command:
                    file = re.search(r'/([^/]+(' + '|'.join(MediaExt) + '))$', cmd).group(1)
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
            error(E)
    elif command.startswith("rm "):
        cmd = command[3:]
        if not "|" in cmd:
            if os.path.exists(cmd):
                if os.path.isdir(cmd):
                    try:
                        os.rmdir(cmd)
                    except:
                        error("目标文件夹不是空文件夹，可使用rd指令移除")
                else:
                    os.remove(cmd)
                dir()
            else:
                error(f"路径异常:{cmd}")
        else:
            cmds = cmd.split("|")
            for cmd in cmds:
                if os.path.exists(cmd):
                    if os.path.isdir(cmd):
                        try:
                            os.rmdir(cmd)
                        except:
                            error("目标文件夹不是空文件夹，可使用rd指令移除")
                    else:
                        os.remove(cmd)
                else:
                    error(f"路径异常:{cmd}")
            dir()

    elif command.startswith("md "):
        cmd = command[3:]
        try:
            os.mkdir(cmd)
            dir(cmd)
        except Exception as E:
            error(E)
    elif command.startswith("rd "):
        cmd = command[3:]
        try:
            if not "|" in cmd:
                if os.path.isdir(cmd):
                    shutil.rmtree(cmd)
                    dir()
                else:
                    error(f"路径异常:{cmd}")
            else:
                cmds = cmd.split("|")
                for cmd in cmds:
                    if os.path.isdir(cmd):
                        shutil.rmtree(cmd)   
                    else:
                        error(f"路径异常:{cmd}")
                dir()
        except Exception as E:
            error(E)
    elif command.startswith("sqlmap"):
        cmd = command[6:]
        os.system(f"python {path}/sqlmap/sqlmap.py{cmd}")
    elif command.startswith("var:"):
        cmd = command[4:]
        var = cmd
        with open(f"{path}/config/var", "w", encoding="u8")as f:
            f.write(var)
    elif command.startswith("var "):
        cmd = command[4:]
        if cmd.count("=") > 0:
            lis = cmd.split("=")
            for i in lis[:-1]:
                UserVars[i] = lis[-1]
        else:
            var = cmd
            with open(f"{path}/config/var", "w", encoding="u8")as f:
                f.write(var)
    elif command.startswith("chat:") or command.startswith("chat "):
        cmd = command[5:]
        print(Chat(cmd))
    elif command.startswith("username ") or command.startswith("username:"):
        username = command[9:]
        with open(f"{path}/config/username", "w", encoding="u8")as f:
            f.write(username)
    elif command.startswith("cookies:"):
        cmd = command[8:]
        try:
            cookies = CookieTrans(cmd)
            print("{")
            for key in cookies: 
                print(f"    '{key}': '{cookies[key]}',")
            print("}")
        except Exception as E:
            error(E)
    elif command.startswith("data:"):
        cmd = command[5:]
        try:
            data = DataTrans(cmd)
            print("{")
            for key in data: 
                print(f"    '{key}': '{data[key]}',")
            print("}")
        except Exception as E:
            error(E)
    elif command.startswith("clone "):
        cmd = command[6:]
        os.system(f"git clone {UrlConfig['git']}/{cmd}")
    elif command.startswith("install "):
        cmd = command[8:]
        os.system(f"pip install -i {UrlConfig['pip']} {cmd}")
    elif command.startswith("mpv ") or command.startswith("mpv:"):
        cmd = command[4:]
        if os.path.exists(cmd):
            os.system(f"{path}/tools/mpv.exe {cmd}")
        else:
            error(f"路径异常:{cmd}")
    elif command.startswith("read ") or command.startswith("read:"):
        cmd = command[5:]
        if os.path.exists(cmd):
            os.system(f"{path}/tools/mpv.exe -vo null {cmd}")
        else:
            os.system(f"{path}/tools/edge-tts.exe --voice zh-CN-XiaoyiNeural --text '{cmd}' --write-media {path}/target/output.mp3")
            os.system(f"{path}/tools/mpv.exe -vo null {path}/target/output.mp3")
    elif command.startswith("N "):
        cmd = command[2:]
        os.system(f"{path}/N_m3u8DL/N.exe {cmd}")
    elif True in [command.startswith(i + " ") for i in BusyBoxCommands] and not True in [command == i for i in BusyBoxCommands]:
        os.system(f"{path}/tools/busybox.exe {command}")
    elif command.startswith("busybox "):
        cmd = command[8:]
        os.system(f"{path}/tools/busybox.exe {cmd}")
    elif command.startswith("nmap "):
        cmd = command[5:]
        os.system(f"{path}/nmap/nmap.exe {cmd}")
    elif command.startswith("hydra "):
        cmd = command[6:]
        os.system(f"{path}/hydra/hydra.exe {cmd}")
    elif command.startswith("mdv "):
        cmd = command[4:]
        os.system(f"python {path}/mdv/markdownviewer.py {cmd}")
    elif command.startswith("glow "):
        cmd = command[5:]
        os.system(f"{path}/glow/glow.exe {cmd}")
    elif command.startswith("b4m ") or command.startswith("run "):
        cmd = command[4:]
        if os.path.exists(cmd):
            os.system(f"python {__file__} {cmd}")
        elif os.path.exists(cmd+".b4m"):
            os.system(f"python {__file__} {cmd}.b4m")
        else:
            error(f"文件:{cmd}未找到")
    elif command.startswith("host "):
        cmd = command[5:]
        try:
            print(socket.gethostbyname(cmd))
        except Exception as E:
            error(E)
    elif command.startswith("hostname "):
        cmd = command[9:]
        pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'  
        if re.match(pattern, cmd):  
            try:
                print(socket.gethostbyaddr(cmd))
            except Exception as E:
                error(E)
        else:
            error("请输入规范的IP地址")
    elif command.startswith("cupp "):
        cmd = command[5:]
        os.system(f"python {path}/cupp/cupp.py {cmd}")
    elif command.startswith("love "):
        cmd = command[5:]
        print('\n'.join([''.join([(cmd[(x-y)%len(cmd)] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ') for x in range(-30,30)]) for y in range(15,-15,-1)]))
    # elif command.startswith("svg "):
    #     cmd = command[4:]
    #     if os.path.isdir(cmd):
    #         for filename in os.listdir(cmd):  
    #             if filename.endswith('.svg'):  
    #                 svg_path = os.path.join(cmd, filename)  
    #                 png_path = os.path.join(f"{path}/target", os.path.splitext(filename)[0] + '.png')  
    #                 convert_svg_to_png(svg_path, png_path)  
    #     elif cmd.endswith(".svg"):
    #         convert_svg_to_png(cmd)
    elif command.startswith("wipe ") or command == "wipe":
        if command == "wipe":
            cmd = "."
        else:
            cmd = command[5:]
        if os.path.isdir(cmd):
            targets = os.listdir(cmd)
            isOrder = input("根据文件名(比如'a_1','a_10','a_2')搜索到的第一个数字进行排序?(Y/n)")
            if isOrder == "y" or isOrder == "Y":
                targets = sorted(targets, key=custom_sort)
            targets_raw = targets.copy()
            print(Cyan+"Targets:",targets,Color)
            pat = input("Wipe Pattern(enter 'e' to exit):")
            if pat == "e" or pat == "exit":
                print(White+"[exit]"+Color)
            else:
                for i in range(len(targets)):
                    if re.search(pat,targets[i]):
                        wipe = re.search(pat,targets[i]).group()
                        print("Find:",targets[i],",Wipe:",wipe)
                        targets[i] = targets[i].replace(wipe,"")
                print(Cyan+"Res:",targets,Color)
                confirm = input("Continue?(Order/Reverse/Y/n/OrRe):")
                if confirm == "Reverse" or  confirm == "OrRe":
                    targets.reverse()
                if confirm == "Order" or confirm == "OrRe":
                    Postfix = input("Postfix(enter '{i}' to replace order):")
                    for i in range(len(targets)):
                        targets[i] += Postfix.replace("{i}",str(i))
                print(Cyan+"Res:",targets,Color)
                if confirm == "Y" or confirm == "y" or confirm == "Reverse" or confirm == "Order":
                    for i in range(len(targets_raw)):
                        rename_target = os.path.join(cmd,targets_raw[i])
                        rename_res = os.path.join(cmd,targets[i]+"_")
                        os.rename(rename_target,rename_res)
                        print(f"{Yellow}Successfully Rename:{rename_target} to {rename_res};{Color}")
                else:
                    print(White+"[exit]"+Color)
                confirm = input("Continue(Remove:'_')?(Y/n):")
                if confirm == "Y" or confirm == "y":
                    for i in range(len(targets_raw)):
                        rename_res = os.path.join(cmd,targets[i])
                        if rename_res[-1] != "_":
                            print(f"{Red}Fail to Rename:{rename_res},not found '_';")
                        else:
                            os.rename(rename_res,rename_res[:-1])
                            print(f"{Yellow}Successfully Rename:{rename_res} to {rename_res[:-1]};{Color}")
        else:
            error("not a path:"+cmd)
    elif command.startswith("suffix "):
        cmd = command[7:]
        for i in os.listdir():
            os.rename(i,i+cmd)
        print(Yellow+"Successfully;"+Color)
    elif re.match(r'^\d[\d\s\(\)\+\-\*/\.]*$',command):
        try:
            exec(f"print({command})") 
        except Exception as E:
            error(E)

#--------------------------------------------------------------START
    elif command == 'lim' or command == "limit":
        print(f"\033[1A\033[30C\033[32m[使用指令'dic_f'查看快捷替换内容;使用'E'表示自然常数;使用'pi'表示圆周率常数;使用指令'help'查看更多;]{Color}")
        formula = "A"
        x, y, z = sympy.symbols("x y z")
        sym = ''
        m = x
        n = sympy.oo
        while True:
            brand = f"\033[37mlim(f(x),{m}->{n},{sym})\033[32m"
            formula = input(f"{brand}<<")
            if not re.search(r'\S', formula):
                pass
            elif formula == 'exit' or formula == 'exit()' or formula == 'e' or formula == 'E':
                break
            elif formula == 'integrate' or formula == 'int' or formula == 'inte' or formula == 'i':
                auto_mode = 1
                msg = 'integrate'
                break
            elif formula == 'diff' or formula == 'd' or formula == 'D':
                auto_mode = 1
                msg = 'diff'
                break
            elif re.search(r'm\[(?P<M>[\w/]+)\]', formula):
                m = re.search(r'm\[(?P<M>[\w/]+)\]', formula).group("M")
                m = sympy.sympify(m)
            elif re.match(r'n\[(?P<N>[\w/]+)\]', formula):
                n = re.match(r'n\[(?P<N>[\w/]+)\]', formula).group("N")
                n = sympy.sympify(n)
            elif re.match(r'((to)|t)\s+[\w/]+', formula):
                # print(re.match(r'((to)|t)\s*\w+', formula).group())
                n = re.sub(r'((to)|t)\s+', '', formula)
                try:
                    n = sympy.sympify(n)
                except:
                    print("Error(n),try again.")
                    n = 0
            elif re.search(r'o\[(?P<O>[+-])\]', formula):
                sym = re.search(r'o\[([+-])\]', formula).group("O")
            elif re.search(r'o\[=\]', formula):
                sym = '+'
            elif re.search(r'o\[\w+\]', formula):
                sym = ''
            elif formula == '+' or formula == '=':
                sym = '+'
            elif formula == '-' or formula == '_':
                sym = '-'
            elif formula == 'o[]' or formula == 'o':
                sym = ''
            elif formula == 'help':
                print("""
                Func:limit(F,m,n,o);
                Command:'m[...]':变量(默认x);  
                        'n[...]'/'to ...':变量趋近于的值(不可为负值);
                        'o[+]'/'o[-]'/'+'/'-':更改趋近于的值的方向;
                        'o[]':消除趋近于的值的方向;
                        'exit'/'e':返回;""")
            elif formula == 'dic_formula' or formula == 'dic_f':
                print(dic_formula)
            else:
                try:
                    for key in dic_formula.keys():
                        if key in formula:
                            formula = formula.replace(key, dic_formula[key])
                    F = sympy.sympify(formula)
                    print(f"\033[37mlim(\033[33m{F}\033[37m,{m}->{n},{sym})\033[32m" + ">>\033[33m",
                          sympy.limit(formula, m, n), Color, sep="")
                except:
                    print("|>>Error,try again.(input'e'to exit)")

    elif command == 'diff':
        print(f"\033[1A\033[30C\033[32m[使用指令'dic_f'查看快捷替换内容;使用'E'表示自然常数;使用'pi'表示圆周率常数;使用指令'help'查看更多;]{Color}")
        formula = "A"
        x, y, z = sympy.symbols("x y z")
        sym = ''
        v = x
        n_ = 1
        while True:
            brand = f"\033[37mdiff(f(x),{v},{n_})\033[32m"
            formula = input(f"{brand}<<")
            if not re.search(r'\S', formula):
                pass
            elif formula == 'exit' or formula == 'exit()' or formula == 'e' or formula == 'E':
                break
            elif formula == 'integrate' or formula == 'int' or formula == 'inte' or formula == 'i':
                auto_mode = 1
                msg = 'integrate'
                break
            elif formula == 'lim' or formula == 'L' or formula == 'li' or formula == 'l':
                auto_mode = 1
                msg = 'lim'
                break
            elif re.search(r'v\[(?P<V>\w+)\]', formula):
                v = re.search(r'v\[(?P<V>\w+)\]', formula).group("V")
                v = sympy.sympify(v)
            elif re.search(r'n\[(?P<N_>\d+)\]', formula):
                n_ = re.search(r'n\[(?P<N_>\d+)\]', formula).group("N_")
                try:
                    n_ = int(n_)
                except:
                    print("Error(n_),try again.")
                    n_ = 1
            elif formula == 'help':
                print("""
                Func:diff(F,v,n_);
                Command:'v[...]':变量(默认x);  
                        'n[...]':求导等级(默认1);
                        'exit'/'e':退出;""")
            elif formula == 'dic_formula' or formula == 'dic_f':
                print(dic_formula)
            else:
                try:
                    for key in dic_formula.keys():
                        if key in formula:
                            formula = formula.replace(key, dic_formula[key])
                    F = sympy.sympify(formula)
                    print(f"\033[37mdiff(\033[33m{F}\033[37m,{v},{n_})\033[32m" + ">>\033[33m",
                          sympy.diff(formula, v, n_), Color, sep="")
                except:
                    print("|>>Error,try again.(input'e'to exit)")


    elif command == 'integrate' or command == 'inte':
        print(f"\033[1A\033[30C\033[32m[使用指令'dic_f'查看快捷替换内容;使用'E'表示自然常数;使用'pi'表示圆周率常数;使用指令'help'查看更多;]{Color}")
        formula = "A"
        x, y, z = sympy.symbols("x y z")
        sym = ''
        v = x
        domainX, domainY = 0, 1
        while True:
            brand = f"\033[37minte(f(x),{v},{domainX},{domainY})\033[32m"
            formula = input(f"{brand}<<")
            if not re.search(r'\S', formula):
                pass
            elif formula == 'exit' or formula == 'exit()' or formula == 'e' or formula == 'E':
                break
            elif formula == 'diff' or formula == 'd' or formula == 'D':
                auto_mode = 1
                msg = 'diff'
                break
            elif formula == 'lim' or formula == 'L' or formula == 'li' or formula == 'l':
                auto_mode = 1
                msg = 'lim'
                break
            elif re.search(r'v\[(?P<V>[\w/]+)\]', formula):
                v = re.search(r'v\[(?P<V>[\w/]+)\]', formula).group("V")
                v = sympy.sympify(v)
            elif re.search(r'l\[(?P<L>-?[\w/]+)\]', formula):
                domainX = re.search(r'l\[(?P<L>-?[\w/]+)\]', formula).group("L")
            elif re.search(r'r\[(?P<R>-?[\w/]+)\]', formula):
                domainY = re.search(r'r\[(?P<R>-?[\w/]+)\]', formula).group("R")
            elif re.match(r'(?P<L>-?[\w/]+)\s(?P<R>[\w/]+$)', formula):
                domainX = re.match(r'(?P<L>-?[\w/]+)\s(?P<R>-?[\w/]+$)', formula).group('L')
                domainY = re.match(r'(?P<L>-?[\w/]+)\s(?P<R>-?[\w/]+$)', formula).group('R')
            elif formula == 'help':
                print("""
                Func:integrate(F,(v,l,r));
                Command:'v[...]':变量(默认为x);
                        'l[...]':求积分范围左值;   
                        'r[...]':求积分范围右值;
                        '... ...':求积分范围左值 求积分范围右值;
                        'exit'/'e':返回;""")
            elif formula == 'dic_formula' or formula == 'dic_f':
                print(dic_formula)
            else:
                try:
                    for key in dic_formula.keys():
                        if key in formula:
                            formula = formula.replace(key, dic_formula[key])
                    F = sympy.sympify(formula)
                    domain = sympy.sympify(f"({v},{domainX},{domainY})")
                    print(f"\033[37minte(\033[33m{F}\033[37m,{domainX},{domainY})\033[32m" + ">>\033[33m",
                          sympy.integrate(formula, domain), Color, sep="")
                except:
                    print("|>>Error,try again.(input'e'to exit)")

#--------------------------------------------------------------END
    elif True in [command.startswith(i) for i in SystemCommands]:
        os.system(command)
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
                    error("未启用")
            case "power":
                if usePsutil:
                    try:
                        battery = psutil.sensors_battery()
                        print(f"{battery.percent}% Plugged:{battery.power_plugged}")
                    except Exception as E:
                        error(E)
                else:
                    error("未启用")
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
                    error(E)
            case "vim":
                os.system(f"{path}/vim82/vim.exe")
            case "code":
                os.system(f"{path}/vim82/vim.exe {__file__}")
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
                if sysMode == "Windows":
                    os.system(f"{path}/glow/glow.exe {path}/README.md")
                else:
                    os.system(f"python {path}/mdv/markdownviewer.py {path}/README.md")
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
                        error(E)
            case "restart":
                if sysMode == "Windows":
                    os.system("cls")
                elif sysMode == "Linux":
                    os.system("clear")
                os.system(f"python {path}/B4mShell.py")
                sys.exit(0)
            case "rs":
                if sysMode == "Windows":
                    os.system("cls")
                elif sysMode == "Linux":
                    os.system("clear")
                os.system(f"python {path}/B4mShell.py")
                sys.exit(0)
            case "var":
                var = ""
                if os.path.exists(f"{path}/config/var"):
                    os.remove(f"{path}/config/var")
            case "server":
                os.system("python -m http.server 9999")
            case "start server":
                os.system("start python -m http.server 9999")
            case "myip":
                try:
                    print(requests.get(UrlConfig["myip"]).text)
                except Exception as E:
                    error(E)
            case "getip":
                try:
                    print(requests.get(UrlConfig["getip"]).text)
                except Exception as E:
                    error(E)
            case "headers":
                cmd = ""
                while True:
                    cmd = input("$Headers >")
                    if cmd.count(": ") == 1:
                        key,value = cmd.split(': ')
                        value = re.sub(r"^\s*", "", value).replace("'", "\\'")
                        key = re.sub(r"^\s*", "", key).replace("'", "\\'")
                        if len(value) > 0 and len(key) > 0:
                            headers[key] = value
                        else:
                            break
                    else:
                        break
            case "interip":
                try:
                    print(get_internal_ip())
                except Exception as E:
                    error(E)
            case "hostname":
                print(socket.gethostname())
            case "host":
                print(socket.gethostbyname(socket.gethostname()))
            case "last":
                print("-->"+last)
                procCMD(last)
            case "l":
                print("-->"+last)
                procCMD(last)
            case "echo":
                echo = ""
                line = "" 
                while True:
                    line = input("echo />")
                    if line != "exit" and line != "quit" and not "{exit}" in line and not "{e}" in line:
                        echo +=(line + "\n")
                        # print(line,line != "exit" and line != "quit" and not "{exit}" in line and not "{e}" in line)
                    else:
                        break
                print(echo)
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
        # raise TypeError("输入非字符串！")
        error("输入内容非字符串")
        return False
    for num in data:
        if num not in ["0", "1"]:
            error("输入内容非二进制字符串")
            return False
        #     raise ValueError("输入非二进制字符串！")

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
        error("输入内容非正整数")
        return False
        # raise TypeError("输入非正整数！")
    bcd = 0
    for index, char in enumerate(str(dec)[::-1]):
        bcd += int(char) * 16**index
    # 转化为二进制字符串，高位补0
    pattern = f"{bcd:0{lenth}b}"
    if len(pattern) > lenth:
        # raise OverflowError("输入十进制数过大，超过BCD码指定长度")
        error("输入十进制数过大，超过BCD码指定长度")
    return "".join(code for code in pattern)

	
def baidu(st0):
    url = "https://fanyi.baidu.com/sug"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    data_0 = {"kw": st0}
    try:
        res1 = requests.post(url=url, headers=headers, data=data_0, timeout=5)
    except Exception as E:
        error(f"{E}*")
        return False
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
        errot(E)
        return False
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
    print("", end=f"\033[43m\033[35m0{BgColor}{Color} ")
    for i in os.listdir(Path):
        index = os.listdir(Path).index(i)
        UserVars[str(index)] = i
        if i == file:
            color = '\033[35m'
        elif os.path.isdir(os.path.join(path, i)):
            color = '\033[37m'  
        else:
            color = '\033[36m'
        if index == len(os.listdir(Path))-1:
            print(f"{color}{i}{Color}", end=f"{Color} ")    
        else:
            print(f"{color}{i}{Color}", end=f" \033[43m\033[35m{index+1}{BgColor}{Color} ")
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
        error(E)
        return False

Chat = MFZN

def CookieTrans(msg):
    cookies = {}
    for line in msg.split(';'):
        key,value = line.split('=',1)
        value = re.sub(r"^\s*", "", value).replace("'", "\\'")
        key = re.sub(r"^\s*", "", key).replace("'", "\\'")
        cookies[key] = value
    return cookies
def DataTrans(msg):
    data = {}
    for line in msg.split('&'):
        key,value = line.split('=',1)
        value = re.sub(r"^\s*", "", value).replace("'", "\\'")
        key = re.sub(r"^\s*", "", key).replace("'", "\\'")
        data[key] = value
    return data


def ComandReplace(command):
    currentGlobals = globals()
    for key, value in currentGlobals.items():
        if "{"+key+"}" in command:
            command = command.replace("{"+key+"}", str(value))
    for key, value in UserVars.items():
        if "{"+key+"}" in command:
            command = command.replace("{"+key+"}", str(value))
    return command

def get_internal_ip():
    # 获取所有网络接口
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        # 排除回环接口和虚拟接口
        if interface == 'lo' or 'virtual' in interface:
            continue
        # 获取接口的IP地址
        addresses = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addresses:
            for address in addresses[netifaces.AF_INET]:
                internal_ip = address['addr']
                return internal_ip
    return None
def custom_sort(x):
    if re.search(r'\d+', x):
        number = int(re.search(r'\d+', x).group())
    else:
        print(f"custom_sort:未找到参数:{x}中的数字;")
        number = 0
    return number
def procCMD(command, mode=0):
    if command.startswith("#"):
        return False
    command = ComandReplace(command)
    Fix_01 = re.search(r"\[\*\d+$", command)
    if Fix_01:
        Fix_01 = Fix_01.group()
        command = command.replace(Fix_01, "")
        try:
            num = int(Fix_01[2:])
            for i in range(num):
                MyShell(command, mode)
        except Exception as E:
            error(E)
    elif MyShell(command, mode):
        pass
    else:
        try:
            exec(f"{command}")
        except:
            pass
def convert_svg_to_png(svg_path, png_path=f"{path}/target"):  
    image = Image.open(svg_path)  
    image.save(png_path, 'png')


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
    Path = os.getcwd() 
    if len(sys.argv) == 1:
        print(f"{Color}Welcom to B4mShell by 南竹！(https://github.com/B4m600/B4mShell)", end=Cyan)
        if sysMode == "Windows":
            os.system("Color 9")
            print(Banner_2)
        elif sysMode == "Linux":
            print(Banner_1)
        else:
            error("系统模式配置异常,已改用Linux系统模式")
            with open("target\\sysMode", "w")as f:
                f.write("Linux")
            sysMode = "Linux"
        #print("\"" + random.choice(welcom) + "\"")
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
            procCMD(command)
            if not command == "last" and not command == "l" and re.search(r"\S",command):
                last = command
    else:
        for argv in sys.argv[1:]:
            if argv.endswith(".b4m"):
                if os.path.exists(argv):
                    for command in open(argv, encoding="u8"):
                        procCMD(command.replace("\n", ""), mode=1)
            else:
                warning(f"参数:{argv}未识别")



