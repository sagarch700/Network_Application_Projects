import paramiko
import os
import sys
import time
import re

username = os.getenv('username')
pasword = os.getenv('password')

def ssh_connection(ip):
    
    try:
        session = paramiko.SSHClient()
        session.connect(ip, username= username, password= pasword)
        connection = session.invoke_shell()
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)
        connection.send("conf t\n")
        time.sleep(1)

        with open("cmd.txt", "r") as file:
            commands = file.readlines()
        
        for command in commands:
            connection.send(command)
            time.sleep(2)

        router_output = connection.recv(65535)

        if re.search(b"% Invalid input", router_output):
            print(f"IOS syntax error {ip}")
        else:
            print(f"done for device {ip}")
        
        print(str(router_output) + "\n")
        session.close()
        
    except paramiko.AuthenticationException:
        print(f"invalid username or password check again")
        print(f"closing program bye!!")


