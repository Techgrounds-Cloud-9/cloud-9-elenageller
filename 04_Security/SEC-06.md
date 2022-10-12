# Public Key Infrastructure
 
Public Key Infrastructure (PKI) is a set of roles, policies, hardware, software and procedures needed to create, manage, distribute, use, store and revoke digital certificates and manage public-key encryption.
It consists of three entities that assure you can communicate securely over an insecure network like the public internet.
X.509 is the standard which defines the process in which a PKI should function. There are many ways of implementing a PKI, not all of them comply with the X.509 standard.

## Key terminology

* The Public key infrastructure (PKI) is the set of hardware, software, policies, processes, and procedures required to create, manage, distribute, use, store, and revoke digital certificates and public-keys.

* **Today, asymmetric encryption powers things like:** 

SSH algorithms 
SSL/TLS 
S/MIME encrypted email 
Code signing 
Bitcoin/Blockchain 
Signal private messenger 
Digital signatures
Most notably, asymmetric encryption powers PKI. 

* PKI governs encryption keys by issuing and managing **digital certificates.** Digital certificates are also called **X.509 certificates and PKI certificates.**

* A public key certificate, also known as a digital certificate or identity certificate, is an electronic document used to prove the validity of a public key.

* Certification authorities. One of the key components of any PKI architecture is a certification authority, or what’s more commonly called a certificate authority or CA. An organization can rely on one or more CAs within its PKI.

![Screenshot]()

* Public PKI (Public CA) — This term refers to a PKI that issues certificates that are automatically trusted by most browsers and devices. For example, if you purchase an SSL certificate from The SSL Store, that certificate is issued by a public CA. This is the most commonly used type of PKI.

* Private PKI (Private CA) — This refers to PKI that is only used to secure your internal network. The certificates won’t be automatically trusted on all devices — you’ll need to install the appropriate root certificate on each device first. The plus side is that you have a lot more control over the certificates you issue. Private PKI can be set up via tools like Microsoft CA or via managed PKI services (aka mPKI or PKI as a service).

![Screenshot]()

* Registration Authority (RA):
Which is authorized by the Certificate Authority to provide digital certificates to users on a case-by-case basis. All of the certificates that are requested, received, and revoked by both the Certificate Authority and the Registration Authority are stored in an encrypted certificate database.

## Exercise

1. Create a self-signed certificate on your VM.
2. Analyze some certification paths of known websites (ex. techgrounds.nl / google.com / ing.nl).
3. Find the list of trusted certificate roots on your system (bonus points if you also find it in your VM).

### Sources

https://www.keyfactor.com/resources/what-is-pki/
https://www.youtube.com/watch?v=Jefr7wFLu3M
https://www.thesslstore.com/blog/pki-architecture-fundamentals-of-designing-a-private-pki-system/
https://linuxize.com/post/creating-a-self-signed-ssl-certificate/ 

### Overcome challenges


### Results


![Screenshot]()


![Screenshot]()


![Screenshot]()

![Screenshot]()

![Screenshot]()

![Screenshot]()
