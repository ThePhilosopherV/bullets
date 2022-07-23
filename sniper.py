#!/usr/bin/env python3

import socket
import ipaddress
import sys
import datetime

netip=sys.argv[1]
port=int(sys.argv[2])
ips = [str(ip) for ip in ipaddress.IPv4Network(netip)]




def check(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    result = sock.connect_ex((ip,port))
    if result == 0:        
        print(ip+':'+str(port))
    sock.close()
    


a = datetime.datetime.now().replace(microsecond=0)
for ip in ips:
        check(ip,port)

b = datetime.datetime.now().replace(microsecond=0)

print(b-a)

