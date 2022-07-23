#!/usr/bin/env python3

import socket, threading,sys,ipaddress


def TCP_connect(ip, port, delay):
    #print(ip)
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    r=TCPsock.connect_ex((ip, port))
    if r==0:
        print(ip+':'+str(port))



def scan_ports(ips, delay,port):

    threads = []        

    for ip in ips:
        t = threading.Thread(target=TCP_connect, args=(ip, port, delay))
        threads.append(t)

    
    for i in range(len(ips)):
        threads[i].start()

    
    for i in range(len(ips)):
        threads[i].join()



def main():
    netip=sys.argv[1]
    port = int(sys.argv[2])
    ips = [str(ip) for ip in ipaddress.IPv4Network(netip)]
    delay = 2   
    scan_ports(ips, delay,port)

if __name__ == "__main__":
    main()