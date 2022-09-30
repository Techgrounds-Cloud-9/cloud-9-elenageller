# Cron Jobs


## Key terminology
The crontab command is used to view or edit the table of commands to be run by cron. Each user on your system can have a personal crontab. Crontab files are located in /var/spool/ (or a subdirectory such as /var/spool/cron/crontabs), but they are not intended to be edited directly

The df command (short for disk free), is used to display information related to file systems about total space and available space. If no file name is given, it displays the space available on all currently mounted file systems.

## Exercise
Create a Bash script that writes the current date and time to a file in your home directory.
Register the script in your crontab so that it runs every minute.
Create a script that writes available disk space to a log file in ‘/var/logs’. Use a cron job so that it runs weekly.


### Sources
https://www.baeldung.com/linux/create-crontab-script
https://stackoverflow.com/questions/4880290/how-do-i-create-a-crontab-through-a-script

### Overcome challenges
I need to do the reserach how to run a crontab so it runs every minute.

### Results

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/blob/main/00_includes/LNX08-1.png)

![Screenshot](https://github.com/Techgrounds-Cloud-9/cloud-9-elenageller/commit/fa43be8c1a988a63cc806a49ae9147c709b50ecf)