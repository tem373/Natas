#!/usr/bin/python3

import base64
import codecs
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

# Here we've got a hex string that appears to be the hex(reversestring(b64(secretkey))) - if we reverse this we might get the
# key to unlock the page with the password on it. First regex the encodedSecret string and perform decoding
encodedString = re.findall('\$encodedSecret&nbsp;=&nbsp;"(.*)";<br /><br />', source_response.text)[0]
decodedString = base64.b64decode(codecs.decode(encodedString, "hex")[::-1])

# Now, make a POST request providing the decoded string as a POST parameter
post_params = {'secret':decodedString, 'submit':'Submit+Query'}
post_response = requests.post(url, auth=(username, password), data=post_params)

# That should do it - now print the password
password = re.findall('The password for natas9 is (.*)', post_response.text)[0]
print(password)

