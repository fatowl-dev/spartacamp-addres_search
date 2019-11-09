import requests
zipcode = input('郵便番号?: ')
if len(zipcode) != 7 or not zipcode.isdigit():
    print('エラー: 7桁の数字を入力してください')
    exit()


response = requests.get(f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}')
print(response)
print(response.text)
