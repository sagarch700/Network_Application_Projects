import sys


def ip_addr_valid(ip_list):
    
    for ip in ip_list:
        octet_list = ip.split(".")

        if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and \
        (int(octet_list[0]) != 169 or int(octet_list[0]) != 169) and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
            continue
        else:
            print(f"There was an invalid IP address entry in the file: {ip}")


# test = ip_addr_valid(["10.10.10.1", "10.10.10.2", "127.10.10.3"])
# print(test)


