# Protocol
There is no network without network devices if you want to connect more than two computers together. 

## Key terminology
* Wireshark is a network protocol analyzer, or an application that captures packets from a network connection, such as from your computer to your home office or the internet.

* User Datagram Protocol (UDP) refers to a protocol used for communication throughout the internet. It is specifically chosen for time-sensitive applications like gaming, playing videos, or Domain Name System (DNS) lookups.

* ‘Fire and forget’ strategy
Fundamentally UDP is a fire and forget protocol. You send a data packet to a target, and that's it!
* ‘Three-way handshake’
A three-way handshake establishes a reliable connection between client and server, and it is vital for online communication.

**Layer** **Name**	  **Protocols**
Layer 7	Application	  SMTP, HTTP, FTP, POP3, SNMP
Layer 6	Presentation	MPEG, ASCH, SSL, TLS
Layer 5	Session	NetBIOS, SAP
Layer 4	Transport	TCP, UDP
Layer 3	Network	IPV5, IPV6, ICMP, IPSEC, ARP, MPLS.
Layer 2	Data Link	RAPA, PPP, Frame Relay, ATM, Fiber Cable, etc.
Layer 1	Physical	RS232, 100BaseTX, ISDN, 11.

## Exercise

1. Identify several other protocols and their associated OSI layer. Name at least one for each layer.
2. Figure out who determines what protocols we use and what is needed to introduce your own protocol.
3. Look into wireshark and install this program. Try and capture a bit of your own network data. Search for a protocol you know and try to understand how it functions.

### Sources
https://www.guru99.com/layers-of-osi-model.html
https://www.imperva.com/learn/application-security/osi-model/
https://www.internetx.com/en/news-detailview/who-creates-the-standards-and-protocols-for-the-internet/
https://afteracademy.com/blog/what-are-protocols-and-what-are-the-key-elements-of-protocols


### Overcome challenges

To analyze the data from Wireshack

### Results

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/NTW-03-1.png)

**The organisations that determine what protocols we use are:**

World Wide Web Consortium (W3C)
Telecommunication Standardization Sector (ITU-T)
Internet Architecture Board (IAB)
Internet Assigned Numbers Authority (IANA)
Internet Corperation for Assigned Names and Numbers (ICANN)
Internet Engineering Task Force (IETF)
Internet Society (ISOC)
Internet Research Task Force (IRTF)

* For new protocol needed - have it accepted by an IETF working group.

* In Wireshack I filtered by TCP protocols, and found 3 way handshake. You can see for each of the pakket what protocol it is, and what the aknowledgement is, its number and sequence numbers. How the converstaion being tracked by TCP from client (myb computer) to server

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/NTW-03-2.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/NTW03-3.gif)

