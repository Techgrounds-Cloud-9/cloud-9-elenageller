# Virtual Private Cloud (VPC)

Amazon VPC is typically described as a virtual private data center in the cloud. It is a virtual network that is logically isolated from other VPCs.
With a VPC you have full control over the design of the network. You can create subnets, internet gateways (igw), NAT gateways, VPN connections, and more.

There is always a default VPC when you create a new AWS account, but you can add up to 5 non-default VPCs per region per account. This is a soft limit. That is, you can request the limit to be raised.
Many services, like EC2, RDS and ECS require a VPC to be placed into.

When you create a VPC, you must assign a CIDR block. Choose your CIDR block and subnet mask carefully, as they have to allow for enough subnets and hosts and cannot be changed after creation.

Subnets can be either public or private. The only difference is that private subnets do not have an entry for the internet gateway (igw) in their route table, where public subnets do. In other words, private subnets cannot access the internet without a NAT gateway or a NAT instance.

VPCs operate at the regional level, while subnets can only be placed into a single Availability Zone.

Elastic IPs are also available from the VPC menu. EIPs are public IP addresses that can be dynamically allocated to resources like EC2 instances or NAT gateways.



## Study

### Exercise 1

Allocate an Elastic IP address to your account.
Use the Launch VPC Wizard option to create a new VPC with the following requirements:
Region: Frankfurt (eu-central-1)
VPC with a public and a private subnet
Name: Lab VPC
CIDR: 10.0.0.0/16
Requirements for the public subnet:
Name: Public subnet 1
CIDR: 10.0.0.0/24
AZ: eu-central-1a
Requirements for the private subnet:
Name: Private subnet 1
CIDR: 10.0.1.0/24
AZ: eu-central-1a


### Exercise 2

Create an additional public subnet without using the wizard with the following requirements:
VPC: Lab VPC
Name: Public Subnet 2
AZ: eu-central-1b
CIDR: 10.0.2.0/24
Create an additional private subnet without using the wizard with the following requirements:
VPC: Lab VPC
Name: Private Subnet 2
AZ: eu-central-1b
CIDR: 10.0.3.0/24
View the main route table for Lab VPC. It should have an entry for the NAT gateway. Rename this route table to Private Route Table.
Explicitly associate the private route table with your two private subnets.
View the other route table for Lab VPC. It should have an entry for the internet gateway. Rename this route table to Public Route Table.
Explicitly associate the public route table to your two public subnets.

### Exercise 3
Create a Security Group with the following requirements:
Name: Web SG
Description: Enable HTTP Access
VPC: Lab VPC
Inbound rule: allow HTTP access from anywhere
Outbound rule: Allow all traffic

### Exercise 4
Launch an EC2 instance with the following requirements:
AMI: Amazon Linux 2
Type: t3.micro
Subnet: Public subnet 2
Auto-assign Public IP: Enable
User data:
#!/bin/bash
* Install Apache Web Server and PHP
yum install -y httpd mysql php
* Download Lab files
wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
unzip lab-app.zip -d /var/www/html/
* Turn on web server
chkconfig httpd on
service httpd start
Tag:
Key: Name
Value: Web server
Security Group: Web SG
Key pair: no key pair
Connect to your server using the public IPv4 DNS name.

### Used Sources

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html
https://docs.aws.amazon.com/directoryservice/latest/admin-guide/gsg_create_vpc.html
https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html

### Overcome challanges

### Results 

### Exercise 1

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week2/aws10-01-1.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week2/aws10-01-2.png)

### Exercise 2

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week2/aws10-02-1.png)


![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week2/aws10-02-2.png)


![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week2/aws10-02-3.png)


![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week2/aws10-02-4.png)


### Exercise 3

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week2/aws10-03-1.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week2/aws10-03-2.png)

### Exercise 4

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week2/aws10-04-1.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week2/aws10-04-2.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week2/aws10-04-3.png)