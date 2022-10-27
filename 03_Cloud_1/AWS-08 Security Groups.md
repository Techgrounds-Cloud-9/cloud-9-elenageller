# Security Groups

* Security Groups are stateful virtual firewalls that can be assigned to instances. They do not run in the OS, but rather in the VPC.

* One Security Group can be assigned to multiple instances. The other way around, one instance can have up to 5 Security Groups.

* Security Groups only have allow rules. Everything not explicitly allowed is automatically implicitly denied.

* A Network Access Control List (NACL) is a stateless firewall that runs on the subnet level in a VPC.
* A NACL has both explicit allow and deny rules. Rules have a number assigned to them. This number indicates the order in which the rules are applied.

By default, a NACL is configured to allow all traffic in and out of the network.

## Key terminology


## Study

Security Groups in AWS
Network Access Control Lists in AWS

### Used Sources

https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html

https://www.checkpoint.com/cyber-hub/cloud-security/what-is-aws-security-groups/#:~:text=Check%20Point%20solution-,What%20are%20AWS%20Security%20Groups%3F,traffic%20from%20your%20instance%2C%20respectively. 

### Results 


NACL can be understood as the firewall or protection for the subnet. Security group can be understood as a firewall to protect EC2 instances. These are stateless, meaning any change applied to an incoming rule isn't automatically applied to an outgoing rule.

### Security Groups in AWS

An AWS security group acts as a virtual firewall for your EC2 instances to control incoming and outgoing traffic. Both inbound and outbound rules control the flow of traffic to and traffic from your instance, respectively.

### Network Access Control Lists in AWS

A network access control list (NACL) is an additional way to control traffic in and out of one or more subnets. Unlike AWS Security Groups, NACLs are stateless, so both inbound and outbound rules will get evaluated. Network ACLs can be set up as an optional, additional layer of security to your VPC.