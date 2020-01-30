#!/usr/bin/python3

import requests
import re

level = 8
username = 'natas%s' % level
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'
url = 'http://%s.natas.labs.overthewire.org/' % username

# First request testing
response = requests.get(url, auth=(username, password))

# View the source code - look for clues
source_response = requests.get(url + 'index-source.html', auth=(username, password))
print(source_response.content)

# Here we've got a hex string that appears to be the hex(reversestring(b64(secretkey))) - if we reverse this we might get the
# key to unlock the page with the password on it. First regex the encodedSecret string, decode it and make a POST request with
# that as the 'secret' parameter

# That should do it - now print the password
password = re.findall('<br>\n<br>\n(.*)\n\n', etc_response.text)[0]
print(password)

