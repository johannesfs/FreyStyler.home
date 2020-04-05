#!/usr/local/bin/python3
import urllib, requests

# Connect to Home Center
r = requests.get('http://192.168.86.124/api/devices', auth=("johannesfs@gmail.com", "Tluhmmal75"))
print(r.status_code)

# hc = Client('v3', 'http://192.168.86.124/api/', 'johannesfs@gmail.com', 'tluhmmal75')
