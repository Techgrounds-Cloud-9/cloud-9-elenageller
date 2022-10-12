# Passwords
 
Of course, these strategies make it harder to remember your own passwords. Password managers were created to solve this problem.
On the back-end, passwords need to be stored securely. If your database (or /etc/shadow file in Linux) gets leaked or stolen, you don’t want anyone to just be able to read passwords in plaintext. This is why most stored passwords are hashed. Hackers will try to use a Rainbow Table to crack hashed passwords.

## Key terminology

* A hash function is any function that can be used to map data of arbitrary size to fixed-size values. The values returned by a hash function are called hash values, hash codes, digests, or simply hashes. The values are usually used to index a fixed-size table called a hash table.
Hashing gives a more secure and adjustable method of retrieving data compared to any other data structure

* A rainbow table attack is a password cracking method that uses a special table (a “rainbow table”) to crack the password hashes in a database.

* Salting is a modern technique used to thwart rainbow table attacks. It involves adding an extra random value to every hashed password to create a different hash value. Most modern password authentication systems include salting, which has significantly lessened the number of successful rainbow table attacks. 

## Exercise

* Find out what hashing is and why it is preferred over symmetric encryption for storing passwords.
* Find out how a Rainbow Table can be used to crack hashed passwords.
* Below are two MD5 password hashes. One is a weak password, the other is a string of 16 randomly generated characters. Try to look up both hashes in a Rainbow Table.
03F6D7D1D9AAE7160C05F71CE485AD31
03D086C9B98F90D628F2D1BD84CFA6CA
* Create a new user in Linux with the password 12345. Look up the hash in a Rainbow Table.
* Despite the bad password, and the fact that Linux uses common hashing algorithms, you won’t get a match in the Rainbow Table. This is because the password is salted. 
* To understand how salting works, find a peer who has the same password in /etc/shadow, and compare hashes.

### Sources

https://www.geeksforgeeks.org/hashing-data-structure/
https://www.csoonline.com/article/3602698/hashing-explained-why-its-your-best-bet-to-protect-stored-passwords.html
https://www.beyondidentity.com/glossary/rainbow-table-attack
https://crackstation.net/

### Overcome challenges


### Results

1. Hashing is the process of transforming any given key or a string of characters into another value. This is usually represented by a shorter, fixed-length value or key that represents and makes it easier to find or employ the original string. 
Hashing is almost always preferable to encryption when storing passwords inside databases because in the event of a compromise attackers won't get access to the plaintext passwords and there's no reason for the website to ever know the user's plaintext password

2. Hackers must first gain access to leaked hashes in order to carry out rainbow table attacks. The password database itself might be poorly secured, or they may have gained access to the Active Directory. Others gain access through phishing techniques of those that might have access to the password database. On top of all these techniques, there are already millions and millions of leaked password hashes on the dark web that are available to hackers. 
Once they have the password hashes the rainbow table is used to help decrypt the password hashes. As long as the password hashes don't include a “salt,” (explained above) they’ll be able to translate the encrypted passwords into plaintext easily.

3. 
* Hash	                           Type	        Result
* 03F6D7D1D9AAE7160C05F71CE485AD31	md5 	   welldone!
* 03D086C9B98F90D628F2D1BD84CFA6CA	Unknown	   Not found.

4. 
![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/SECURITY/SEC-07-01.png)

The user was added with the weak password that is why the salt and hash is shown. 


