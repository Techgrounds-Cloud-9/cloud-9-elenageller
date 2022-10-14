# Asymmetric encryption

The previous assignment introduced you to cryptography and symmetric encryption. In the previous exercise, you shared your encryption key with the recipient of your message. This means that anyone who has the key can decrypt the message.

Asymmetric encryption solves this issue. Instead of 1 key, you get 2: A public key, and a private key.


## Key terminology

* Asymmetric encryption uses a mathematically related pair of keys for encryption and decryption: a public key and a private key. If the public key is used for encryption, then the related private key is used for decryption. If the private key is used for encryption, then the related public key is used for decryption.

* The most well-known example of Asymmetric Encryption is **the Digital Signature Algorithm (DSA).** Developed by National Institute of Standards and Technology (NIST) in 1991, DSA is used for digital signature and its verification.

* The Diffie-Hellman algorithm will be used to establish a secure communication channel. This channel is used by the systems to exchange a private key. This private key is then used to do symmetric encryption between the two systems.

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-05-01.png)

**Difference Between Symmetric and Asymmetric Encryption**

Symmetric encryption uses a single key that needs to be shared among the people who need to receive the message while asymmetric encryption uses a pair of public key and a private key to encrypt and decrypt messages when communicating.

* The RSA algorithm (Rivest-Shamir-Adleman) is the basis of a cryptosystem -- a suite of cryptographic algorithms that are used for specific security services or purposes.

## Exercise

* Generate a key pair.
* Send an asymmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key you share with them. The recipient should be able to read the message, but it should remain a secret to everyone else.
* You are not allowed to use any private messages or other communication channels besides Slack. Analyse the difference between this method and symmetric encryption.




### Sources

https://www.ssl2buy.com/wiki/symmetric-vs-asymmetric-encryption-what-are-differences
https://cheapsslsecurity.com/blog/what-is-asymmetric-encryption-understand-with-simple-examples/
https://www.youtube.com/watch?v=Pq8gNbvfaoM
https://www.sciencedirect.com/topics/computer-science/hellman-algorithm
https://www.devglan.com/online-tools/rsa-encryption-decryption



### Overcome challenges


### Results

Its ecatly the same outcome as Exercise 4, the only difference might be in Encryption, instead of AES use RSA encryption method. The generate a Public and Private key, share the public key for encryption by other peer, and decryprt it with the private key which was simultaneously generated with Public key.

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-05-02.png)


![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-05-03.png)





