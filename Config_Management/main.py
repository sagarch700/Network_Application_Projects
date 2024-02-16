import difflib
import datetime
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from netmiko import ConnectHandler


# Test RFC1918 IP
ip = "10.10.10.10"

# Defining the device type for extracting running-config
device_type = "arista_eos"

# Getting the username and password stored in os env
username = os.getenv("username")
# print(username)
password = os.getenv("password")

# Command you want to run on your network device
command = "show running-config"

# connecting to device via ssh
session = ConnectHandler(device_type = device_type, ip = ip, username = username, password = password, global_delay_factor = 3)
enable = session.enable()
output = session.send_command(command)

# Comparing the previous day file for comparison
# Make sure to create the old_config file when you're running the code for the first time
old_config = "configfiles/routers/" + ip + "_" + (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
new_config = "configfiles/routers/" + ip + "_" + datetime.date.today().isoformat()

# writing the current running config to new_config file
with open (new_config, "w") as file:
    file.write(output + "\n")

# Extracting the differences b/w the yesterday's and today's config file
with open(old_config, "r") as old_file, open(new_config, "r") as new_file:
    differnce = difflib.HtmlDiff().make_file(fromlines=old_file.readlines(), tolines=new_file.readlines(), fromdesc="Yesterday", todesc="Today")

# Sending the differences via the email
# Declaring the sender and receiver email, using the same sender and receiver email for POC
sender_email = os.getenv("email")
recepient_email = os.getenv("email")

# Using MIME for emails with attachments and complex structres, here it is html
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recepient_email
message["Subject"] = "Daily Config management report"
message.attach(MIMEText(differnce, "html"))

smtp_username = sender_email
smtp_password = os.getenv("smtp_api_key")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=smtp_username, password=smtp_password)
    connection.send_message(message)

'''
    To run this code everyday at 6 AM :- pick a time where you think there will less changes from that time to your shift
    issue linux commands:
        sudo crontab -e
        0 6 * * *  cd /home/users && sudo python3 Config_Management/main.py
        ctrl + o to save
        exit crontab
        chmod 7555 /home/users/Config_Management/main.py
        sudo crontab -l --> to list out all scheduled cronjobs
'''
'''
    Now to delete these config management files after every month, create a below script and an cronjob
    vim delete_config_management_files_monthly.sh
        #!/bin/bash

        PATH_DIR="/home/users/configfiles/routers
        # This delets all the files in that directory whose last modification date is more than 30 days.
        find "${PATH_DIR}" -f -mtime +30 -delete
        :wq
    chmod +x /home/users/Config_Management/delete_config_management_files_monthly.sh
    crontab -e
        0 0 1 * * /home/users/Config_Management/delete_config_management_files_monthly.sh
        ctrl + o save and exit
'''



