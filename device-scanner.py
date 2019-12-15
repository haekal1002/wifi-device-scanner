import subprocess
import threading
from getmac import get_mac_address

ip_ad = []

def net_scan(i):
    try:
        ip = '192.168.1.'+str(i)
        command = 'ping -c 1 '+ip
        data = subprocess.check_output(command.split()).decode().split('\n')
        
        for line in data:
            #print(line)
            if '0% packet loss' in line: 
                #print('[+] {} is active'.format(ip+str(i)))
                ip_ad.append(ip)
 
    except Exception as error:
        #print(error)
        #print('[-] Trouble with {}'.format(ip+str(i)))
        pass

for i in range(1, 255):
    try:
        t = threading.Thread(target=net_scan, args=(i, ))
        t.start()
    except Exception as error:
        print('[-] {}'.format(error))


for i in range(0, len(ip_ad)):
    mac = get_mac_address(ip=ip_ad[i])
    if mac != None:
        print('[+] IP: {} \t MAC Address: {}'.format(ip_ad[i], mac))

