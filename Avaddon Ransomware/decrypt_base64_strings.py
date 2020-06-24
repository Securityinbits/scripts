# Decrypt the encrypted base64 strings present in the Avaddon binary
# Differnt keys for v1 and v2
# Todo: May be in future version, it will select this automatically
# Md5: c9ec0d9ff44f445ce5614cc87398b38d (v1)
# Md5: 6c660f960daac148be75427c712d0134 (v2)
# Author: Securityinbits
import base64
import sys

from argparse import ArgumentParser

def decrypt(str, variant):
    out= []
    # To-do: simplify the script
    # For v1 it uses below key
    if variant == 1:
        sub_key = 0x2
        xor_key = 0x43

    # For v2 use this below key
    if variant == 2:
        sub_key = 0x4
        xor_key = 0x92

    for i in bytearray(str):
        # First subtraction with key then xoring with key
        out.append(((i-sub_key) ^ xor_key) & 0xff)
    return ''.join(chr(i) for i in out)

def main(args):
    # Pass the encyrypted base64 strings
    with open(args.filepath,'r') as f:
        for i in f:
            print (decrypt(base64.b64decode(i.strip()), args.variant))

if __name__ == "__main__":
    ap = ArgumentParser(description='Decrypt the encrypted base64 strings present in the Avaddon')
    ap.add_argument('-f', '-filepath', dest='filepath', required=True, help="File path for base64 encrypted string")
    ap.add_argument('-v', '-variant', dest='variant', required=True, type=int, help="enter 1 or 2, then key will be selected")
    args = ap.parse_args()
    main(args)
