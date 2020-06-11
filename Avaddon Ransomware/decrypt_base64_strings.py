# Script to decrypt the encrypted base64 strings present in the Avaddon binary
# Md5: c9ec0d9ff44f445ce5614cc87398b38d
# Author: Securityinbits
import base64
import sys

def decrypt(str):
    out= []
    for i in bytearray(str):
        # First subtraction with 2 then xoring with 0x43
        out.append((i-2)^0x43)
    return ''.join(chr(i) for i in out)

# base64str.txt contain base64 encoded string found in the Avaddon binary
with open('./base64str.txt','r') as f:
    for i in f:
        print (decrypt(base64.b64decode(i.strip())))
