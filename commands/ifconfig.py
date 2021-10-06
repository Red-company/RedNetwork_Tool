# Import.
from sys import platform
import os


# Ifconfig function.
def ifconfig():
    ifconfig_cmd = "ifconfig"

    if platform == "linux" or platform == "linux2":
       ifconfig_cmd = "ifconfig -a"

    elif platform == "win32":
        ifconfig_cmd = "ipconfig /all"

    os.system(ifconfig_cmd)