#!/bin/bash
clear
echo -e "                Installing \033[91mRed\033[0mNetwork Tool,"
echo -e "                Please Wait..."

# Install necessary packages.
sudo pip3 install python-nmap
sudo pip3 install ipinfo

# Finally.
clear
echo -e "\033[92m[*]\033[0m \033[91mRed\033[0mDDoS Tool was installed successfully."
echo -e "\n\n\033[93mWarning: To use it you need the following programs installed and being reachable from terminal: 'nmap', 'traceroute', 'python3-pip'.\033[0m"
echo -e "\n\nTo run it type '\033[1;4mpython3 RDDoS_Tool.py\033[0m'\n\n"
