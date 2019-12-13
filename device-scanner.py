import socket
from threading import Thread

ip = '192.168.1.'

def main(i):
    data = socket.gethostbyaddr(ip+str(i))
    if data[0] != data[2][0]:
        print("[+] %s \t\t %s" % (data[0], data[2][0]))

for i in range(1, 256):
    try:
        t = Thread(target=main, args=(i, ))
        t.start()
    except:
        pass
