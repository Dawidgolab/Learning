"""
pip - pip installs packeges
Pypi - Phyton Packege index
To download the library reguests we open the pypi.org
"""
import requests

interia = requests.get("https://www.interia.pl/")
print(interia.status_code)

