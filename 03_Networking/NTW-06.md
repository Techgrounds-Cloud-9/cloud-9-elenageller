# Subnetting
 

## Key terminology

Subnet is a segmented piece of a larger network. Subnets are a logical partition of an IP network into multiple, smaller network segments.  
Instances in the private subnet are back-end servers that don't need to accept incoming traffic from the internet and therefore do not have public IP addresses
A public subnet is a subnet that's associated with a route table that has a route to an internet gateway.
A routing table is a set of rules, often viewed in table format, that is used to determine where data packets traveling over an Internet Protocol (IP) network will be directed.
LAN
NAT gateway (Network Address Translation) provides outbound internet connectivity for one or more subnets of a virtual network. Once NAT gateway is associated to a subnet, NAT provides source network address translation (SNAT) for that subnet. 
Hosts . Each computer, or host, on the internet has at least one IP address as a unique identifier.
An IP address is divided into two fields: a Network Prefix (also called the Network ID) and a Host ID.

## Exercise

Create a network architecture that meets the following requirements:
1 private subnet accessible only from within the LAN. This subnet must be able to accommodate a minimum of 15 hosts.
1 private subnet that has Internet access through a NAT gateway. This subnet must be able to accommodate a minimum of 30 hosts (the 30 hosts does not include the NAT gateway).
1 public subnet with an internet gateway. This subnet must be able to accommodate a minimum of 5 hosts (the 5 hosts does not include the internet gateway).


### Sources

https://www.youtube.com/watch?v=s_Ntt6eTn94
https://www.techtarget.com/searchnetworking/definition/subnet
https://www.youtube.com/watch?v=ecCuyq-Wprc


### Overcome challenges

learn and understand about subnetting

### Results

If we need to create 3 subnets, then we check the maximum number of hosts per subnet, excl. 2 which are Broadcast IP and Network ID.
Broadcast IP we get from next Subnets network IP (current Network IP + 64) minus 1. 
In my example First Subnet's Network IP is 192.168.10.0/26 for 30 hosts, 2nd - 192.168.10.64/27 for 15 hosts and 3rd- 192.168.10.96/29 for 5 hosts.

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/NTW-06-01.png)


