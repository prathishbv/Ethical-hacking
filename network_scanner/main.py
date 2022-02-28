#!/usr/bin/env python

import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="IP should be provided")
    options = parser.parse_args()
    if not options:
        parser.error("[-] IP should be specified")
    else:
        return options


def scan(ip):
    arp_request=scapy.ARP(pdst=ip)
    # scapy.ls(scapy.ARP())   IT WILL DISPLAYS THE OPTIONS THAT ARE AVAILABLE IN THE SCAPY.ARP HERe WE USE PDST TO HANDLE THE IP ADDRESS
    # arp_request.show()      IT WILL SHOW ALL THE INFO OF ARP_REQUEST

    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # scapy.ls(scapy.Ether())   IT WILL DISPLAYS THE OPTIONS THAT ARE AVAILABLE IN THE SCAPY.ARP HERE WE USE DST TO SET THE MAC ADDRESS
    # broadcast.show()          IT WILL SHOW ALL THE INFO OF BROADCAST

    arp_request_broadcast=broadcast/arp_request
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()

    answered_list = scapy.srp(arp_request_broadcast, verbose=False, timeout=2)[0]
    # print(answered.summary())
    # print(unanswered.summary())


    client_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        client_list.append(client_dict)
        # print(element[1].show()) IT WILL SHOW THE COMPLETE OUTPUT
        # print(element[1].hwsrc)  #IT PRINTS THE DESTINATION MAC

    return client_list

def print_result(client_result):
    print("IP\t\t\tMAC address\n----------------------------------------------")
    for client in client_result:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
client_result = scan(options.target)
print_result(client_result)