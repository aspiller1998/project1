#! /usr/bin/env python3

import webbrowser
from time import sleep

url = input('Input the URL to reload, including "http://: ')

while True:
    print("refreshing...")
    sleep(10)    webbrowser.open(url, new=0)