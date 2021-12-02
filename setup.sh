#!/bin/bash
clear
echo -e "                Installing \033[91mRed\033[0mNetwork Tool,"
echo -e "                Please Wait..."

# Installing necessary packages.
sudo pip3 install python-nmap
sudo pip3 install ipinfo
sudo pip install requests

# Creating config file.
echo "#" > config.py
echo "# Config file for Red Network Tool." >> config.py
echo "#" >> config.py
echo "" >> config.py
echo "" >> config.py
echo "# Shodan api key." >> config.py
echo "shodan_key = ''" >> config.py
echo "" >> config.py
echo "# Ipinfo api key." >> config.py
echo "ipinfo_key = ''" >> config.py
echo "" >> config.py
echo "# Wappalyzer api key." >> config.py
echo "wappalyzer_key = ''" >> config.py

# Finally.
clear
echo -e "\033[92m[*]\033[0m \033[91mRed\033[0mNetwok Tool was installed successfully."
echo -e "\n\n\033[93mWarning: To use it you need the following programs installed and being reachable from terminal: 'nmap', 'traceroute', 'python3-pip'.\033[0m"
echo -e "\n\nTo run it type '\033[1;4msudo python3 RedNetwork_Tool.py\033[0m'\n\n"
