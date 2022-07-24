#!/usr/bin/env python3

import socket, threading,sys,ipaddress,datetime

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        
def TCP_connect(ip, port, delay):
    #print(ip)
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    r=TCPsock.connect_ex((ip, port))
    if r==0:
        print(ip+':'+str(port))



def scan_ports(iplist, delay,port):
    
    for ips in iplist:
        threads = []        
    
        for ip in ips:
            t = threading.Thread(target=TCP_connect, args=(ip, port, delay))
            threads.append(t)
    
        
        for i in range(len(ips)):
            threads[i].start()
    
        
        for i in range(len(ips)):
            try:
                threads[i].join()
            except KeyboardInterrupt:
                print()
                quit('CTRL+C signal')



def main():
    netip=sys.argv[1]
    port = int(sys.argv[2])
    nthread = int(sys.argv[3])
    
    ips = [str(ip) for ip in ipaddress.IPv4Network(netip)]
    print('number of targets: '+str(len(ips)))
    
    iplist = list(chunks(ips,nthread))
    
    delay = 2   
    scan_ports(iplist, delay,port)


t1 = datetime.datetime.now().replace(microsecond=0)
main()
t2= datetime.datetime.now().replace(microsecond=0)

tl=str(t2-t1).split(':')
print("time elapsed: ",end='')
if tl[0] == '0' and tl[1]=='00':
    print(tl[2]+'s')
elif tl[0] != '0':
        print(tl[0]+'h'+ tl[1]+'m'+tl[2]+'s' )

elif tl[1] != '00':
        print(tl[1]+'m'+tl[2]+'s')

    