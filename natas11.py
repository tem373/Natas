#!/usr/bin/python3

import base64
import json
import requests
import re

from urllib.parse import unquote

def xor_keycrack(plaintext, ciphertext):
    assert(len(plaintext) == len(ciphertext))
    key = ""
    for i in range(0, len(plaintext)):
        key += chr(plaintext[i] ^ ciphertext[i]) # chr() converts int to char
    return key.encode()

level = 11
username = 'natas%s' % level
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
url = 'http://%s.natas.labs.overthewire.org/' % username

# First request testing
response = requests.get(url, auth=(username, password))

# This will have to do with cookies - we have cookies that are protected using XOR encryption.
# View the source code - look for clues
source_response = requests.get(url + 'index-source.html', auth=(username, password))
tmpstr = unquote(response.cookies.get_dict()['data']) #URL decode

# Now base64 decode the cookie to get the raw encrypted version
encryptedCookie = base64.b64decode(tmpstr)

# Now, taking $defaultdata from the source code, we have that as the input and the encrypted cookie
# as the output. Given these two pieces of data and the XOR algorithm, we can find the key and use
# that to properly encrypt a different piece of data to unlock this level!
defaultData = '{"showpassword":"no","bgcolor":"#ffffff"}'.encode()

# Now, decrypt the cookie!
key = xor_keycrack(defaultData, encryptedCookie)

# We got it! The key appears to just be 'qw8J' repeating - now we can encrypt a different value
newCookiePlain = '{"showpassword":"yes","bgcolor":"#ffffff"}'.encode()

# Encrypt the cookie with the new key
newCookieEncrypted = xor_keycrack(newCookiePlain, 'qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw'.encode()) # keylen 42
tmp = base64.b64encode(newCookieEncrypted).decode('ascii')

# Add to cookies
cookies = {'data': tmp}

get_response = requests.post(url, auth=(username, password), cookies=cookies)

# That should do it - now print the password
password = re.findall('The password for natas12 is (.*)<br>', get_response.text)[0]
print(password)

