# AWS Global Infrastructure


## Key terminology

* Availability Zones are distinct locations within an AWS Region that are engineered to be isolated from failures in other Availability Zones. They provide inexpensive, low-latency network connectivity to other Availability Zones in the same AWS Region. Important. Each region is completely independent.

## Study

1. What is an AWS Availability Zone?
2. What is a Region?
3. What is an Edge Location?
4. Why would you choose one region over another? (e.g. eu-central-1 (Frankfurt) over us-west-2 (Oregon)).

### Used Sources

https://aws.amazon.com/about-aws/global-infrastructure/
https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/RegionsAndAZs.html
https://www.rackspace.com/blog/aws-101-regions-availability-zones


### Overcome challanges

### Results 

1. ### What is an AWS Availability Zone?

**An availability zone** is a logical data center in a region available for use by any AWS customer. Each zone in a region has redundant and separate power, networking and connectivity to reduce the likelihood of two zones failing simultaneously. A common misconception is that a single zone equals a single data center.
Amazon Web Services (AWS) operates 2 regions and 6 availability zones.

2. ### What is a Region?

Each **Region** is a separate geographic area. Availability Zones are multiple, isolated locations within each Region
An AWS Region is a geographical location with a collection of availability zones mapped to physical data centers in that region. Every region is physically isolated from and independent of every other region in terms of location, power, water supply, etc. This level of isolation is critical for workloads with compliance and data sovereignty requirements where guarantees must be made that user data does not leave a particular geographic region. The presence of AWS regions worldwide is also important for workloads that are latency-sensitive and need to be located near users in a particular geographic area. Inside each region, you will find two or more availability zones with each zone hosted in separate data centers from another zone.


3. ### What is an Edge Location?

**Edge locations** are AWS data centers designed to deliver services with the lowest latency possible.
Amazon has dozens of these data centers spread across the world. They’re closer to users than Regions or Availability Zones, often in major cities, so responses can be fast and snappy. A subset of services for which latency really matters use edge locations, including:

* CloudFront, which uses edge locations to cache copies of the content that it serves, so the content is closer to users and can be delivered to them faster.
* Route 53, which serves DNS responses from edge locations, so that DNS queries that originate nearby can resolve faster.
* Web Application Firewall and AWS Shield, which filter traffic in edge locations to stop unwanted traffic as soon as possible.


4. ### Why would you choose one region over another?

**There are four main factors that play into evaluating each AWS Region for a workload deployment:** 

* Compliance. If your workload contains data that is bound by local regulations, then selecting the Region that complies with the regulation overrides other evaluation factors. This applies to workloads that are bound by data residency laws where choosing an AWS Region located in that country is mandatory.
* Latency. A major factor to consider for user experience is latency. Reduced network latency can make substantial impact on enhancing the user experience. Choosing an AWS Region with close proximity to your user base location can achieve lower network latency. It can also increase communication quality, given that network packets have fewer exchange points to travel through.
* Cost. AWS services are priced differently from one Region to another. Some Regions have lower cost than others, which can result in a cost reduction for the same deployment.
* Services and features. Newer services and features are deployed to Regions gradually. Although all AWS Regions have the same service level agreement (SLA), some larger Regions are usually first to offer newer services, features, and software releases. Smaller Regions may not get these services or features in time for you to use them to support your workload.