# Well Architected Framework

The way you set up your IT or your application, the architecture, is a big part of how your application runs, how secure it is, and how much it costs. To help design architectures, AWS has the Well Architected Framework (WAF, not to be confused with the Web Application Firewall).

WAF consists of six pillars, all with their own key concepts, design principles, and best practices. You should be able to name these pillars, as well as understand what they mean. You should also be able to think about architectures in the context of the Well Architected Framework.

The mnemonic device for the six pillars is CROPSS (the first letter of each pillar). The pillars are:
Cost optimization
Reliability
Operational Excellence
Performance efficiency
Security
Sustainability

AWS has them ordered as OSRPCS, but that’s a little harder to remember.


## Key terminology

* The AWS Well-Architected Framework describes key concepts, design principles, and architectural best practices for designing and running workloads in the cloud

## Study

The Well Architected Framework


### Used Sources

https://aws.amazon.com/blogs/apn/the-6-pillars-of-the-aws-well-architected-framework/
https://aws.amazon.com/architecture/well-architected/?wa-lens-whitepapers.sort-by=item.additionalFields.sortDate&wa-lens-whitepapers.sort-order=desc&wa-guidance-whitepapers.sort-by=item.additionalFields.sortDate&wa-guidance-whitepapers.sort-order=desc

## Result

1. Operational Excellence

The Operational Excellence pillar includes the ability to support development and run workloads effectively, gain insight into their operation, and continuously improve supporting processes and procedures to delivery business value. 

**5 Design Principles**

* Perform operations as code
* Make frequent, small, reversible changes
* Refine operations procedures frequently
* Anticipate failure
* Learn from all operational failures

2. Security

The Security pillar includes the ability to protect data, systems, and assets to take advantage of cloud technologies to improve your security.

**7 Design Principles**

* Implement a strong identity foundation
* Enable traceability
* Apply security at all layers
* Automate security best practices
* Protect data in transit and at rest
* Keep people away from data
* Prepare for security events

3. Reliability

The Reliability pillar encompasses the ability of a workload to perform its intended function correctly and consistently when it’s expected to. This includes the ability to operate and test the workload through its total lifecycle. 

**5 Design Principles**

* Automatically recover from failure
* Test recovery procedures
* Scale horizontally to increase aggregate workload availability
* Stop guessing capacity
* Manage change in automation

4. Performance Efficiency

The Performance Efficiency pillar includes the ability to use computing resources efficiently to meet system requirements, and to maintain that efficiency as demand changes and technologies evolve.

**5 Design Principles** 

* Democratize advanced technologies
* Go global in minutes
* Use serverless architectures
* Experiment more often
* Consider mechanical sympathy

5. Cost Optimization

The Cost Optimization pillar includes the ability to run systems to deliver business value at the lowest price point. 

**5 Design Principles** 

* Implement cloud financial management
* Adopt a consumption model
* Measure overall efficiency
* Stop spending money on undifferentiated heavy lifting
* Analyze and attribute expenditure

6. Sustainability

The discipline of sustainability addresses the long-term environmental, economic, and societal impact of your business activities.

**6 Design Principles**

* Understand your impact
* Establish sustainability goals
* Maximize utilization
* Anticipate and adopt new, more efficient hardware and software offerings
* Use managed services
* Reduce the downstream impact of your cloud workloads
