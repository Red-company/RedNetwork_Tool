"""
Copyright (c) 2020-2021 Vladimir Rogozin (vladimir20040609@gmail.com)

Distributed under the MIT License (MIT) (See accompanying file LICENSE.txt
or copy at http://opensource.org/licenses/MIT)
"""

# Import.
from   platform import system
import sys
import os

from command_handler import *


# Version.
version = "1.4"


# Platform info
uname = system()

if uname == "Windows":
    cmd_clear_clear = 'cls'
else:
    cmd_clear = 'clear'


# Variables.
command_history = []


# RedNetwork_Tool.
def main():
    while True:
        # UI.
        os.system(cmd_clear)
        print("\033[91m _ __         \033[0m\033[36m _ __                      \033[0m    ______    _            Version: " + version)
        print("\033[91m( /  )       /\033[0m\033[36m( /  )   _/_              /\033[0m   (  /      //")
        print("\033[91m /--<  _  __/ \033[0m\033[36m /  / _  /  , , , __ _   /<\033[0m     /__ __ // ")
        print("\033[91m/   \\_(/_(_/_ \033[0m\033[36m/  (_(/_(__(_(_/_(_)/ (_/ |_\033[0m  _/(_)(_)(/_ ")
        print("\n                     Author: Mr.\033[91mRed\033[0m")
        print(" Github: https://github.com/Red-company/RedNetwork_Tool")
        print('                For legal purposes only\n')

        # Input.
        command = str(input("RNT > "))

        if command != "history":
            command_history.append(command.strip())

        if command.strip() == "history":
            if len(command_history) > 0:
                print("Last commands:")

                for i in range(0, len(command_history)):
                    print(command_history[i])

            else:
                print("No commands history.")

            x = input("\nPress Enter to continue.")

        elif command.strip() == "about":
            print("\n\033[101mEasy.       .سهل\033[0m  \033[101m       \033[0m  \033[101m        \033[0m \033[101m       \033[0m \033[0m                \033[92m_____\033[0m")
            print("                  \033[101m   \033[0m  \033[101m   \033[0m \033[101m   \033[0m      \033[101m   \033[0m  \033[101m   \033[0m\033[0m             \033[92m.-'     '-.\033[0m")
            print("\033[101mOpen.      .افتح\033[0m  \033[101m       \033[0m  \033[101m      \033[0m   \033[101m   \033[0m  \033[101m   \033[0m           \033[92m.'\033[91m____\033[0m secure\033[92m'.\033[0m")
            print("                  \033[101m   \033[0m \033[101m   \033[0m  \033[101m   \033[0m      \033[101m   \033[0m  \033[101m   \033[0m          \033[92m/  \033[91m|  _ \\\033[0m  \033[93m__\033[0m   \033[92m\\\033[0m")
            print("\033[101mSecure.    .يؤمن\033[0m  \033[101m   \033[0m  \033[101m   \033[0m \033[101m        \033[0m \033[101m       \033[0m          \033[92m;\033[0m r \033[91m| |_) /\033[0m\033[93m/ o\\\033[0m t \033[92m;\033[0m")
            print("                                                     \033[92m|\033[0m e \033[91m|  _ <\033[0m \033[93m\\__/\033[0m e \033[92m|\033[0m")
            print("RedNetwork Tool is an open source tool for           \033[92m;\033[0m d \033[91m|_| \\ \\\033[0m \033[93m<|\033[0m  a \033[92m;\033[0m")
            print("network exploring. You can scan networks,             \033[92m\\       \033[91m\\/\033[0m \033[93m<|\033[0m  m\033[92m/\033[0m")
            print("look for vulnerabilities and information               \033[92m'.\033[0m member \033[93m<|\033[0m \033[92m.'\033[0m")
            print("with it.                                                 \033[92m'-._____.-'\033[0m")
            print("\nAuthor of the program is not responsible for")
            print("it's usage, everybody MUST use it ONLY in         member-id: 'rst-00000003'")
            print("legit cases.")
            print("\nFor more information visit project's site.")
            
            goon = input("\n\n\n\n\n\nPress Enter to continue.")

        else: # If command.                           
            os.system(f"python3 command_handler.py {command}")  
            x = input("\nPress Enter to continue.")                                        


# Let's begin.
main()
