import scapy.all as scapy
import argparse


def scanner(ipaddress):
    #Creating a Arp request using a destination ip address and our ip address 
    ip_headers=scapy.ARP(pdst=ipaddress)
    #Creating a Arp request using Broadcast Macaddress
    Destination_Mac=scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    #Combining both to Create a packet .Packet will have srcip ,srcmac,dstip,dstmac
    Packet=Destination_Mac/ip_headers
    #Using the srp( )Method (SendRecievePacket) to send a packet to to clients and catching the reply in variable
    Request_Packets=scapy.srp(Packet,timeout=1,verbose=False)[0]  
    #We looping through the result and extracting the clientip and clientmac.
    print("IPADDRESS \t\t\t MACADDRESS")
    for reply_packet in Request_Packets:
        print(reply_packet[1].psrc + "\t\t" + reply_packet[1].hwsrc)
        
def parse_arguments():
    parser=argparse.ArgumentParser()
    parser.add_argument('-i','--ipaddress',dest='ipaddress',help="Enter the ipaddress or ipaddress  with subnetmask for entering range of ipaddress..")
    #parse_args() gives the reuslt argument so we can catch the argument in the variable
    args=parser.parse_args()
    ipaddress=args.ipaddress
    scanner(ipaddress)

parse_arguments()
