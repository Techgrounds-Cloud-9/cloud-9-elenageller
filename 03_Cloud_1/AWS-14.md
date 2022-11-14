# Files,AppServices,CDN,DNS,Database



## Key terminology

* Trusted Advisor inspects your AWS environment, and then makes recommendations when opportunities exist to save money, improve system availability and performance, or help close security gaps.

* AWS Simple Monthly Calculator: Calculates the cost of your entire AWS infrastructure to get a monthly bill

* Total Cost of Ownership (TCO) Calculator: Compares total cost of running your infrastructure on-premise VS on AWS

* AWS Cost Explorer: Analyze cost and usage data to identify trends, cost drivers, and detect anomalies

* Consolidated Billing allows one Paying Account to receive bills from multiple Linked Accounts to receive one monthly bill for everything in the company’s AWS environments. The service itself is free.

* CloudWatch dynamically monitors and can react to changes/triggers.  Need to know how much CPU an EC2 instance is using? CloudWatch.

* CloudTrail is audit logs.  Need to know how someone got into an app? CloudTrail for access logs.

* AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet. Chef and Puppet are automation platforms that allow you to use code to automate the configurations of your servers.

* Amazon Elastic Container Service (ECS) is a highly scalable, high performance container management service that supports Docker containers and allows you to easily run applications on a managed cluster of Amazon Elastic Compute Cloud (Amazon EC2) instances. Amazon ECS eliminates the need for you to install, operate, and scale your own cluster management infrastructure.

* AWS Config is a fully managed service that provides you with an AWS resource inventory, configuration history, and configuration change notifications to enable security and governance.

* The main purpose of SQS is to facilitate decoupling of applications and to enable asynchronous communication between services. SQS allows developers to publish messages to a Queue, that the consuming application can process either immediately or at a later time.


## Study

AWS Support Plans
Trusted Advisor
AWS Config
AWS Cloud Trail
ECS

## Practical:

IAM
AWS Cloudwatch
DynamoDB
AWS Lambda
SNS, SQS, Event Bridge

**Questions for practical research:**
Where can I find this service in the console?
How do I turn on this service?
How can I link this service to other resources?

### Used Sources

https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html
https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html
https://aws.amazon.com/ecs/ 


### Overcome challanges

### Results 

1. **AWS Support Plans**

There are 5 tiers to AWS Support Plans: Basic, Developer, Business, and  Enterprise On-Ramp, Enterprise.

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week3/aws14-01.png)

2. Trusted Advisor: optimize infrastructure (performance, cost optimization, security, fault tolerance)

* If you have a Basic or Developer Support plan, you can use the Trusted Advisor console to access all checks in the Service Limits category and six checks in the Security category.

* If you have a Business, Enterprise On-Ramp, or Enterprise Support plan, you can use the Trusted Advisor console and the AWS Support API to access all Trusted Advisor checks. You also can use Amazon CloudWatch Events to monitor the status of Trusted Advisor checks.

3. Config is focused on the configuration of your AWS resources and reports with detailed snapshots on how your resources have changed. CloudTrail focuses on the events, or API calls, that drive those changes. It focuses on the user, application, and activity performed on the system

4. Amazon CloudWatch metrics is a monitoring service which provides data about the usage of your systems, including the ability to search, graph, and build alarms on metrics about AWS resources. With this release, you can now use Amazon CloudWatch metrics to verify your setup and understand your usage of AWS Config.

5. AWS CloudTrail enables auditing, security monitoring, and operational troubleshooting by tracking user activity and API usage. CloudTrail logs, continuously monitors, and retains account activity related to actions across your AWS infrastructure, giving you control over storage, analysis, and remediation actions.

6. Three of the most useful messaging patterns for serverless developers are queues, publish/subscribe, and event buses. In AWS, these are provided by Amazon SQS, Amazon SNS, and Amazon EventBridge respectively. All of these services are fully managed and highly available, so there is no infrastructure to manage. All three integrate with Lambda, allowing you to publish messages via the AWS SDK and invoke functions as targets. Each of these services has an important role to play in serverless architectures.

SNS enables you to send messages reliably between parts of your infrastructure. It uses a robust retry mechanism for when downstream targets are unavailable. When the delivery policy is exhausted, it can optionally send those messages to a dead-letter queue for further processing. SNS uses topics to logically separate messages into channels, and your Lambda functions interact with these topics.

SQS provides queues for your serverless applications. You can use a queue to send, store, and receive messages between different services in your workload. Queues are an important mechanism for providing fault tolerance in distributed systems, and help decouple different parts of your application. SQS scales elastically, and there is no limit to the number of messages per queue. The service durably persists messages until they are processed by a downstream consumer.

EventBridge is a serverless event bus service, simplifying routing events between AWS services, software as a service (SaaS) providers, and your own applications. It logically separates routing using event buses, and you implement the routing logic using rules. You can filter and transform incoming messages at the service level, and route events to multiple targets, including Lambda functions.


