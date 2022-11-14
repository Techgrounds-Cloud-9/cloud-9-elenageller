# Files,AppServices,CDN,DNS,Database



## Key terminology

* AWS Elastic Beanstalk is an orchestration service offered by Amazon Web Services for deploying applications which orchestrates various AWS services, including EC2, S3, Simple Notification Service, CloudWatch, autoscaling, and Elastic Load Balancers.

* Amazon CloudFront is a content delivery network operated by Amazon Web Services. Content delivery networks provide a globally-distributed network of proxy servers that cache content, such as web videos or other bulky media, more locally to consumers, thus improving access speed for downloading the content.

* Amazon Route 53 is a scalable and highly available Domain Name System service

* Amazon Elastic File System is a cloud storage service provided by Amazon Web Services designed to provide scalable, elastic, concurrent with some restrictions, and encrypted file storage for use with both AWS cloud services and on-premises resources

* Amazon Relational Database Service is a distributed relational database service by Amazon Web Services. It is a web service running "in the cloud" designed to simplify the setup, operation, and scaling of a relational database for use in applications. It is a collection of managed services that makes it simple to set up, operate, and scale databases in the cloud

* Amazon Aurora is a relational database management system (RDBMS) built for the cloud with full MySQL and PostgreSQL compatibility. Aurora gives you the performance and availability of commercial-grade databases at one-tenth the cost.

## Study

1. Elastic Beanstalk
2. CloudFront
3. Route53
4. EFS	
5. RDS
6. Aurora

## Practical:

1. EFS	
2. RDS/Aurora

**A handy list of tasks you should be able to do practically:**
Where can I find this service in the console?
How do I turn on this service?
How can I link this service to other resources?

### Used Sources

https://docs.aws.amazon.com

### Overcome challanges

### Results 

1. Elastic Beanstalk is a service for deploying and scaling web applications and services. Upload your code and Elastic Beanstalk automatically handles the deployment—from capacity provisioning, load balancing, and auto scaling to application health monitoring.
Elastic Beanstalk fully manages this load balancer, taking care of security settings and of terminating the load balancer when you terminate your environment.

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week2/aws13-01.jpeg)

**Benefits Of AWS Elastic Beanstalk**

* Fast and simple to deploy: It is the simplest and fastest way to deploy your application on AWS. You just use the AWS Management Console, a Git repository, or an integrated development environment (IDE) such as Eclipse or Visual Studio to upload your application, and it automatically handles the deployment details of capacity provisioning, auto-scaling, load balancing, and application health monitoring. Within minutes, your application will be ready to use without any infrastructure or resource configuration work on your part.
* Scalable: It automatically scales your application up and down based on your application’s need using easily adjustable Auto Scaling settings. For e.g, you can use CPU utilization metrics to trigger Auto Scaling actions. With this, your application can handle peaks in workload or traffic while minimizing your costs.
* Developer productivity: Amazon Elastic Beanstalk provisions and operates the infrastructure and manages the application stack (platform) for you, so you don’t have to spend the time or develop the expertise. It also keeps the underlying platform running your application up-to-date with the latest patches and updates. So, you can focus on writing code rather than spending time managing and configuring servers, load balancers, databases, firewalls, and networks.
* Complete infrastructure control: You are free to select the AWS resources, such as Amazon EC2 instance type, that are optimal for your application. Additionally, it lets you “open the hood” and allow you to full control over the AWS resources powering your application. If you decide you want to take over some (or all) of the elements of your infrastructure, you can do so seamlessly by using Amazon Elastic Beanstalk’s management capabilities.

2. Amazon CloudFront is a web service that speeds up distribution of your static and dynamic web content, such as . html, . css, . js, and image files, to your users

**Benefits of AWS CloudFront**
* It will cache your content in edge locations and decrease the workload, thus resulting in high availability of applications.
* It is simple to use and ensures productivity enhancement.
* It provides high security with the ‘Content Privacy’ feature.
* It facilitates GEO targeting service for content delivery to specific end-users.
* It uses HTTP or HTTPS protocols for quick delivery of content.
* It is less expensive, as it only charges for the data transfer.


3. Amazon Route 53 is a scalable and highly available Domain Name System service

**Features of Route 53**

* Easy to register your domain − We can purchase all level of domains like .com, .net, .org, etc. directly from Route 53.

* Highly reliable − Route 53 is built using AWS infrastructure. Its distributed nature towards DNS servers help to ensure a consistent ability to route applications of end users.

* Scalable − Route 53 is designed in such a way that it automatically handles large volume queries without the user’s interaction.

* Can be used with other AWS Services − Route 53 also works with other AWS services. It can be used to map domain names to our Amazon EC2 instances, Amazon S3 buckets, Amazon and other AWS resources.

* Easy to use − It is easy to sign-up, easy to configure DNS settings, and provides quick response to DNS queries.

* Health Check: Route 53 monitors the health of the application. If an outage is detected, then it automatically redirects the users to a healthy resource.

* Cost-Effective − Pay only for the domain service and the number of queries that the service answers for each domain.

* Secure − By integrating Route 53 with AWS (IAM), there is complete control over every user within the AWS account, such as deciding which user can access which part of Route 53.

**When you create a record, you choose a routing policy, which determines how Amazon Route 53 responds to queries:**

**Simple routing policy** – Use for a single resource that performs a given function for your domain, for example, a web server that serves content for the example.com website. 
You can use simple routing to create records in a private hosted zone.

**Failover routing policy** – Use when you want to configure active-passive failover. 
You can use failover routing to create records in a private hosted zone.

**Geolocation routing policy** – Use when you want to route traffic based on the location of your users. 
You can use geolocation routing to create records in a private hosted zone.

**Geoproximity routing policy** – Use when you want to route traffic based on the location of your resources and, optionally, shift traffic from resources in one location to resources in another.

**Latency routing policy** – Use when you have resources in multiple AWS Regions and you want to route traffic to the region that provides the best latency. 
You can use latency routing to create records in a private hosted zone.

**IP-based routing policy** – Use when you want to route traffic based on the location of your users, and have the IP addresses that the traffic originates from.

**Multivalue answer routing policy** – Use when you want Route 53 to respond to DNS queries with up to eight healthy records selected at random. 
You can use multivalue answer routing to create records in a private hosted zone.

**Weighted routing policy** – Use to route traffic to multiple resources in proportions that you specify. 
You can use weighted routing to create records in a private hosted zone.

4. EFS
* Amazon Elastic File System (Amazon EFS) is a simple, serverless, set-and-forget, elastic file system. There is no minimum fee or setup charge. You pay only for the storage you use, for read and write access to data stored in Infrequent Access storage classes, and for any provisioned throughput.
* The data stored in EBS remains in the same availability zone and multiple replicas are created within the same availability zone whereas in EFS the data stored remains in the same region and multiple replicas are created within the same region

5. RDS
* Amazon RDS supports three types of instance classes: general purpose, memory optimized, and burstable performance.
* As a fully managed service, Amazon RDS handles many of the onerous tasks of database management, such as migration, patching, and backup and recovery.
* Amazon RDS Read Replicas enable you to create one or more read-only copies of your database instance within the same AWS Region or in a different AWS Region. Updates made to the source database are then asynchronously copied to your Read Replicas. 

 Read replicas are available in Amazon RDS for MySQL, MariaDB, PostgreSQL, Oracle, and SQL Server as well as Amazon Aurora.

6. RDS allows you to provision up to 5 replicas, and the process of replication is slower compared to Aurora. Aurora allows you to provision up to 15 replicas, and the replication is done in milliseconds. Aurora scales faster because it can add new read replicas quickly.

