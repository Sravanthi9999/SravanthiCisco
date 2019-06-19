import requests
import sys
import json

if len(sys.argv) <= 1:
        print("Invalid arguments")
        sys.exit(1)
macAddress = sys.argv[1]

payload = {'apiKEY':'at_QnRpupLp1Ff0BfvCPJWVYs33CKsZ1','output':'json','search': macAddress}
req = requests.get("https://api.macaddress.io/v1",params=payload)
print(req.url)
print(req.text)
print(req.status_code)