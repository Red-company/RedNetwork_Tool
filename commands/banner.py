"""
Copyright (c) 2020-2021 Vladimir Rogozin (vladimir20040609@gmail.com)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

# Import.
import socket
import sys
import multiprocessing


# Banner function.
def bannerWithPort(host, port):
    socket.setdefaulttimeout(2)
    sckt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        print(f'\033[93mConnecting to {host}:{port}\033[0m')
        sckt.connect((host, port))
        sckt.send('WhoAreYou\r\n'.encode())
        banner = sckt.recv(1024)
        
    except KeyboardInterrupt:
        sys.exit('\n')

    except:
        e = sys.exc_info()[1]
        print(f'\033[91m{e}\033[0m\n')

    else:
        sckt.close()
        print(f'\033[92m{banner.decode()}\033[0m\n')
