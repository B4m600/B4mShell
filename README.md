### [:指令]

#### [调试]

- print:

  - 输出指定的全局变量内容，调试用。

  - `print:path` -> 输出当前路径。

- exec:

  - 执行一个指定的python语句。
  - `exec:print("Hello, World。")`

#### [编码]

- md5:
  - 将输入内容转换为MD5加密内容。
- b64:
  - 将输入内容转换为Base64加密内容。
- b64d:
  - 输入Base64密文后返回解密内容。
- url:
  - 将输入内容转换为URL编码。
- urld:
  - 输入URL编码后返回解码内容。
- hex:
  - 输入十进制数字后返回十六进制内容。
- bin:
  - 输入十进制数字后返回二进制内容。
- echo:
  - 将输入内容中包含的&#int;代码转换为对应符号后返回原文。
- utf8:
  - 返回输入内容的UTF-8编码内容。
- gbk:
  - 返回输入内容的GBK编码内容。
- unic:
  - 返回输入内容的Unicode编码内容。
- CN:
  - 返回输入内容中的中文内容。
- bcd:
  - 返回输入十进制数字的bcd编码。
- bcdd:
  - 返回输入二进制数字的bcd解码。
- len:
  - 返回输入内容的字符数量。
- comp:
  - 返回输入十进制数字的补码。

#### [功能]

- m4a:

  - 调用`https://github.com/FFmpeg/FFmpeg`中的FFmpeg工具进行相关操作。

  - 将当前文件夹内的M4A格式的音频文件转换为MP3格式。
  - `m4a:Test`
    - 将当前文件夹内名为"Test.m4a"的文件转换为"Test.mp4"到当前文件夹内。

- cd:

  - 转移路径。
  - `cd:tools` or `cd tool`

- C: || D:

  - 直接输入以C:或者D:开头的绝对路径，快捷转移至此路径。
  - `C:\Users\LEGION`

- trans:

  - 输入一段中文或者英文，返回翻译内容。

- vim:

  - 调用`https://github.com/vim/vim`中的vim工具进行相关操作。

  - 输入文本文件名，使用vim在新窗口中打开。
  - `vim:new.txt`

- hx:

  - 调用`https://github.com/helix-editor/helix`中的helix工具进行相关操作。

  - 输入文本文件名，使用helix在新窗口中打开。

- http: || https:

  - 直接输入以http:或者https:开头的网址后进行Get请求，返回的网页源码自动保存到Get.html中并使用vim打开。

### [空格指令]

#### [功能]

- cd

  - 效果等同于"cd:"指令。

  - `cd tools`

- vim

  - 输入文本文件名，使用vim在当前窗口内打开。
  - `vim new.txt`

- hx

  - 输入文本文件名，使用helix在当前窗口内打开。
  - `hx new.txt`

- get

  - 输入一段链接进行Get请求，返回的网页源码自动保存到Get.html中并使用vim打开。

- sqlmap

  - 调用`https://github.com/sqlmapproject/sqlmap`中的sqlmap工具进行相关操作。

- var

  - 输入一段文本后记录在全局变量var中并显示在提示行末尾。
  - `var https://www.baidu.com`

#### [系统]

- rm
  - 调用CMD中的del指令。
- md
  - 调用CMD中的md指令。
- rd
  - 调用CMD中的rd指令。

### [单指令]

#### [调试]

- test
- file
- path
  - sys.executable
- qq
- abspath
  - os.path.abspath(".")
- realpath
  - os.path.realpath(".")
- green || cyan || red || purple || white || blue || yellow
- code
  - 使用vim在当前窗口打开源码文件:B4mShell.py
- Disk
  - 打开一个小窗口用来监控当前硬盘的剩余内存。
- Time
  - 打开一个小窗口用来实时输出时间戳。
- v
  - 打开一个用于快速调控音量的弹窗。

#### [功能]

- help
  - 使用vim打开README.md文件。
- exit
- 等同指令"e"
  
- 退出程序。
- home

  - 若使用cd指令改变了当前路径，则可以使用该指令还原至初始路径。
- ~

  - 若使用cd指令改变了当前路径，则可以使用该指令还原至初始路径。
- date

  - datetime.date.today()
- timestamp

  - time.time()
- time

  - datetime.datetime.now().strftime("%H:%M:%S")
- dir

  - 查看当前文件夹中的内容，横向展开。
- ls

  - 查看当前文件夹中的内容，纵向展开。
- vim

  - 直接运行vim。

#### [系统]

- sdh

  - shutdown /h

- sda

  - shutdown /a

- sds

  - shutdown /s /t 0

- sdr

  - shutdown /r /t 0

- ./

  - 使用资源管理器打开当前路径。

- .

  - 等同指令"。"

  - 使用资源管理器打开原始路径。

- cls

  - cls

- lock

  - rundll32.exe user32.dll LockWorkStation

- goodnight

- task

  - taskmgr

- temp

  - explorer %temp%

- local

  - explorer %localappdata%

- hosts

  - explorer C:\Windows\System32\drivers\etc

#### [计算]

- distance
  - 输入四个浮点数计算对应两个二维坐标的距离。

#### [效果]

- face
  - 展示一个表情。
- Firework
  - 展示全屏烟花特效，按Esc键退出。
- Rain
  - 展示全屏数字雨特效，按Esc键退出。

### [语法]

- *
  - 执行指令后缀添加`*1`至`*9`时将执行1至9遍该指令。
  - `print:path*9`