### [系统指令]

- help

  - 在Windows模式下使用glow打开README.md文件。
  - 在Linux模式下使用mdv打开README.md文件。
  
- rm

  - `rm tmp.txt`

  - 删除指定的文件或者空文件夹。
  
- md

  - `md test`
  - 创建指定的文件夹。
  
- cd

  - `cd tools`
  - 改变当前路径。
  
- rd

  - `rd test`

  - 删除指定的文件夹。
  
- getcwd

  - `getcwd`

  - 查看当前工作路径。
  
- dir

  - 查看当前文件夹中的内容，横向展开。
  - 每个文件名称前会生成序号，在之后输入指令中包含`{序号}`则会快捷替换为该序号对应的文件名。
  
  ```
  $ >dir
  0 .git 1 B4mShell.cmd 2 B4mShell.py 3 B4mShell.sh 4 bs 5 config 6 execjs 7 ffmpeg 8 helix 9 LICENSE 10 nmap 11 N_m3u8DL 12 README.md 13 requests 14 sqlmap 15 target 16 tools 17 vim82
  $ >echo {13}
  requests
  ```
  
- ls

  - 查看当前文件夹中的内容，纵向展开。
  
- exit

  - 等同指令`e`

  - 退出程序。
  
- home

  - 等同指令 `~`
  
  - 若使用cd指令改变了当前路径，则可以使用该指令还原至初始路径。
  
- restart
  - 等同指令 `rs`
  - 重启或刷新程序。

### [配置指令]

- username
  - `username B4m600`
  - 修改当前用户名。
  - 可使用`whoami`指令查看当前用户名。
- reset
  - `reset`
  - 清空缓存文件与配置文件。

### [功能指令]

- vim

  - 调用`https://github.com/vim/vim`中的vim工具进行相关操作。
  - 输入文本文件名，使用vim在当前窗口内打开。
  - `vim new.txt`
- hx

  - 调用`https://github.com/helix-editor/helix`中的helix工具进行相关操作。
  - 输入文本文件名，使用helix在当前窗口内打开。
  - `hx new.txt`
- get

  - 输入一段链接进行Get请求，返回的网页源码自动保存到Get.html中并使用vim打开。
  - 使用-headers参数添加请求头，使用`headers`单指令设置请求头内容。`get -headers https://www.baidu.com`
  - 使用-cookies参数添加cookies，使用`cookies:A=B; C=D; `指令设置cookies。`get -cookies https://www.baidu.com`
  - 使用-data参数添加data，使用`data:A=B&C=D`指令设置data。`get -data -headers -cookies https://www.baidu.com`
- post
  - 同get指令。
- m4a
  - 调用`https://github.com/FFmpeg/FFmpeg`中的FFmpeg工具进行相关操作。
  - 将指定路径的m4a格式的音频文件转换为MP3格式。
  - `m4a:Test.m4a`
    - 将当前文件夹内名为"Test.m4a"的文件转换为"Test.mp4"到当前文件夹内。
- webp
  - 调用`https://github.com/FFmpeg/FFmpeg`中的FFmpeg工具进行相关操作。
  - 将指定路径的webp格式的图像文件转换为png格式。
  - `webp:Test.webp`
    - 将当前文件夹内名为"Test.webp"的文件转换为"Test.png"到当前文件夹内。
- trans
  - 输入一段中文或者英文，返回翻译内容。[依赖接口]
- sqlmap

  - 调用`https://github.com/sqlmapproject/sqlmap`中的sqlmap工具进行相关操作。
- nmap
  - 调用`https://nmap.org`中的nmap工具进行相关操作。
- var

  - 输入一段文本后记录在全局变量var中并显示在提示行末尾。
  - `var https://www.baidu.com`
- mpv
  - 调用`https://github.com/mpv-player/mpv`中的mpv工具进行相关操作。
  - 输入媒体文件名称后即可播放该媒体文件。
  - `mpv Demo.mp3`
  - `mpv Test.mp4`
- read
  - 调用`https://github.com/mpv-player/mpv`中的mpv工具进行相关操作。
  - 输入文本后即可读出该文本。
  - 输入MP3文件后即可播放该音频。
  - `read 阿巴阿巴  `
- N
  - 调用`https://github.com/nilaoda/N_m3u8DL-CLI`中的N_m3u8DL工具进行相关操作。
  - 用于下载并转换m3u8文件。
  - `cd D:/Movie`
  - `N url --saveName "Demo"`
- busybox
  - 调用`http://frippery.org/files/busybox`中的busybox工具进行相关操作。
  - 使用`busybox --help`查看包含的指令。
  - `busybox ls`
  - 带参数且与已知指令不冲突的指令可直接调用，无需busybox指令前缀。
  - `cat demo.txt`
- hydra
  - 调用`https://github.com/maaaaz/thc-hydra-windows`中的hydra工具进行相关操作。
  - 用于爆破密码。
- mdv
  - 调用`https://github.com/axiros/terminal_markdown_viewer`中的mdv工具进行相关操作。
  - 用于查看Markdown文件。
- glow
  - 调用`https://github.com/charmbracelet/glow`中的glow工具进行相关操作。
  - 用于查看Markdown文件。
- b4m
  - 等同指令`run`
  - 运行一个由B4mShell支持的b4m格式的文件。
  - `run demo.b4m`
  - `b4m demo`
- host
  - 指定一个主机名，获取其IP。
  - `host www.baidu.com`
  - `host {hostname}`
- hostname
  - 指定一个IP地址，获取其主机名。
  - `hostname {host}`
- cupp
  - 调用`https://github.com/Mebus/cupp`中的cupp工具进行相关操作。
  - 用于根据参数生成密码字典。

### [:指令]

#### [调试]

- print:

  - 输出指定的全局变量内容，调试用。

  - `print:path` -> 输出当前路径。

- exec:

  - 执行一个指定的python语句。
  - `exec:print("Hello, World。")`

#### [编码|加解密]

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
  - 将输入内容中包含类似`&#2960;`格式的符号代码转换为对应的符号后返回原文。
  - 可配合{var}语法输出全局变量内容。`echo CurrentPath:{path}`
- utf8:
  - 返回输入内容的UTF-8编码内容。
- gbk:
  - 返回输入内容的GBK编码内容。
- unic:
  - 返回输入内容的Unicode编码内容。
- bcd:
  - 返回输入十进制数字的bcd编码。
- bcdd:
  - 返回输入二进制数字的bcd解码。
- comp:
  - 返回输入十进制数字的补码。

#### [文本处理]

- len:
  - 返回输入内容的字符数量。
- cookies:
  - 输入一段`a=2; b=3;`格式的字符串后输出转化为字典格式的内容。
  - 将指定内容存储到全局变量cookies，使用post指令时直接使用-cookies参数调用该变量。
- data:
  - 输入一段`a=2&b=3&c=4`格式的字符串后输出转化为字典格式的内容。
  - 将指定内容存储到全局变量data，使用post指令时直接使用-data参数调用该变量。
- cn:
  - 返回输入内容中的中文内容。

### [单指令]

#### [调试]

- file
  - 使用记事本打开源码文件。
- path
  - sys.executable
  - {path}
- abspath
  - os.path.abspath(".")
- realpath
  - os.path.realpath(".")
- code
  - 使用vim在当前窗口打开源码文件。
- Disk
  - 打开一个小窗口用来监控当前硬盘的剩余内存。
- Time
  - 打开一个小窗口用来实时输出时间戳。
- v
  - 打开一个用于快速调控音量的弹窗。

#### [功能]

- date

  - datetime.date.today()
  - {date}
- timestamp

  - time.time()
  - {timestamp}
- time

  - datetime.datetime.now().strftime("%H:%M:%S")
  - {time}
- headers
  - 进入headers输入模式，每行输入`A: B`格式的内容，输入格式之外的内容则自动退出当前模式。
  - 将指定内容存储到全局变量cookies，使用post指令时直接使用-cookies参数调用该变量。
- interip
  - 获取当前内网IP。
  - 依赖netifaces模块。
- getip
  - 获取当前公网IP。[依赖接口:http://ifconfig.me/ip]
- myip
  - 获取当前公网IP并查看相关信息。[依赖接口:https://myip.ipip.net]
- hostname
  - 获取当前设备hostname
  - {hostname}
- host
  - 获取当前设备的内网IP
  - {host}
- last
  - 等同指令`l`
  - 执行上一条不是`last`的指令。
- echo
  - 进入文本接收模式，在模式中输入的内容都会在结束后原文本输出。
  - 模式期间单独输入exit或者quit退出。
  - 模式期间输入内容包含{exit}或者{e}退出。

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

  - 等同指令`。`
  - 使用资源管理器打开原始路径。
- cls

  - cls [Windows]
  - clear [Linux]
- lock

  - rundll32.exe user32.dll LockWorkStation
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
- hi
  - 打招呼。
- goodnight
  - 晚安，玛卡巴卡。
- Firework
  - 展示全屏烟花特效，按Esc键退出。
- Rain
  - 展示全屏数字雨特效，按Esc键退出。

### [语法]

- [*后缀
  
  - 执行指令后缀添加`[*正整数`将执行指定次数该指令。
  - `print:path*9`
  
- {var}
  - 输入内容若包含"{var}"则将该内容替换为当前全局变量var中，默认为空。
  - 输入内容若包含"{某全局变量}"则将该内容替换为该全局变量的取值。
  - 全局变量var使用"var:"指令赋值，缓存，会覆盖上一次取值。
  - 自定义全局变量使用"var 变量名=变量取值"指令赋值，不缓存，会覆盖上一次取值。
  
  ```b4m
  var:www.vaidu.com
  ping {var}
  ```
  
  ```b4m
  var a=5
  echo {a}
  ```
  
  ```b4m
  var www.vaidu.com
  ping {var}
  ```
  
  ```b4m
  var a=b=1
  exec:print({a}+{b})
  ```
  
- 输入根路径自动cd

  - 直接输入以`C:` `D:` `E:` `F`开头的绝对路径，快捷转移至此路径。
  - `C:\Users\LEGION`

- 输入网址自动get

  - 直接输入以`http:`或者`https:`开头的网址后进行Get请求，请求到的源码自动保存到`target/Get.html`中并使用vim打开。
  - 若输入网址为媒体文件(通过文件后缀判定，判定范围可配置全局变量MediaExt)，则自动下载文件至target文件夹中。
  
- python指令补充

  - 输入与已知指令不冲突的python语句可直接执行。

### [busybox指令]

- 当前busybox指令总览。`busybox --help`

  ```
  ar, arch, ascii, ash, awk, base32, base64, basename, bash, bc, bunzip2, busybox, bzcat, bzip2, cal, cat,
  cdrop, chattr, chmod, cksum, clear, cmp, comm, cp, cpio, crc32, cut, date, dc, dd, df, diff, dirname, dos2unix,
  dpkg, dpkg-deb, drop, du, echo, ed, egrep, env, expand, expr, factor, false, fgrep, find, fold, free, fsync,
  ftpget, ftpput, getopt, grep, groups, gunzip, gzip, hd, head, hexdump, httpd, iconv, id, inotifyd, install,
  ipcalc, jn, kill, killall, less, link, ln, logname, ls, lsattr, lzcat, lzma, lzop, lzopcat, make, man, md5sum,
  mkdir, mktemp, mv, nc, nl, nproc, od, paste, patch, pdpmake, pdrop, pgrep, pidof, pipe_progress, pkill,
  printenv, printf, ps, pwd, readlink, realpath, reset, rev, rm, rmdir, rpm, rpm2cpio, sed, seq, sh, sha1sum,
  sha256sum, sha3sum, sha512sum, shred, shuf, sleep, sort, split, ssl_client, stat, strings, su, sum, sync, tac,
  tail, tar, tee, test, time, timeout, touch, tr, true, truncate, ts, tsort, ttysize, uname, uncompress,
  unexpand, uniq, unix2dos, unlink, unlzma, unlzop, unxz, unzip, uptime, usleep, uudecode, uuencode, vi, watch,
  wc, wget, which, whoami, whois, xargs, xxd, xz, xzcat, yes, zcat
  ```

- du

  - 查看指定路径或者当前路径的内存大小。
  - `du -sh`
  - `du --help`

  ```
          -a      Show file sizes too
          -b      Apparent size (including holes)
          -L      Follow all symlinks
          -H      Follow symlinks on command line
          -d N    Limit output to directories (and files with -a) of depth < N
          -c      Show grand total
          -l      Count sizes many times if hard linked
          -s      Display only a total for each argument
          -x      Skip directories on different filesystems
          -h      Sizes in human readable format (e.g., 1K 243M 2G)
          -m      Sizes in megabytes
          -k      Sizes in kilobytes (default)
  ```

- cat

  - 打印文本文件内容。
  - `cat test.txt` 

- less

  - 文本编辑器。

- vi

  - 文本编辑器。
