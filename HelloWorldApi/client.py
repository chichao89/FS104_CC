import requests

url = 'http://127.0.0.1:8000/hello/'
headers = {'Authorization': 'Token dfcd35657a422db13344c82d3e5942278ec41eb2'}
r = requests.get(url, headers=headers)
print(url)
print(headers)
print(r)
