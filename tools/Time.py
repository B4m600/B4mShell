import threading, time, os
os.system("color a")
os.system('mode con: cols=17 lines=3')
def Main():
    while True:
        TS = int(time.time() * 1000)
        print(f'\033[2;3H{TS}')
        time.sleep(0.1)
    T_Main = threading.Thread(target=Main)
    T_Main.start()
Main()