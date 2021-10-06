# Red DDoS Tool ![](https://img.shields.io/apm/l/vim-mode) ![](https://img.shields.io/github/last-commit/Red-company/RedNetwork_Tool) ![](https://img.shields.io/github/release-date/Red-company/RedNetwork_Tool) ![](https://img.shields.io/github/stars/Red-company/RedNetwork_Tool?style=social)
![plot](./Screenshots/RNT_main.png)

## What is RedNetwork Tool?
Red Network Tool is a tool for network exploration and info finding.

Current tool consist of:
- Ifconfig.
- Port scan(comprehensive, TCP, SYN, ACK, UDP).
- Host discovery(scan for up devices on a local network).
- DNS checks with geolocation information.
- Banner grabbing.
- Ping(send ICMP packets to a host to check connectivity).
- Traceroute(diagnose route paths and measure transit delays).

## Supported Devices:
 This program is supported in all operating system like Linux, Windows and MacOs. The Code is written in python3, so Dont worry it works well without any bugs.
 
## Installing (Windows/Linux/MacOs/Termux):
```
git clone https://github.com/Red-company/RedNetwork_Tool.git
cd RN_Tool
sudo . setup.sh
sudo python3 RedNetwork_Tool.py
```

## How to use? Let's figure it out:

### ifconfig
If you want to display your system's current TCP/IP network configuration, type the following command:

`-ifconfig`

![plot](./Screenshots/RNT_ifconfig.png)

### ports scanning
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

### local scan
Perform scan to detect local devices.

`-scanlocal`

![plot](./Screenshots/RNT_scanlocal.png)

### DNS check
Similar to the well known `nslookup` command used on UNIX systems.

`-ns [HOST(s)]`

![plot](./Screenshots/RNT_ns.png)

### banner grabbing
To perform banner grabbing, type one of the following commands:

`-grab -host [HOST(s)] -p [PORT(s)]`

`-grab -iprange [START IP] [END IP] -prange [START PORT] [END PORT]`

`-grab -host [HOST(s)] -prange [START PORT] [END PORT]`

`-grab -iprange [START IP] [END IP] -p [PORT(s)]`

![plot](./Screenshots/RNT_grab.png)

### ping
Uses to send ICMP packets to a host to check connectivity, simply type:

`-ping [HOST]`

![plot](./Screenshots/RNT_ping.png)

### traceroute
Uses to diagnose route paths and measure transit delays, use the following command:

`-traceroute [HOST]`

![plot](./Screenshots/RNT_traceroute.png)

## Screenshots? Here they are:

![plot](./Screenshots/RNT_about.png)

![plot](./Screenshots/RNT_help.png)

##
All material in this repository is in the public domain.
