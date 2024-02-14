import os.path
import sys

# ip_list = []

def ip_file_valid():

    ip_file = "ip_file.txt"

    if os.path.isfile(ip_file) == True:
        print(" Your IP File does exist")
    else:
        print("please input the correct path")
        sys.exit()

    with open(ip_file, 'r') as file:
        ip_list = file.read().splitlines()
    
    return ip_list

# test = ip_file_valid()
# print(test)
        

