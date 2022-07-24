#!/usr/bin/env python3

import socket, threading,sys,ipaddress,datetime,os

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]



targets=[]
def TCP_connect(ip, port, delay):
    #print(ip)
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    r=TCPsock.connect_ex((ip, port))
    if r==0:
        print(ip+':'+str(port))
        targets.append(ip+':'+str(port))
        



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
help= """Usage:

./sniper <networkAddress/CIDR> <Port> <NumberOfThreads> [browser]

[browser] :browser name is optinal, aslo activates IPs browsing; make sure [browser] is callable from any directory.

Example: ./sniper.py 196.217.254.0/24 8080 200 firefox """
def main():
    if len(sys.argv)==1:
        print(help)
        quit()
    global webflag
    webflag=0
    netip=sys.argv[1]
    port = int(sys.argv[2])
    nthread = int(sys.argv[3])
    try:
        global webarg
        webarg = sys.argv[4]
        
        webflag=1
    except:
        pass
    
    ips = [str(ip) for ip in ipaddress.IPv4Network(netip)]
    print('number of targets: '+str(len(ips))+'\n')
    
    iplist = list(chunks(ips,nthread))
    
    delay = 3   
    scan_ports(iplist, delay,port)


t1 = datetime.datetime.now().replace(microsecond=0)
main()
t2= datetime.datetime.now().replace(microsecond=0)

tl=str(t2-t1).split(':')
print('\nNumber of positive targets: '+str(len(targets)))
print("time elapsed: ",end='')
if tl[0] == '0' and tl[1]=='00':
    print(tl[2]+'s')
elif tl[0] != '0':
        print(tl[0]+'h'+ tl[1]+'m'+tl[2]+'s' )

elif tl[1] != '00':
        print(tl[1]+'m'+tl[2]+'s')

num = len(targets)
if webflag and num:
    
    
    print('\n<<< browsing IPs >>>>')
    
    for ip in targets:
        cunts=int(input('How many IPs you want to browse ('+str(num)+' IP<s> left): '))
        for i in range(cunts):
            os.system(webarg+" "+ip)
        num -= cunts
            

