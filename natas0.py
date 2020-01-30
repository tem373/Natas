#!/usr/bin/python3

import requests
import re

level = 0
username = 'natas%s' % level
password = 'natas0'
url = 'http://%s.natas.labs.overthewire.org' % username

response = requests.get(url, auth=(username, password))
password = re.findall('<!--The password for natas%s is (.*) -->' % str(level+1), response.text)[0]

print(password)
