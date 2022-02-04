"""
Copyright (c) 2020-2021 Vladimir Rogozin (vladimir20040609@gmail.com)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

# Import.
import ipaddress
import argparse
import textwrap
import sys
import os

# Files.
from commands.ifconfig        import ifconfig
from commands.scan            import scanStatus, scan, scanWithPort, scanLocalDevices
from commands.ns              import ns, nsconv
from commands.ping            import ping
from commands.traceroute      import traceroute
from commands.banner          import bannerWithPort
from commands.reverseiplookup import reverseiplookup
from commands.censys          import censys
from commands.techdetect      import detectTech
from commands.honeypot        import honeypot
from commands.macaddress      import macaddresslookup
from commands.dnsmap          import dnsmap
from commands.subdomains      import subdomains


# Argument parser.
ap = argparse.ArgumentParser(description="RedNetwork Tool", formatter_class=argparse.RawDescriptionHelpFormatter,
epilog=textwrap.dedent('''
Examples:
        -ifconfig
        -scan -host 192.168.0.1 -prange 1 100
        -scanlocal
        -ns scanme.nmap.org
        -grab -host 127.0.0.1 -p 22
        -ping scanme.nmap.org
        -traceroute scanme.nmap.org
        -reverseip 8.8.8.8
        -censys 8.8.8.8
        -techdetect https://mail.ru
        -honeypot 164.128.164.7
        -macaddress 00:00:5e:00:53:af
        -dnsmap mail.ru
        -subdomains mail.ru
'''
))


# Arguments list.
ap.add_argument('-ifconfig', action = 'store_true', 
        help = 'display current network configuration')

ap.add_argument('-ping',
        nargs = 1,
        help = 'send ICMP packets to a host to check connectivity.')

ap.add_argument('-traceroute',
        nargs = 1,
        help = 'diagnose route paths and measure transit delays.')

ap.add_argument('-ns', type = str,
        nargs = '+',
        help = 'DNS check.')

ap.add_argument('-host', type = str,
        nargs = '+',
        help = 'specify one or more hosts to scan.')

ap.add_argument('-iprange', type = str,
        nargs = 2,
        help = 'specify IP range of hosts to scan.')

ap.add_argument('-p', type = int,
        nargs = '+',
        help = 'specify one or more ports to scan.')

ap.add_argument('-prange', type = int,
        default = [1-1000], 
        nargs = 2,
        help = 'specify port range to scan.')

ap.add_argument('-scan', action = 'store_true',
        help = 'perform comprehensive scan for open ports (root privileges needed).')

ap.add_argument('-scanlocal', action = 'store_true',
        help = 'perform scan to detect local devices.')

ap.add_argument('-scantcp', action = 'store_true',
        help = 'perform TCP scan for open ports.')

ap.add_argument('-scanack', action = 'store_true',
        help = 'perform ACK scan for open ports.')

ap.add_argument('-scansyn', action = 'store_true',
        help = 'perform SYN scan for open ports (root privileges needed).')

ap.add_argument('-scanudp', action = 'store_true',
        help = 'perform UDP scan for open ports (root privileges needed).')

ap.add_argument('-grab', action = 'store_true',
        help = 'perform banner grabbing.')

ap.add_argument('-reverseip', type = str,
        nargs = 1,
        help = 'perform reverse ip lookup.')

ap.add_argument('-censys', type = str,
        nargs = 1,
        help = 'censys feature.')

ap.add_argument('-techdetect', type = str,
        nargs = 1,
        help = 'perform technologies detection.')

ap.add_argument('-honeypot', type = str,
        nargs = 1,
        help = "perform honeypot probability checker.")

ap.add_argument('-macaddress', type = str,
        nargs = 1,
        help = "perform mac address lookup.")

ap.add_argument('-dnsmap', type = str,
        nargs = 1,
        help = "perform dns mapping feature.")

ap.add_argument('-subdomains', type = str,
        nargs = 1,
        help = "get subdomains")


# Let's parse user's input.
args = vars(ap.parse_args())

# Function to handle user's selection.
def handleScan(scantype):
    if args['host']:
        # Perform SYN scan with IP address(es) only
        if not args['p'] and not len(args['prange']) == 2: 
            for i in range(0, len(args['host'])):
                scan(nsconv(args['host'][i]), args['host'][i], 1, 1000, f'{scantype}')

        # Perform SYN scan with IP address(es) and port(s)        
        elif args['p'] and not len(args['prange']) == 2:
            for i in range(0, len(args['host'])):
                for j in range(0, len(args['p'])):
                    scanWithPort(nsconv(args['host'][i]), args['host'][i], args['p'][j], i, j, f'{scantype}')
        
        # Perform SYN scan with IP address(es) and port range
        elif len(args['prange']) == 2 and not args['p']:
            for i in range(0, len(args['host'])):
                scan(nsconv(args['host'][i]), args['host'][i], args['prange'][0], args['prange'][1], f'{scantype}')

        else:
            print('Please type the command correctly. Examples: \n \t -scan -host [HOST(s)] \n \t -scan -host [HOST(s)] -p [PORT(s)] \n \t -scan -host [HOST(s)] -prange [START PORT] [END PORT] \n \t -scan -iprange [START IP] [END IP] -p [PORT(S)] \n \t -scan -iprange [START IP] [END IP] -prange [START PORT] [END PORT]')

    else:
        print('Please specify the host(s) (or IP range) to scan and port(s) (or port range). Examples: \n \t -scan -host [HOST(s)] \n \t -scan -host [HOST(s)] -p [PORT(s)] \n \t -scan -host [HOST(s)] -prange [START PORT] [END PORT] \n \t -scan -iprange [START IP] [END IP] -p [PORT(S)] \n \t -scan -iprange [START IP] [END IP] -prange [START PORT] [END PORT]') 


# Check host IP configuration
if args['ifconfig']:
    ifconfig()

# DNS check (check IP address of a website)
elif args['ns']:
    for i in range(0, len(args['ns'])):
        ns(args['ns'][i])

# Ping to check connectivity
elif args['ping']:
    ping(args['ping'][0])

# Traceroue
elif args['traceroute']:
    traceroute(args['traceroute'][0])

# TCP scan
elif args['scantcp']:
    handleScan('-sT')

# ACK scan
elif args['scanack']:
    handleScan('-sA')

# UDP scan
elif args['scanudp']:
    handleScan('-sU')

# SYN scan
elif args['scansyn']:
    handleScan('-sS')
                                
# Comprehensive scan
elif args['scan']:
    handleScan('-sS -sV -sC -A -O')

# Scan for local devices
elif args['scanlocal']:
    scanLocalDevices()

# Banner grabbing
elif args['grab']:    
    if args['host']: 
        # Perform grabbing with IP address(es) and port number(s)
        if args['p'] and not len(args['prange']) == 2: 
            for i in range(0, len(args['host'])):
                for j in range(0, len(args['p'])):
                    bannerWithPort(nsconv(args['host'][i]), args['p'][j])               

        # Perform grabbing with IP address(es) and port range 
        elif len(args['prange']) == 2 and not args['p']: 
            for i in range(0, len(args['host'])):
                for j in range(args['prange'][0], args['prange'][1] + 1):
                    bannerWithPort(nsconv(args['host'][i]), j)
        else:
            print('Please type the command correctly. Examples: \n \t -grab -host [HOST(s)] -p [PORT(s)] \n \t -grab -iprange [START IP] [END IP] -prange [START PORT] [END PORT] \n \t -grab -host [HOST(s)] -prange [START PORT] [END PORT] \n \t -grab -iprange [START IP] [END IP] -p [PORT]')

    elif args['iprange']:
        # Perform grabbing with IP range and port number(s)
        if args['p'] and not len(args['prange']) == 2: 
            for ip_int in range(int(ipaddress.IPv4Address(args['iprange'][0])), int(ipaddress.IPv4Address(args['iprange'][1]) + 1)):
                for j in range(0, len(args['p'])):
                    bannerWithPort(ipaddress.IPv4Address(ip_int), args['p'][j])

        # Perform grabbing with IP range and port range
        elif len(args['prange']) == 2 and not args['p']: 
            for ip_int in range(int(ipaddress.IPv4Address(args['iprange'][0])), int(ipaddress.IPv4Address(args['iprange'][1]) + 1)):
                for j in range(args['prange'][0], args['prange'][1] + 1):
                    bannerWithPort(ipaddress.IPv4Address(ip_int), j) 
        else:
             print('Please type the command correctly. Examples: \n \t -grab -host [HOST(s)] -p [PORT(s)] \n \t -grab -iprange [START IP] [END IP] -prange [START PORT] [END PORT] \n \t -grab -host [HOST(s)] -prange [START PORT] [END PORT] \n \t -grab -iprange [START IP] [END IP] -p [PORT]')
    else:
        print('Please type the command correctly. Examples: \n \t -grab -host [HOST(s)] -p [PORT(s)] \n \t -grab -iprange [START IP] [END IP] -prange [START PORT] [END PORT] \n \t -grab -host [HOST(s)] -prange [START PORT] [END PORT] \n \t -grab -iprange [START IP] [END IP] -p [PORT]')

# Reverse ip lookup
elif args['reverseip']:
    reverseiplookup(args['reverseip'][0])

# Censys
elif args['censys']:
    censys(args['censys'][0])

# Technologies detector
elif args['techdetect']:
    detectTech(args['techdetect'][0])

# Honeypot
elif args['honeypot']:
    honeypot(args['honeypot'][0])

# Mac address
elif args['macaddress']:
    macaddresslookup(args['macaddress'][0])

# Dns map
elif args['dnsmap']:
    dnsmap(args['dnsmap'][0])

# Subdomains
elif args['subdomains']:
    subdomains(args['subdomains'][0])