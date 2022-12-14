# Elastic Block Store (EBS)

* EBS can be seen as virtual hard drives in the cloud. They can be either root volumes (like an internal hard disk), or seperate volumes (like an external hard disk). One instance of an EBS is called a volume. One volume can usually only be attached to one EC2 instance at a time, although for every non-root volume, you can detach it and attach it to a different EC2 instance. EBS Multi-Attach is only available in specific cases.

* You can create snapshots of a volume to create backups or new identical volumes. These snapshots will be stored in S3.
There are four different volume types. Generally speaking, lower performance means lower cost, but newer generations or specialized hardware might give better performance for lower costs.

* For security, EBS volumes can be encrypted. Volumes can be scaled up, but not down.

* Any external device, including EBS, needs to be mounted if you want to use them in Linux.

## Key terminology


## Exercise 1

Navigate to the EC2 menu.
Create a t2.micro Amazon Linux 2 machine with all the default settings.
Create a new EBS volume with the following requirements:
Volume type: General Purpose SSD (gp3)
Size: 1 GiB
Availability Zone: same as your EC2
Wait for its state to be available.

## Exercise 2

Attach your new EBS volume to your EC2 instance.
Connect to your EC2 instance using SSH.
Mount the EBS volume on your instance.
Create a text file and write it to the mounted EBS volume.

## Exercise 3
Create a snapshot of your EBS volume.
Remove the text file from your original EBS volume.
Create a new volume using your snapshot.
Detach your original EBS volume.
Attach the new volume to your EC2 and mount it.
Find your text file on the new EBS volum

### Used Sources

https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-creating-volume.html
https://devopscube.com/mount-ebs-volume-ec2-instance/
https://www.shellhacks.com/sudo-echo-to-file-permission-denied/ 

### Overcome challanges

I could not creat a text file with Echo command and >, after googling this issue, I found out that there is another command works for me.

### Results 

### Exercise 1

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week1/aws07-01-1.png)


![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week1/aws07-01-2.png)


![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week1/aws07-01-3.png)

### Exercise 2

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week1/aws07-02-3.png)

### Exercise 3

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week1/aws07-03-1.png)


![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week1/aws07-03-2.png)


![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week1/aws07-03-3.png)


![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week1/aws07-03-4.png)


![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/AWS%20week1/aws07-03-5.png)