#!use/bin/env python

import scapy.all as scapy

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, verbose=False, timeout=1)[0]
    return answered_list[0][1].hwsrc


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packets)



def process_sniffed_packets(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        try:
            real_mac = get_mac(packet[scapy.ARP].prsc)
            responce_mac = packet[scapy.ARP].hwsrc
            if real_mac != responce_mac:
                print("[+] You are under attack!!!")
            print(packet.show)
        except IndexError:
            pass

sniff("eth0")
