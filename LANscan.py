import os, subprocess, re, socket
from colorama import  init, Fore

devices = {}
def main(): 
    init(convert=True)
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True) 
    # FIX: Send a single ping to the local machine to populate the ARP cache
    subprocess.Popen('ping %s -n 1' % socket.gethostbyname(socket.gethostname()), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    process = subprocess.Popen('arp -a', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = (process.stdout.read() + process.stderr.read()).decode()
    output_split = output.split('\n')
    d_num = 0
    
    for line in output_split:
        line = line.strip()
        regex = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\s+.{3}-.{3}', line)

        if regex:
            d_num += 1
            d_addr = re.search(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', line).group(0)
            d_mac = re.search(r'(.{2}-.{2}-.{2}-.{2}-.{2}-.{2})', line).group(0).replace('-', ':').upper()
            devices.update({d_addr:{'num': d_num, 'address': d_addr, 'mac': d_mac}})
    
    print('ID         IPv4 address           MAC address')
    print('---        ---------------        -----------------')
    
    for device in devices.values():
        d_num = device['num']
        d_addr = device['address']
        d_mac = device['mac']

        #FIX: Add spaces to align the output
        id_spaces = ' ' * (11 - len(str(d_num)))
        address_spaces = ' ' * (23 - len(d_addr))
        mac_spaces = ' ' * (25 - len(d_mac))
    
        print(f'{Fore.RED}{d_num}{id_spaces}{Fore.WHITE}{d_addr}{address_spaces}{Fore.GREEN}{d_mac}{mac_spaces}')
    
if __name__ == '__main__':
    main(), print()
