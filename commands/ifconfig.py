"""
Copyright (c) 2020-2021 Vladimir Rogozin (vladimir20040609@gmail.com)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

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