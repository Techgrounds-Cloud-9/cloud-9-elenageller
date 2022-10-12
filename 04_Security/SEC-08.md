# Detection, response and analysis
 
Detecting an (attempted) attack is the first step to stopping it and to preventing future attempts. Tools like Wireshark can help analyse a network to detect anomalies. Intrusion detection systems (IDS) and intrusion prevention systems (IPS) are also used for this purpose.

## Key terminology

* IPS - Intrusion Prevention System is also known as Intrusion Detection and Prevention System

* IDS - An Intrusion Detection System (IDS) is a network security technology originally built for detecting vulnerability exploits against a target application or computer.

* Malware - Malware (short for “malicious software”) is a file or code, typically delivered over a network, that infects, explores, steals or conducts virtually any behavior an attacker wants. 

* Social engineering is a manipulation technique that exploits human error to gain private information, access, or valuables. Social engineering attacks are a type of cybercrime wherein the attacker fools the target through impersonation.

* A disaster recovery plan is is an important part of a bigger business continuity plan. When a disaster strikes and infrastructure goes offline, a business could be done for. There are many strategies when it comes to mitigating a disaster. From just having a cold backup, to a redundant site.

* Recovery Point Objective; RPO)

* Recovery Time Objective (RTO) refers to the maximum acceptable length of time that can elapse before the lack of a business function severely impacts the organization. This is the maximum agreed time for the resumption of the critical business functions.

*  A SIEM system integrates outputs from multiple sources and uses alarm filtering techniques to differentiate malicious activity from false alarms.

## Exercise

**Study**
1. IDS and IPS.
2. Hack response strategies.
3. The concept of systems hardening.
4. Different types of disaster recovery options.


* A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?

* An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?


### Sources

https://www.geeksforgeeks.org/intrusion-detection-system-ids/
https://www.securitymetrics.com/blog/6-phases-incident-response-plan
https://www.beyondtrust.com/resources/glossary/systems-hardening#:~:text=Systems%20hardening%20is%20a%20collection,condensing%20the%20system's%20attack%20surface.
youtube.com/watch?v=B09dU3jEPzc
https://sados.com/blog/types-of-disaster-recovery-plans/
https://solutionsreview.com/backup-disaster-recovery/top-three-types-of-disaster-recovery-plans/
https://www.empowerit.com.au/blog/it-planning/different-types-disaster-recovery-plans/
https://www.bcmpedia.org/wiki/Recovery_Time_Objective_(RTO)


### Overcome challenges

### Results

* An Intrusion Detection System (IDS) is a system that monitors network traffic for suspicious activity and issues alerts when such activity is discovered. It is a software application that scans a network or a system for the harmful activity or policy breaching. Any malicious venture or violation is normally reported either to an administrator or collected centrally using a security information and event management (SIEM) system

**IDS Detection Types**

1. Network intrusion detection systems (NIDS): A system that analyzes incoming network traffic.
2. Host-based intrusion detection systems (HIDS): A system that monitors important operating system files.
3. Signature-based: Signature-based IDS detects possible threats by looking for specific patterns, such as byte sequences in network traffic, or known malicious instruction sequences used by malware.
4. Anomaly-based: a newer technology designed to detect and adapt to unknown attacks, primarily due to the explosion of malware.


* Intrusion Prevention System is also known as Intrusion Detection and Prevention System. It is a network security application that monitors network or system activities for malicious activity. Major functions of intrusion prevention systems are to identify malicious activity, collect information about this activity, report it and attempt to block or stop it. 

**Classification of Intrusion Prevention System (IPS)**

1. Network-based intrusion prevention system (NIPS): 
It monitors the entire network for suspicious traffic by analyzing protocol activity. 
 
2. Wireless intrusion prevention system (WIPS): 
It monitors a wireless network for suspicious traffic by analyzing wireless networking protocols. 
 
3. Network behavior analysis (NBA): 
It examines network traffic to identify threats that generate unusual traffic flows, such as distributed denial of service attacks, specific forms of malware and policy violations. 
 
4. Host-based intrusion prevention system (HIPS): 
It is an inbuilt software package which operates a single host for doubtful activity by scanning events that occur within that host. 

* **Hack response strategies**
1. Preparation
2. Identification
3. Containment
4. Eradication
5. Recovery
6. Lessons Learned


* Systems hardening is a collection of tools, techniques, and best practices to reduce vulnerability in technology applications, systems, infrastructure, firmware, and other areas. The goal of systems hardening is to reduce security risk by eliminating potential attack vector s and condensing the system’s attack surface. 


* **Major types of DR include:**
1. Data center disaster recovery.
 A Data Center DR plan focuses on the entire building where a business houses its servers. It’s more comprehensive than simply protecting computers. Physical security, support employees, backup power sources, HVAC, internet and electric providers, and fire prevention and suppression plans all impact a data center DR plan. When a natural disaster, cyberattack, or another type of outage occurs, all the previous elements must work together to protect data. A data center disaster recovery plan lowers the risk of cyberattacks, but a major natural disaster can still negatively impact data.
2. Backup-only disaster recovery plan
 The minimum service a reputable Managed Services Provider will offer to keep your business running is to back up your files daily. With backup-only plans, a backup technician will store copies of your files in at least three different locations; onsite, on a removable drive (like a USB drive), and in their secure data centres.
3. Virtualized disaster recovery. 
 Virtualization negates the need to reconstruct a physical server in the event of a disaster. You are also able to achieve your targeted recovery time objectives (RTO) more easily by placing a virtual server on reserve capacity or the cloud. 
4. Cloud Based disaster recovery. 
 When using a cloud-based approach, you’re able to cut costs by using a cloud provider’s data center as a recovery site, rather than spending more on your own data center’s facilities, personnel, and systems. Users also benefit from the competition between cloud providers, as they continue to attempt to best each other in the market.
5. Disaster recovery as a service (DRaaS)
 While Disaster Recovery as a Service (DRaaS) is often based in the cloud, it is not strictly cloud-based. Some DRaaS providers offer their solutions as a site-to-site service, in which they host and run a secondary hot site. Additionally, providers can rebuild and ship servers to an organization’s site as a server replacement service. On the other hand, cloud-based DRaaS enables users to failover applications immediately, orchestrate failback to rebuilt servers, and reconnect users through VPN or Remote Desktop Protocol
6. Cold site DR
 A cold site disaster recovery plan involves renting out space in a secondary facility where you can set up a temporary office in the event of a disaster. These facilities have the basic infrastructure required to get servers and data online in a pinch; including power, cooling, and network connectivity.
 7. Hot site DR
   Hot site disaster recovery plan is where an identical facility is set up in a remote location; fully equipped with systems preloaded with apps, data, and security software. At higher price points, these facilities even come with phones, tablets, and other equipment required to run your business.



* 1. RPO is your goal for the maximum amount of data the organization can tolerate losing. This parameter is measured in time: from the moment a failure occurs to your last valid data backup. In this example, company experiences a failure now and their last full data backup was 24 hours ago, the RPO is 24 hours. 
* RTO is the goal your organization sets for the maximum length of time it should take to restore normal operations following an outage or data loss.
SO in this example RTO is 15 min.

* 2. RTO is 8 min.