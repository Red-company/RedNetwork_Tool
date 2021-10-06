# Import.
import nmap
import sys
import os
import multiprocessing
import socket


# Preparing.
scanner = nmap.PortScanner()


# Scan status function.
def scanStatus(str, inputed):
    try:
        scanner.scan(str, '1', '-v -sT')

    except KeyboardInterrupt:  
        sys.exit('\n^C\n')

    except:
        e = sys.exc_info()
        print(f'\n\033[91m{e}\033[0m')
        sys.exit(1)

    else:
        if scanner[str].state() == 'up':
            print(f'\033[92mStatus: {str} is {scanner[str].state()}\033[0m')

        else: 
            print(f'\033[91mStatus: {str} is {scanner[str].state()}\033[0m')
            sys.exit()


# Scan function.
def scan(str, inputed, prstart, prend, scantype):
    scanStatus(str, inputed)
    print('\033[4mScan will start. Press CTRL + C to cancel.\033[0m') 

    try:
        print(f'\033[93mScanning {str}:{prstart}-{prend}\033[0m') 
        scanner.scan(str, f'{prstart}-{prend}', f'-v {scantype}')

    except KeyboardInterrupt: 
        sys.exit('\n^C\n')

    except: 
        e = sys.exc_info()[1]
        printcolor(f'\033[91m\n{e}\033[0m')

    else:
        if len(scanner[str].all_protocols()) == 0:
            print('No port(s) found.')

        else:
            for protocol in scanner[str].all_protocols():
                if scanner[str][protocol].keys():
                    print(f'\nProtocol: {protocol.upper()}')
                    print('\n PORT     \t\tSTATE     \t\tSERVICE')

                    for port in scanner[str][protocol].keys():
                        print(f" {port}      \t\t{scanner[str][protocol][port]['state']}       \t\t{scanner[str][protocol][port]['name']}")


# Scan with port function.
def scanWithPort(str, inputed, int, i, j, scantype):
    try:
        if j == 0:
            scanStatus(str, inputed)
            print(f'\033[93mScanning {str}\033[0m') 
            print('\033[4mScan will start. Press CTRL + C to cancel.\033[0m')

        scanner.scan(str, f'{int}', f'-v {scantype}')

    except KeyboardInterrupt: 
        sys.exit('^C\n')

    except:
        e = sys.exc_info()[1]
        print(f'{e}')

    else:
        for protocol in scanner[str].all_protocols():
            if scanner[str][protocol].keys():
                if j == 0:
                    print(f'Protocol: {protocol.upper()}')
                    print('\n PORT     \t\tSTATE     \t\tSERVICE')

                for port in scanner[str][protocol].keys():
                    print(f" {port}      \t\t{scanner[str][protocol][port]['state']}       \t\t{scanner[str][protocol][port]['name']}")


# Scan local function.
def scanLocalDevices():
    network = input('Please type the network you want to scan (Example: 192.168.1.0/24): ')
    print(f'The network address is {network}')

    try:
        print(f'\033[93mScanning for devices on {network} network...\033[0m') 
        scanner.scan(hosts = network, arguments = '-v -sn')

    except KeyboardInterrupt:
        sys.exit('\n^C\n')

    except: 
        e = sys.exc_info()[1]
        print(f'\033[91m\n{e}\033[0m')

    else:
        #print(scanner._scan_result.items()) ###testing
        for host in scanner.all_hosts():
            if scanner[host]['status']['state'] == 'up':
                print(f"{host}      \t\t {scanner[host]['vendor']}")
           