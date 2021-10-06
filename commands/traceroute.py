# Import.
import os


# Traceroute function.
def traceroute(host):
    print('\033[4mTraceroute will start. Press CTRL + C to cancel.\033[0m')
    os.system(f'traceroute {host}')