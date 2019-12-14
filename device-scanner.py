import subprocess 

command = 'nmap -sP 192.168.1.0/24'
data = subprocess.check_output(command.split()).split('\n')

# 2-dimensional lists contaning host:ip
profiles = [a.split('for')[1][1:-1].split() for a in data if 'Nmap scan report' in a]

# a list containing MAC Addresses
#mac_address = [b.split()[2] for b in data if 'MAC Address' in b]

for host, ip in profiles:
    print('[+] Host: {0:<25} IP: {1}'.format(host, ip[1:]))
