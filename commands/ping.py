# Import.
import os


# Ping function.
def ping(host):
    print('\033[4mPing will start. Press CTRL + C to cancel.\033[0m')
    os.system(f'ping {host}')