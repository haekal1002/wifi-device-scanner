import subprocess
import threading

def net_scan(i):
    try:
        ip = '192.168.1.'
        command = 'ping -c 1 '+ip+str(i)
        data = subprocess.check_output(command.split()).decode().split('\n')
        
        for line in data:
            #print(line)
            if '0% packet loss' in line: 
                print('[+] {} is active'.format(ip+str(i)))
    
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

