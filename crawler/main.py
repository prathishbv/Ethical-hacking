#usr/bin/env python3

import requests

def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "10.0.2.7/mutillidae/"
# [+] It is used to find the directories using wordlist
with open("/root/Downloads/files-and-dirs-wordlist.txt") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = target_url + "/" + word
        response = request(test_url)
        if response:
            print("[+] Discovered directory -->", test_url)

# [+] It is used to find the subdomains using wordlist
# with open("/root/Downloads/subdomains-wodlist.txt") as wordlist_file:
#     for line in wordlist_file:
#         word = line.strip()
#         test_url = word + "." +target_url
#         response = request(test_url)
#         if response:
#             print("[+] Discovered subdomain -->", test_url)