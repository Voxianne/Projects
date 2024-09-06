from scapy.all import *
import time
import os


###########################################################################################
def Clear_Screen():
    
    if os.name == "posix":
        _ = os.system('clear')
    else:
        _ = os.system('cls')



###########################################################################################

#Sniffing Filter
def Filters():   
    
    print("Please use this format to create your filter:")
    print("\n\n")
    print("(Protocols) and host (IPv4 Address) and port (port number)")
    print("--> Protocols: arp , tcp , udp , icmp, ip, ipv6")
    print("Example: tcp and icmp and host 192.168.254.255")    
    filter = input("")
    
    Clear_Screen()
    return filter.lower()

#Choice 1 --> Sniffing    
def Sniffing():
#Choice to use a filter or not!
    while 1:
        choice = input("Would you like to use a filter? [Y/N]")
        if choice.lower() == "y":
            filter = Filters()
            break
        elif choice.lower() == "n":
            filter = ''
            break
        else:
            print("Invalid input!\n")
            
#Choice to use count or not. 
    while 1:
        count_packet= input("Please give a count of packets you wish to find at most.if not, press 0:")
        if count_packet.isdigit() and count_packet >= '0':
            print("\n")
            count_packet = int(count_packet)
            break
        else:
            print("Invalid input!\n")
            
#Choice to use a certain iface
    iface = input("Please give me an specific internet interface.If not,please 0:")
    
#case 1: count is 0, iface not specified and filter is not set    
    if int(count_packet) == 0 and iface == '0' and filter == '':
        
        print("Process is about to start...\n")
        time.sleep(3)
        print("Please press Ctrl+C to stop the process...\n")
        pck = sniff(prn = lambda x: x.summary()) 

#case 2: count not 0 , iface not specified and no filter
    elif int(count_packet) != 0 and iface == '0' and filter == '':
        
        print("Process is about to start...\n")
        time.sleep(3)
        pck = sniff(count = int(count_packet),prn = lambda x: x.summary())

#case 3: count is zero, iface specified and filter not set, filter
    elif int(count_packet) == 0 and iface != '0' and filter == '':

        print("Process is about to start...\n")
        time.sleep(3)
        print("Please press Ctrl+C to stop the process...\n")
        pck = sniff(iface = iface,timeout = 10,prn = lambda x: x.summary)

        
#case 4: count is zero, iface not specified and filter set        
    elif count_packet == 0 and iface == '0' and filter != '':
        
        print("Process is about to start...\n")
        time.sleep(3)
        print("Please press Ctrl+C to stop the process...\n")

        pck = sniff(filter = filter,prn = lambda x: x.summary())

        
#case 5: count is zero, iface specified and filter set        
    elif count_packet == 0 and iface != '0' and filter != '':
        
        print("Process is about to start...\n")
        time.sleep(3)        
        print("Please press Ctrl+C to stop the process...\n")    
        pck = sniff(iface = iface,filter = filter,prn = lambda x: x.summary())


#case 6: count is not zero and iface is not specified and filter is set.
    elif count_packet != 0 and iface == '0' and filter != '':
        
        print("Process is about to start...\n")
        time.sleep(2)
        pck = sniff(count = int(count_packet),filter = filter,prn = lambda x: x.summary())
        
#case 7: count is not zero and iface is specified and filter is not set
    elif count_packet != 0 and iface != '0' and filter == '': 
        
        print("Process is about to start...\n")
        time.sleep(2)
        pck = sniff(count = int(count_packet), iface = iface,prn = lambda x: x.summary())
        
#case 8: count is not zero and iface is specified and filter is set.
    else:
        
        print("Process is about to start...\n")
        time.sleep(2)
        pck = sniff(count = int(count_packet),iface = iface , filter = filter,prn = lambda x: x.summary())   

#Choice to save sniffed packets in a .pcap file or not!
    while 1:
        choice = input("Would you like to save the recorded packets?[Y/N]")
        if choice.lower() == "y":
            name = input("Please name the .pcap file...: ")
            print("Creating " + name + ".pcap...")    
            name = name + ".pcap"      
            time.sleep(2)
            wrpcap(name, pck)
            break
        elif choice.lower() == "n":
            break
        else:
            print("Invalid input!\n")

    

##############################################################################################

#Choice 2 --> Create_Send_Recieve 
def Create_Send_Recieve():
    
    Clear_Screen()
    Clear_Screen()
    packet_created = ''
    
    print("Please choose one of these layers to use:")
    print("\n\n")
    print("-->[1] IP()\n")
    print("-->[2] TCP()\n")
    print("-->[3] UDP()\n")
    print("-->[4] ICMP()\n")
    print("-->[5] BACK\n")
    choice = input("")
    
    stop = False
    while not stop:
        
        if choice == '0':
            Clear_Screen()
            print("Please choose one of these layers to use:")
            print("\n\n")
            print("-->[1] IP()\n")
            print("-->[2] TCP()\n")
            print("-->[3] UDP()\n")
            print("-->[4] ICMP()\n")
            print("-->[5] BACK\n")
            choice = input("")
            
        elif choice == '1':
            Clear_Screen()
            print("Please see the options below to make the IP packet:\n")
            
            print("--> flags = [0 (is reserved), 1 (do not fragment), 2 (more fragments)]\n")
            print("--> ttl = (num) or [num_1,num_2 or/and (num_3,num_4 to get the range(num_3,num_4+1))]\n")
            print("--> proto = (-- Available Protocols:[upd,icmp,tcp])\n")
            print("--> src = \"(IPv4 Address)\"\n")
            print("--> dst = \"(IPv4 Address/hostname)\" or [\"(IPv4 Address_1/hostname_1\"),\"(IPv4 Address_2/hostname_2)\",...]\n")
            print("\n\n")
            print("Please use the format below:\n")
            print("Example: flags = 0  ttl = [1,3,5,(7,10)] proto = tcp src = \"0.0.0.0\" dst = [\"192.168.45.12\",\"255.255.255.0\"] \n")
            print("\n If you wish to leave it empty, please press Enter: \n")

            layer_IP = input("")
            
            F_layer_IP = 'IP(' + layer_IP + ')' 
            
            if packet_created == '':
                packet_created = F_layer_IP
            else:
                packet_created = packet_created + '/' + F_layer_IP
            

            #Choice to stop or not!
            while 1:
                choice = input("Would you like to create more layers?[Y/N]")
                if choice.lower() == "y":
                    choice = '0'
                    break
                elif choice.lower() == "n":
                    stop = True
                    break
                else:
                    print("Invalid input!\n")
            
            
        
        elif choice == '2':
            
            Clear_Screen()
            print("Please see the options below to make the TCP packet:\n")
            
            print("-->sport = (num) or [(num_1), (num_2),...]\n")
            print("-->dport = (num) or [(num_1), (num_2),...]\n")
            print("-->flags = (A/S/F/R/P/SA/PA/U)")
            print("\n\n")
            print("Please use the format below:\n")
            print("Example: sport = 80 dport = [21,22,80] flags = \"SA\"  \n")
            
            print("\n If you wish to leave it empty, please press Enter: \n")

            layer_TCP = input("")
            
            F_layer_TCP = 'TCP(' + layer_TCP + ')' 
            if packet_created == '':
                packet_created = F_layer_TCP
            else:
                packet_created = packet_created + '/' + F_layer_TCP
                
                        #Choice to stop or not!
            while 1:
                choice = input("Would you like to create more layers?[Y/N]")
                if choice.lower() == "y":
                    choice = '0'
                    break
                elif choice.lower() == "n":
                    stop = True
                    break
                else:
                    print("Invalid input!\n")
            
        elif choice == '3':
            
            Clear_Screen()
            print("Please see the options below to make the UDP packet:\n")
            
            print("-->sport = (num) or [(num_1), (num_2),...]\n")
            print("-->dport = (num) or [(num_1), (num_2),...]\n")
            print("\n\n")
            print("Please use the format below:\n")
            print("Example: sport = 80 dport = [21,22,80]  \n")
            
            print("\n If you wish to leave it empty, please press Enter: \n")

            layer_UDP = input("")
            
            F_layer_UDP = 'UDP(' + layer_UDP+ ')' 
            if packet_created == '':
                packet_created = F_layer_UDP
            else:
                packet_created = packet_created + '/' + F_layer_UDP
                
            #Choice to stop or not!
            while 1:
                choice = input("Would you like to create more layers?[Y/N]")
                if choice.lower() == "y":
                    choice = '0'
                    break
                elif choice.lower() == "n":
                    stop = True
                    break
                else:
                    print("Invalid input!\n")
      
        elif choice == '4':
            
            Clear_Screen()
            F_layer_ICMP = 'ICMP()' 
            if packet_created == '':
                packet_created = F_layer_ICMP
            else:
                packet_created = packet_created + '/' + F_layer_ICMP
                
            #Choice to stop or not!
            while 1:
                choice = input("Would you like to create more layers?[Y/N]")
                if choice.lower() == "y":
                    choice = '0'
                    break
                elif choice.lower() == "n":
                    stop = True
                    break
                else:
                    print("Invalid input!\n")
        elif choice == '5':
            print("Quitting the Creating Packet Process...")
            Clear_Screen()
            return 0
        else:
             print("False Input!Please choose one of these layers below:")
             print("\n\n")
             print("-->[1] IP()")
             print("-->[2] TCP()")
             print("-->[3] UDP()")
             print("-->[4] ICMP()")
             print("-->[5] BACK")
             choice = input("")
             
    time.sleep(2)


             
    time.sleep(2)
    
    print("Which of the following commands would you like to use:\n")
    print("\n\n")
    print("-->[1] send() -- sends and receives without a custom ether() layer\n")
    print("-->[2] sendp() -- sends and receives with a custom ether() layer\n")
    print("-->[3] sr1() -- sends and receives without a custom ether() layer and waits for first answer\n")
    print("-->[4] sr1p() -- sends and receives with a custom ether() layer and waits for first answer\n")
    choice = input("")
    

    while 1:
        
        if choice == '1':
            
            print("Process is about to start...")
            print("Please press Ctrl-C to stop...")
            time.sleep(2)
            try:   
                unans, ans = send(packet_created)
            except TypeError:
                print("No answers received.")
                time.sleep(2)
                return 0
            time.sleep(1)
            print(ans)
            break
        elif choice == '2':
                        
            print("Process is about to start...")
            print("Please press Ctrl-C to stop...")
            time.sleep(2)
            
            unans, ans = sendp(packet_created)
            print(ans)
            break
        
        elif choice == '3':
                        
            print("Process is about to start...")
            print("Please press Ctrl-C to stop...")
            time.sleep(2)
            try:
                unans, ans = sr1(packet_created)
            except TypeError:
                print("Packet did not receive any answers...")
                time.sleep(4)
                return 0
            
            print(ans)
            break
        
        elif choice == '4':
                        
            print("Process is about to start...")
            print("Please press Ctrl-C to stop...")
            time.sleep(2)
            
            unans, ans = sr(packet_created)

            print(ans)
            break
      
    

    
###############################################################################################

#Choice 3 --> Read_Pcap
def Read_Pcap():
    pass

def main():
    print("Welcome to Port Analyzer.\n")
    
    print("\n\n\n")
    
    print("Please select one of the choices below:\n")
    print("\n")
    print("-> [1] Sniffing")  
    print("-> [2] Create and Send/Receive Packets")
    print("-> [3] Read pcaps")  
    print("-> [4] Quit")
    choice = input(" ")
    
    while True:
        if choice == '1':
            Sniffing()
            choice = '0'
        elif choice == '2':
            Create_Send_Recieve()
            choice = '0'
        elif choice == '3':
            Read_Pcap()
            choice = '0'
        elif choice == '4':
            print("Exiting...")
            time.sleep(3)
            break
        elif choice == '0':
            Clear_Screen()
            
            print("Welcome to Port Analyzer.\n")
            print("\n\n\n")
                
            print("Please select one of the choices below:\n")
            print("\n")
            print("-> [1] Sniffing")  
            print("-> [2] Create and Send/Receive Packets")
            print("-> [3] Read .pcaps")  
            print("-> [4] Quit")
            
            choice = input(" ")
        else:
            print("Wrong Input. Please select one of the choices below:")
            print("\n")
            print("-> [1] Sniffing")  
            print("-> [2] Create and Send/Receive Packets")
            print("-> [3] Read pcaps")  
            print("-> [4] Quit")
            choice = input(" ")
            
        
    
if __name__ =='__main__':
    main()