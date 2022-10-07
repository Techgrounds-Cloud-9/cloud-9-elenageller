# Firewall
 

## Key terminology

Firewall is  a network security device that monitors and filters incoming and outgoing network traffic based on an organization's previously established security policies.
Firewalld is a zone-based firewall. Zone-based firewalls are network security systems that monitor traffic and take actions based on a set of defined rules applied against incoming/outgoing packets
UFW (ncomplicated firewal) is used through the command line (although it has GUIs available), and aims to make firewall configuration easy (or, uncomplicated).
Iptables is a firewall program for Linux. It will monitor traffic from and to your server using tables. These tables contain sets of rules, called chains, that will filter incoming and outgoing data packets
A stateful firewall is a kind of firewall that keeps track and monitors the state of active network connections while analyzing incoming traffic and looking for potential traffic and data risks. This firewall is situated at Layers 3 and 4 of the OSI model

## Exercise

Install a web server on your VM.
View the default page installed with the web server.
Set the firewall to block web traffic but allow ssh traffic.
Verify that the firewall is doing its job.


### Sources

https://cloud.google.com/compute/docs/tutorials/basic-webserver-apache
https://superuser.com/questions/387948/how-can-i-determine-if-apache-is-installed-on-a-system
https://help.ubuntu.com/community/UFW
https://opensource.com/article/18/5/how-find-ip-address-linux
https://help.ubuntu.com/community/UFW
https://www.youtube.com/watch?v=-CzvPjZ9hp8
https://www.digitalocean.com/community/tutorials/ufw-essentials-common-firewall-rules-and-commands

### Overcome challenges

To find an externat ip adress which must be connected through port which we have received in the beginig of course

### Results

First I need to install Apache, and open a default page in the browser
 and then allow the required ports to ufw firewall, then to close web by denying responsible ports.
 
![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-02-1.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC02-2.png)

 and then allow the required ports to ufw firewall, then to close web by denying responsible ports.

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-02-3.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-02-4.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-02-4.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-02-5.png)

