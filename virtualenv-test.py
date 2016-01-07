#!/usr/bin/env python


import requests

print requests.__version__

respones = requests.get('https://google.com/')
print respones.status_code

print respones.text
