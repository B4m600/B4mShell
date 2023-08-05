import threading, time, os, psutil
os.system("color a")
os.system('mode con: cols=22 lines=3')
def Main():
    while True:
        disk = psutil.disk_usage('./')
        res = disk.free / 1E9
        print(f'\033[2;3H[{format(res, "^10.10f")} GB]')
        time.sleep(0.1)
    T_Main = threading.Thread(target=Main)
    T_Main.start()
Main()