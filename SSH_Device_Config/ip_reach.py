import sys
import subprocess

def ip_reach(ip_list):

    for ip in ip_list:

        echo_reply = subprocess.run(['ping', 'c', '3', ip], stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL)

        # Echo reply icmp type is 0 and request is 8. refer icmp rfc for queries.
        if echo_reply.returncode == 0:
            print(f"Ip is reachable {ip}")
            continue
        else:
            print(f"Ip not reachable check connectivity to {ip}")
            sys.exit()

# test = ip_reach([])

# ip = "192.168.0.107"

# test = subprocess.run(['ping', '-c', '3', ip], stderr= subprocess.DEVNULL, stdout=subprocess.DEVNULL)
# print(test.returncode)
