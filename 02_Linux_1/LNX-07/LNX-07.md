# Bash scripting (Bourne Again Shell)


## Key terminology
PATH is an environmental variable in Linux and other Unix-like operating systems that tells the shell which directories to search for executable files (i.e., ready-to-run programs) in response to commands issued by a user.
A command script is simply a file, which contains a set of normal linux commands that the command shell will perform automatically in the given order.
httpd is the Apache HyperText Transfer Protocol (HTTP) server program. It is designed to be run as a standalone daemon process. When used like this it will create a pool of child processes or threads to handle requests.
Bash is a Unix shell and command language.

## Exercise 1
Create a directory called ‘scripts’. Place all the scripts you make in this directory.
Add the scripts directory to the PATH variable.
Create a script that appends a line of text to a text file whenever it is executed.
Create a script that installs the httpd package, activates httpd, and enables httpd. Finally, your script should print the status of httpd in the terminal.

## Variables
You can assign a value to a string of characters so that the value can be read somewhere else in the script.
Assigning a variable is done using ‘=’.
Reading the value of a variable is done using ‘$<insert variable name here>’.



## Exercise 2
Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file.

## Condition
You can choose to only run parts of your script if a certain condition is met. For example, only read a file if the file exists, or only write to a log if the health check returns an error. This can be done using conditions.

A check for a condition can be done using ‘if’, ‘elif’, and/or ‘else’.

## Exercise 3
Create a script that generates a random number between 1 and 10, stores it in a variable, and then appends the number to a text file only if the number is bigger than 5. If the number is 5 or smaller, it should append a line of text to that same text file instead.

### Sources

https://linuxize.com/post/how-to-add-directory-to-path-in-linux/
https://www.linuxjournal.com/content/how-create-shell-script-linux
https://medium.com/@ertorrez/use-a-script-to-install-and-launch-an-apache-server-on-centos-8-6db6e4b81cbf
https://stackoverflow.com/questions/8988824/generating-random-number-between-1-and-10-in-bash-shell-script
https://blog.eduonix.com/shell-scripting/generating-random-numbers-in-linux-shell-scripting/

### Overcome challenges
I had to read about PATH to iunderstand how it works, then install Apache2 and understand how to use bash language syntax, which is pretty similar to java I think.

### Results
P
![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/LNX-07-1.png)
![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/LNX-07-2.png)
![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/LNX07-3.png)
![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/LNX07-4.png)
![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/LNX07-5.png)
