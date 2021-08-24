import scapy.all as scapy


def get_mac(ipaddress):
    destination_ip=scapy.ARP(pdst=ipaddress)
    destination_mac=scapy.ARP(hwdst='ff:ff:ff:ff:ff:ff')
    packet=destination_mac/destination_ip
    answered_packet=scapy.srp(packet,verbose=False)[0]
    return answered_packet[0][1].hwsrc

    print(scapy.ls(scapy.ARP()))
def packet_sniffer(interface):
    sniffed_packet=scapy.sniff(iface=interface,store=False,prn=packet_process)

def packet_process(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op==2:
        real_mac=get_mac(packet[scapy.ARP].psrc)
        response_mac=packet[scapy.ARP].hwsrc
        if real_mac==response_mac:
            pass
        else:
            print("under attack...")
        
        print(packet.show())

#get_mac('192.168.1.1')
packet_sniffer('wlp1s0')
