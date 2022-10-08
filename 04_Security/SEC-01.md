# Network Detection
 

## Key terminology

* Nmap is a network scanner utility used for port mapping, host discovery and vulnerability scanning. Most of its functions are based on using IP packet analysis to detect and identify remote hosts, operating systems and services.

## Exercise

1. Scan the network of your Linux machine using nmap. What do you find?
2. Open Wireshark in Windows/MacOS Machine. Analyse what happens when you open an internet browser. (Tip: you will find that Zoom is constantly sending packets over the network. You can either turn off Zoom for a minute, or look for the packets sent by the browser between the packets sent by Zoom.)

### Sources

https://vitux.com/find-devices-connected-to-your-network-with-nmap/
https://securitytrails.com/blog/nmap-commands

### Overcome challenges

First I could not login into my Linux, because my pem key file was not detected by some reasons, which perefectly worked last week. SO i tried several options, and it worked after I renamed the file. Then I installed Nepmap with sudo command.

### Results

* In order to know which devices are connected to my network, first I needed to determine the IP range or subnet mask of my network. I used the ifconfig command to determine this IP. In order to run the ifconfig command, I installed the net-tools package
* The highlighted IP in the output shows that our system uses the subnet mask 10.115.158.132 and the range is 255. So our network IP range is from 10.115.158.0 to 10.115.158.255.

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-01-1.png)

* Used command nmap -sP 10.115.158.0/24 to show how many devices connected to the network

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-01-2.png)

* also Nmap scans the open ports

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC01-3.png)

* here I filtered it bt TRPC port

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-01-4.png)

* when Internat Browser is open, Wireshark runs very fast, the data keeps requesting and receiving. In the details you can see how this proccess is heppening, and what protocols its using.

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-01-5.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-01-6.png)
