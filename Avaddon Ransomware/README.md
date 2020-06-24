# Avaddon Ransomware
Decrypt the encrypted base64 strings present in the Avaddon binary, supports v1 and v2. 

* Md5: **c9ec0d9ff44f445ce5614cc87398b38d** (v1), discovered around 5 June, 2020
* Md5: **6c660f960daac148be75427c712d0134** (v2), discovered around 21 June, 2020

## How to execute?
Just run this decrypt_base64_strings.py with the file containing base64 encrypted string and variant version 
```
python3 decrypt_base64_strings.py -f base64str_v2.txt -v 2 > decrypted_v2.txt
```
### Contains:
Avaddon Ransomware v1
- base64str.txt - contain base64 encoded strings
- decrypted.txt - decrypted strings 

Avaddon Ransomware v2
- base64str_v2.txt - contain base64 encoded strings
- decrypted_v2.txt - decrypted strings

Some more details available in below tweets:
- https://twitter.com/Securityinbits/status/1270274719711768576 -  9 Jun, 2020
- https://twitter.com/Securityinbits/status/1271065316903120902 - 11 Jun, 2020
- https://twitter.com/Securityinbits/status/1275909295100489730 - 25 Jun, 2020

License
----
No copyright and use at your own risk
