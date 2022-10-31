# The Shared Responsibility 

The Shared Responsibility Model is a cloud security framework that mandates the security obligations of cloud service providers and users to ensure accountability. In simple words, A cloud vendor provides various cloud services to its users. One provides the service, and the other uses it. Both vendor and user share some responsibilities, like the vendor is responsible for the service provided, and the user is responsible for the service usage.

## Key terminology

* 

## Study

1. The Shared Responsibility Model

### Used Sources

https://aws.amazon.com/blogs/industries/applying-the-aws-shared-responsibility-model-to-your-gxp-solution/
https://k21academy.com/amazon-web-services/aws-solutions-architect/aws-shared-responsibility-model/

### Overcome challanges

### Results 

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week2/aws09-01.png)

* AWS Responsibility: AWS is responsible for protecting the infrastructure that runs all the AWS services. In other words, AWS control, operate and manage the components from the host operating system and virtualization layer that is down to the physical layer in which the service operates.
* Customer Responsibility: The customer’s responsibility depends on the AWS service used and the configuration they need to perform to secure that service. In other words, customers need to manage the guest operating system, including security patches and application software. Also, they need to configure the AWS provided security controls like security groups, network access control and IAM (Identity and Access Management).

**Examples  of shared controls include:**

1. Patch Management – AWS is responsible for patching and fixing flaws within the infrastructure, but customers are responsible for patching their guest OS and applications.
2. Configuration Management – AWS maintains the configuration of its infrastructure devices, but a customer is responsible for configuring their own guest operating systems, databases, and applications.
3. Awareness & Training – AWS trains AWS employees, but a customer must train their own employees.