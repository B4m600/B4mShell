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
            erorr("读取sysMode失败")
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
try:
    from tools import netifaces
except Exception as E:
    error(E)
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
                  "cleanmgr", "snippingtool", "magnify", "git", "nano", "chmod", "curl", "curl",
                  "telnet", "ssh", 
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
UserVars = {"{this}": "B4mShell.py"}
UrlConfig = {
    "pip": "https://pypi.tuna.tsinghua.edu.cn/simple",
    "git": "https://ghproxy.com",
    "getip": "http://ifconfig.me/ip",
    "myip": "https://myip.ipip.net",
}
data = {}
cookies = {}
headers = {}

if os.path.exists("config/var"):
    with open("config/var", "r", encoding="u8")as f:
        var = f.read()
def MyShell(command):
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
    elif command.startswith("echo:") or command.startswith("echo "):
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
    elif command.startswith("cd "):
        cmd = command[3:]
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
            if os.path.isdir(cmd):
                shutil.rmtree(cmd)
                dir()
            else:
                error(f"路径异常:{cmd}")
        except Exception as E:
            error(E)
    elif command.startswith("sqlmap"):
        cmd = command[6:]
        os.system(f"python {path}/sqlmap/sqlmap.py{cmd}")
    elif True in [command.startswith(i) for i in SystemCommands]:
        os.system(command)
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
        error(E)
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

def error(msg):
    print(f"\033[31mError({msg});{Color}")
def warning(msg):
    print(f"\033[33mWarning({msg});{Color}")

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
        error("系统模式配置异常,已改用Linux系统模式")
        with open("target\\sysMode", "w")as f:
            f.write("Linux")
        sysMode = "Linux"
    print("\"" + random.choice([
    "你想堕落没人拦你，但是你想出人头地？那拦你的人就多了。",
    "正因为你有能力跨越，这个考验才会降临。",
    "登高望远，不是为了让整个世界看见，而是为了看见整个世界。",
    "惟沉默是最高的轻蔑。",
    "任何消耗自己的人和事，多看一眼都是你的不对。",
    "如果社会可以培训你，则也可以培训别人替代你。",
    "自律不是束缚自己，而是保证自己不被束缚。",
    "永远没有正确的选择，而要让选择变得正确。",
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
        command = ComandReplace(command)
        Fix = command[-2:]
        if Fix.startswith("*"):
            try:
                num = int(Fix[1:])
                for i in range(num):
                    MyShell(command[:-2])
            except Exception as E:
                error(E)
        elif MyShell(command):
            pass
        else:
            try:
                exec(f"print({command})")
            except:
                pass
