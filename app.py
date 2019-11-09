import requests

response = requests.get('http://zipcloud.ibsnet.co.jp/api/search?zipcode=0287302')
print(response)
print(response.text)