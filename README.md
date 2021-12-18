# 🌐🔍 Red Network Tool (أداة شبكة ريد) ![](https://img.shields.io/apm/l/vim-mode) ![](https://img.shields.io/github/stars/Red-company/RedNetwork_Tool?style=social)
![plot](./Screenshots/RNT_main.png)

## What is RedNetwork Tool?
Red Network Tool is a tool for network exploration and info finding over the internet. `There is a config feature!`

Current tool version consist of:
- Ifconfig.
- Port scan(comprehensive, TCP, SYN, ACK, UDP).
- Host discovery(scan for up devices on a local network).
- DNS checks with geolocation information.
- Banner grabbing.
- Ping(send ICMP packets to a host to check connectivity).
- Traceroute(diagnose route paths and measure transit delays).
- Reverse ip lookup.
- Censys.
- Site technologies detection feature.
- Honeypot probability.
- Mac address lookup.

## Supported Devices:
 This program is supported in all operating system like Linux, Windows and MacOs. The Code is written in python3, so don't worry it works well without any bugs.
 
## Installing (Windows/Linux/MacOs):
```diff
git clone https://github.com/Red-company/RedNetwork_Tool.git
cd RN_Tool
bash setup.sh

! After executing setup.sh, you'll need to edit newly created config.py

sudo python3 RedNetwork_Tool.py
```

## How to use? Let's figure it out:

### Ifconfig
If you want to display your system's current TCP/IP network configuration, type the following command:

`-ifconfig`

![plot](./Screenshots/RNT_ifconfig.png)

### Ports scanning
Supported types:
- SYN (`-scansyn`)
- TCP (`-scantcp`) 
- UDP (`-scanudp`)
- ACK (`-scanack`)
- Comprehensive scan (`-scan`).

`-scan -host [HOST(s)]`

`-scan -host [HOST(s)] -p [PORT(s)]`

`-scan -host [HOST(s)] -prange [START PORT] [END PORT]`

`-scan -iprange [START IP] [END IP] -p [PORT(s)]`

`-scan -iprange [START IP] [END IP] -prange [START PORT] [END PORT]`

![plot](./Screenshots/RNT_scan.png)

### Local scan
Perform scan to detect local devices.

`-scanlocal`

![plot](./Screenshots/RNT_scanlocal.png)

### DNS check
Similar to the well known `nslookup` command used on UNIX systems.

`-ns [HOST(s)]`

![plot](./Screenshots/RNT_ns.png)

### Banner grabbing
To perform banner grabbing, type one of the following commands:

`-grab -host [HOST(s)] -p [PORT(s)]`

`-grab -iprange [START IP] [END IP] -prange [START PORT] [END PORT]`

`-grab -host [HOST(s)] -prange [START PORT] [END PORT]`

`-grab -iprange [START IP] [END IP] -p [PORT(s)]`

![plot](./Screenshots/RNT_grab.png)

### Ping
Uses to send ICMP packets to a host to check connectivity, simply type:

`-ping [HOST]`

![plot](./Screenshots/RNT_ping.png)

### Traceroute
Uses to diagnose route paths and measure transit delays, use the following command:

`-traceroute [HOST]`

![plot](./Screenshots/RNT_traceroute.png)

### Reverse ip lookup
Uses to perform a reverse ip lookup, to perform write:

`-reverseip [HOST]`

![plot](./Screenshots/RNT_reverseiplookup_1.png)

![plot](./Screenshots/RNT_reverseiplookup_2.png)

### Censys
Censys feature, just type:

`-censys [HOST]`

![plot](./Screenshots/RNT_censys_1.png)

![plot](./Screenshots/RNT_censys_2.png)

### TechDetect
Uses to detect site's technologies. Type:

`-techdetect [URL]`

![plot](./Screenshots/RNT_techdetect_1.png)

![plot](./Screenshots/RNT_techdetect_2.png)

### Honeypot
Uses to calculate probability of ip being honeypot. To calculate just type:

`-honeypot [IP]`

![plot](./Screenshots/RNT_honeypot_1.png)

![plot](./Screenshots/RNT_honeypot_2.png)

### Mac address lookup
You can check information about certain mac address with it, type:

`-macaddress [MAC]`

![plot](./Screenshots/RNT_macaddress_1.png)

![plot](./Screenshots/RNT_macaddress_2.png)

## More screenshots? Here they are:

![plot](./Screenshots/RNT_about.png)

![plot](./Screenshots/RNT_setup.png)

![plot](./Screenshots/RNT_help.png)

##
All material in this repository is in the public domain.
