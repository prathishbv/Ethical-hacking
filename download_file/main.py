#!usr/bin/env python3

import requests

def download(url):
    get_responce = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name,"wb") as out_file:
        out_file.write(get_responce.content)

download("https://image.shutterstock.com/image-photo/aerial-view-monemvasia-island-linked-600w-1944646087.jpg")