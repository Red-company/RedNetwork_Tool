# 🌐🔍 Red Network Tool (أداة شبكة ريد) ![](https://img.shields.io/apm/l/vim-mode) ![](https://img.shields.io/github/stars/Red-company/RedNetwork_Tool?style=social)
![plot](./Screenshots/RNT_main.png)

## What is RedNetwork Tool?
_Red Network Tool_ is a tool for network exploration and info finding over the internet. _`There is a config feature!`_

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
- Dns mapping.

## Supported Devices:
 This program is supported in all operating system like _Linux_, _Windows_ and _MacOS_. The Code is written in _python3_, so don't worry it works well without any bugs.
 
## Installing (_Windows/Linux/MacOS_):
```diff
git clone https://github.com/Red-company/RedNetwork_Tool.git
cd RN_Tool
bash setup.sh

! After executing setup.sh, you'll need to edit newly created config.py

sudo python3 RedNetwork_Tool.py
```

## How to use? Let's figure it out:

### Ifconfig
If you want to display your system's current _TCP/IP_ network configuration, type the following command:

`-ifconfig`

![plot](./Screenshots/RNT_ifconfig.png)

### Ports scanning
Supported types:
- _SYN_ (`-scansyn`)
- _TCP_ (`-scantcp`) 
- _UDP_ (`-scanudp`)
- _ACK_ (`-scanack`)
- _Comprehensive scan_ (`-scan`).

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
Similar to the well known _`nslookup`_ command used on _UNIX_ systems.

`-ns [HOST(s)]`

![plot](./Screenshots/RNT_ns.png)

### Banner grabbing
To perform _banner grabbing_, type one of the following commands:

`-grab -host [HOST(s)] -p [PORT(s)]`

`-grab -iprange [START IP] [END IP] -prange [START PORT] [END PORT]`

`-grab -host [HOST(s)] -prange [START PORT] [END PORT]`

`-grab -iprange [START IP] [END IP] -p [PORT(s)]`

![plot](./Screenshots/RNT_grab.png)

### Ping
Uses to send _ICMP_ packets to a host to check connectivity, simply type:

`-ping [HOST]`

![plot](./Screenshots/RNT_ping.png)

### Traceroute
Uses to diagnose route paths and measure _transit delays_, use the following command:

`-traceroute [HOST]`

![plot](./Screenshots/RNT_traceroute.png)

### Reverse ip lookup
Uses to perform a _reverse ip lookup_, to perform write:

`-reverseip [HOST]`

![plot](./Screenshots/RNT_reverseiplookup_1.png)

![plot](./Screenshots/RNT_reverseiplookup_2.png)

### Censys
_Censys_ feature, just type:

`-censys [HOST]`

![plot](./Screenshots/RNT_censys_1.png)

![plot](./Screenshots/RNT_censys_2.png)

### TechDetect
Uses to detect site's _technologies_. Type:

`-techdetect [URL]`

![plot](./Screenshots/RNT_techdetect_1.png)

![plot](./Screenshots/RNT_techdetect_2.png)

### Honeypot
Uses to calculate probability of ip being _honeypot_. To calculate just type:

`-honeypot [IP]`

![plot](./Screenshots/RNT_honeypot_1.png)

![plot](./Screenshots/RNT_honeypot_2.png)

### Mac address lookup
You can check information about certain _mac address_ with it, type:

`-macaddress [MAC]`

![plot](./Screenshots/RNT_macaddress_1.png)

![plot](./Screenshots/RNT_macaddress_2.png)

### Dns map
Do you want to get a _map of dns servers_ of certain organization? Okay, here it is:

`-dnsmap [DOMAIN]`

![plot](./Screenshots/RNT_dnsmap_1.png)

![plot](./Screenshots/RNT_dnsmap_2.png)

![plot](./Screenshots/RNT_dnsmap_3.png)

## More screenshots? Here they are:

![plot](./Screenshots/RNT_about.png)

![plot](./Screenshots/RNT_setup.png)

![plot](./Screenshots/RNT_help.png)

##
All material in this repository is in the public domain.
