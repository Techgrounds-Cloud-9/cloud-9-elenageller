# Simple Storage Service (S3)

* AWS offers object based storage in the form of S3. S3 makes use of buckets as a container for objects. A single object in S3 has a maximum size of 5TB. However, the total size of a bucket is virtually unlimited.
* Bucket names must be globally unique. That is, even other AWS accounts in different regions cannot share the same bucket name. Buckets, and objects within buckets, can be accessed using a URL.
* The bucket policy acts as an access control list. Data can be encrypted for even further protection.
* Objects are automatically replicated within a region, so that there’s always at least three copies available. This redundancy greatly increases the availability and durability of objects stored in S3.

**There are 4 storage classes:**
1. S3 Standard — The default storage class. If you don't specify the storage class when you upload an object, Amazon S3 assigns the S3 Standard storage class.

2. Reduced Redundancy — The Reduced Redundancy Storage (RRS) storage class is designed for noncritical, reproducible data that can be stored with less redundancy than the S3 Standard storage class.
**Storage classes differ in availability, durability, retrieval time, and cost.**

**In S3, you pay for:**
GBs storage per month
Transfer OUT to out of the region
PUT, COPY, POST, LIST, and GET requests
You don’t pay for:
Transfer IN to Amazon S3
Transfer OUT from S3 to CloudFront or EC2 in the same region

* Besides storing data for all kinds of purposes (big data, storing videos, archiving, etc.), S3 has another use case: hosting static websites.


## Key terminology


## Exercise

**Requirements**

Your AWS environment
A cat picture (jpg or png)
AWS’ demo website (index.html, script.js, style.css; can be found in the Google Drive)
A peer

**Exercise 1**

Create new S3 bucket with the following requirements: Region: Frankfurt (eu-central-1)
Upload a cat picture to your bucket.
Share the object URL of your cat picture with a peer. Make sure they are able to see the picture.

**Exercise 2**

Create new bucket with the following requirements: Region: Frankfurt (eu-central-1)
Upload the four files that make up AWS’ demo website.
Enable static website hosting.
Share the bucket website endpoint with a peer. Make sure they are able to see the website.

### Used Sources

https://aws.amazon.com/s3/storage-classes/

**Exercise 1** 
https://www.youtube.com/watch?v=i2JXvgHsV9w

**Exercise 2** 

https://www.youtube.com/watch?v=-mIANj3lBFk

### Overcome challanges

none

### Results 

**Exercise 1** 

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week1/aws05-01-1.png) 

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week1/aws05-01-2.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week1/aws05-01-3.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week1/aws05-01-4.png)

**Exercise 2** 

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week1/aws05-02-1.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week1/AWS05-02-2.png)

