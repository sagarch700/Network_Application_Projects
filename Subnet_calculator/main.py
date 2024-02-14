import sys
import random

def subnet_calculator():

    try:
        # Checking for the valid IPv4 addresses
        while True:

            ip_addr = input("please input the IPv4 address: ")
            ip_octets = ip_addr.split(".")
            if (len(ip_octets) == 4) and (1 <= int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and \
            (int(ip_octets[0]) != 169 or int(ip_octets[0]) != 254) and (0 <= int(ip_octets[1]) <= 255 and 0 <= int(ip_octets[2]) <= 255 and 0 <= int(ip_octets[3]) <= 255):
                break
            else:
                print(f"Please input correct ip address")

        masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]

        # Checking for the valid subnet mask
        while True:

            subnet_mask = input("Enter the subnet mask: ")
            mask_octets = subnet_mask.split(".")
            print(mask_octets)
            if (len(mask_octets) == 4) and (int(mask_octets[0]) == 255) and (int(mask_octets[1]) in masks) and (int(mask_octets[2]) in masks) and \
             (int(mask_octets[3]) in masks) and (int(mask_octets[0]) >= int(mask_octets[1]) >= int(mask_octets[2]) >= int(mask_octets[3])):
                break
            else:
                print("The subnet mask is invalid, TRY AGAIN")
                continue
        
        # Converting the subnet mask to binary
        mask_octets_binary = []

        for octet in mask_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            # padding every subnet to 8 bits
            mask_octets_binary.append(binary_octet.zfill(8))
        
        binary_mask = "".join(mask_octets_binary)

        # counting number of hosts
        zeroes = binary_mask.count("0")
        hosts = abs(2 ** zeroes - 2)
        ones = 32 - zeroes

        # Calculating wild card octets
        wildcard_octets = []
        for octet in mask_octets:
            wild_octet = 255 - int(octet)
            wildcard_octets.append(str(wild_octet))
        wildcard_mask = ".".join(wildcard_octets)
        # print(wildcard_mask)

        ip_octets_binary = []
            
        for octet in ip_octets:
            binary_octet = bin(int(octet)).lstrip('0b')
            ip_octets_binary.append(binary_octet.zfill(8))
        
        binary_ip = "".join(ip_octets_binary)

        network_address_binary = binary_ip[:ones] + "0" * zeroes
        broadcast_address_binary = binary_ip[:ones] + "1" * zeroes

        net_ip_octets = []
            
            #range(0, 32, 8) means 0, 8, 16, 24
        for bit in range(0, 32, 8):
            net_ip_octet = network_address_binary[bit: bit + 8]
            net_ip_octets.append(net_ip_octet)
        
        # Converting each octet to decimal
        net_ip_address = []
            
        for each_octet in net_ip_octets:
            net_ip_address.append(str(int(each_octet, 2)))
        network_address = ".".join(net_ip_address)

        broadst_ip_octets = []

        for bit in range(0, 32, 8):
            broadcast_ip_octet = broadcast_address_binary[bit: bit + 8]
            broadst_ip_octets.append(broadcast_ip_octet)
        

        broadcast_ip_address = []
            
        for each_octet in broadst_ip_octets:
            broadcast_ip_address.append(str(int(each_octet, 2)))
                
            #print(bst_ip_address)
            
        broadcast_address = ".".join(broadcast_ip_address)

        print(f"Network address is: {network_address}")
        print(f"Broadcast address is: {broadcast_address}")
        print(f"no of valid hosts is: {hosts}")
        print(f"wildcard mask is: {wildcard_mask}")
        print(f"Mask bits: {ones}")

        while True:
            generate = input("generate random ip address from this subnet? (y/n): ")

            if generate == "y":
                generated_ip = []

                for indexb, oct_broadcast in enumerate(broadcast_ip_address):
                    #print(indexb, oct_bst)
                    for indexn, oct_net in enumerate(net_ip_address):
                        #print(indexn, oct_net)
                        if indexb == indexn:
                            if oct_broadcast == oct_net:
                                #Add identical octets to the generated_ip list
                                generated_ip.append(oct_broadcast)
                            else:
                                #Generate random number(s) from within octet intervals and append to the list
                                generated_ip.append(str(random.randint(int(oct_net), int(oct_broadcast))))
                
                random_ipaddr = ".".join(generated_ip)
                print(f"random ip address is: {random_ipaddr}")
                continue
            else:
                print("Existing, BYE!!")
                break
    
    except KeyboardInterrupt:
        print("Program aborted by user, Existing")
        sys.exit()

subnet_calculator()

                    

        