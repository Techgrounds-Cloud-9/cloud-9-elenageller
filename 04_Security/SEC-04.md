# Symmetric encryption
 
Encryption is an important tool for securing data. Be it data at rest, or data in motion. A lot of what you do on your computer and the Internet is encrypted.

## Key terminology

* Ciphers are algorithms, more specifically they’re a set of steps for performing a cryptographic function – it can be encryption, decryption, hashing or digital signatures.

* Symmetric encryption uses a single key to encrypt and decrypt. 

* Symmetric encryption ciphers consist of two main categories: block ciphers and stream ciphers.
**Encrypting information in chunks.** A block cipher breaks down plaintext messages into fixed-size blocks before converting them into ciphertext using a key.
**Encrypting information bit-by-bit.** A stream cipher, on the other hand, breaks a plaintext message down into single bits, which then are converted individually into ciphertext using key bits.

* AES is a symmetric type of encryption, as it uses the same key to both encrypt and decrypt data

* Cipher suites are sets of instructions that enable secure network connections through **Transport Layer Security (TLS)**, often still referred to as **Secure Sockets Layer (SSL)**. 

## Exercise

1. Find two more historic ciphers besides the Caesar cipher.
2. Find two digital ciphers that are being used today.
3. Send a symmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key you share with them. Try to think of a way to share this encryption key without revealing it to everyone. 
(You are not allowed to use any private messages or other communication channels besides Slack. Analyse the shortcomings of this method.)


### Sources

https://interestingengineering.com/innovation/11-cryptographic-methods-that-marked-history-from-the-caesar-cipher-to-enigma-code-and-beyond
https://sectigostore.com/blog/what-is-an-ssl-tls-cipher-suite/
https://www.youtube.com/watch?v=HMoFvRK4HUo
https://www.simplilearn.com/tutorials/cryptography-tutorial/symmetric-encryption#why_is_symmetric_key_cryptography_called_private_key_cryptography
https://www.thesslstore.com/blog/block-cipher-vs-stream-cipher/ 
https://www.practicalnetworking.net/series/cryptography/diffie-hellman/
https://www.comparitech.com/blog/information-security/what-is-aes-encryption/

### Overcome challenges

to find out the right step for encryption and dycription. 
My explanation is below in results section.

### Results

1. Another 2 Ciphers: 
* Scytale Was A Simple Cipher Used By The Spartans
* The Pigpen Cipher Was Used by The Masons

2. **Two digital ciphers that are being used today**

* Steam ciphers:
SSL/TLS connections
Bluetooth connections
Cellular and 4G connections

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-04-02.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-04-01.png)

* Block ciphers
Data Encryption Standard (DES)
Triple DES (3DES or TDEA)
Advanced Encryption Standard (AES)
International Data Encryption Algorithm (IDEA)
Blowfish
Twofish
RC5

**2 digital ciphers that are being used today: AES and RSA**

1. RSA is a public-key cryptosystem that is widely used for secure data transmission. It is also one of the oldest. 

2. AES is implemented in software and hardware throughout the world to encrypt sensitive data. It is essential for government computer security, cybersecurity and electronic data protection.



3. Symmetric keys can be exchanged safely between two systems when encrypted using an RSA public key. Sending system and receiving system do not need to share a secret key to be able to exchange RSA-encrypted symmetric keys.

* First I encrypted my message with AES encryption (https://www.devglan.com/online-tools/aes-encryption-decryption)


![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-04-03.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-04-04.png)

* Then I generate RSA public key (https://www.devglan.com/online-tools/rsa-encryption-decryption). This key we can be shared with our peer publicly for futher usage.

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-04-05.png)

* Then I need to encypt my secret key using Public key generated earlier.

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-04-06.png)

* Next step is decrypting message by RSA decryption by entering decrypted text in previous step/ or the decrypted text shared by peer which was decrypted by using RSA public key provided earlier by me. 

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-04-07.png)

I am using my Private key which was generated together with Public key which I sent it over into public chanel to be used for decryprion of secret key.

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-04-10.png)

* That is how I have a secret key which was used to decyrpt AES message, using this key I decrypted the encypted message.

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-04-08.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-04-09.png)


**Conclusion: In order to do that, one of the peers must first Share a decrypted message in AES and decrypted secret key (RSA) in public chanel. From another peer was required to provide a Publi key, which was used to decreyp a secret key in previous step by using his Private key which was generated simultaneously with Public key for another peer**
