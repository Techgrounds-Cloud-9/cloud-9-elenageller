# Users and groups


## Key terminology
root - is the superuser account in Unix and Linux
sudo - allows you to run programs with the security privileges of another user (by default, as the superuser). It prompts you for your personal password and confirms your request to execute a command by checking a file, called sudoers , which the system administrator configures.
useradd - is command to add new user
usermod - is used to modify existing user account details, such as username, password, home directory location, default shell, and more.


## Exercise
Create a new user in your VM. 
The new user should be part of an admin group.
The new user should have a password.
The new user should be able to use ‘sudo’
Locate the files that store users, passwords, and groups. See if you can find your newly created user’s data in there.



### Sources

https://www.freecodecamp.org/news/linux-how-to-add-users-and-create-users-with-useradd/
https://www.cyberciti.biz/faq/where-are-the-passwords-of-the-users-located-in-linux/#:~:text=The%20%2Fetc%2Fpasswd%20is%20the,is%20one%20entry%20per%20line.



### Overcome challenges
where are the passwords of the users located. 

### Results

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/LNX-04-1.png)
![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/LNX-04-2.png)
![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/LNX-04-3.png)


