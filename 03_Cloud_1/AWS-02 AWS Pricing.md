# AWS Pricing

There are three fundamental drivers of cost with AWS: compute, storage, and outbound data transfer.

## Key terminology

* The Total Cost of Ownership (TCO) is used to measure how much an infrastructure would cost if it were hosted the traditional way.
* This is done by measuring capital expenditures (capex). The cloud pricing model allows you to trade capex for variable expenditure. This can reduce cost by not spending money on capacity you don’t need.
## Exercise

1. The four advantages of the AWS pricing model.
2. AWS free tier for:
S3
EC2
Always free services
3. Understand the differences between capex and opex

### Used Sources

https://aws.amazon.com/pricing/?aws-products-pricing.sort-by=item.additionalFields.productNameLowercase&aws-products-pricing.sort-order=asc&awsf.Free%20Tier%20Type=*all&awsf.tech-category=*all
https://aws.amazon.com/free/registration-faqs/

### Results 

1. AWS lists four advantages of their pricing model:
* Pay-as-you-go allows you to easily adapt to changing business needs without overcommitting budgets and improving your responsiveness to changes
* Save when you commit. For AWS Compute and AWS Machine Learning, Savings Plans offer savings over On-Demand in exchange for a commitment to use a specific amount (measured in $/hour) of an AWS service or a category of services, for a one- or three-year period.
* Pay less by using more. With AWS, you can get volume based discounts and realize important savings as your usage increases. For services such as S3, pricing is tiered, meaning the more you use, the less you pay per GB. AWS also gives you options to acquire services that help you address your business needs.
* Benefit from massive economies of scale

2. AWS free tier for:
* S3 - new AWS customers receive 5GB of Amazon S3 storage in the S3 Standard storage class; 20,000 GET Requests; 2,000 PUT, COPY, POST, or LIST Requests; and 100 GB of Data Transfer Out each month.
* EC2 - This includes 750 hours of Linux and Windows t2.micro instances (t3.micro for the regions in which t2.micro is unavailable), each month for one year. To stay within the Free Tier, use only EC2 Micro instances.
* Some of the services like Amazon EC2, Amazon Cloudfront, Amazon S3 are free for a 12 month period, some like Amazom DynamoDB, Amazon Chime are always free, and others like Amazon Redshift, Amazon Lightsail have short term free trials, typically 30-60 days.