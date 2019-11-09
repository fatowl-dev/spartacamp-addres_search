import requests


# データを加工して表示する
def display_address(dic: dict):
    if dic['message'] is not None:
        print('エラー:', dic['message'])
        return

    if dic['results'] is None:
        print('エラー: 存在しない郵便番号です')
        return

    for address_dic in dic['results']:
        message = address_dic["address1"]
        message += address_dic["address2"]
        message += address_dic["address3"]
        print(message)


zipcode = input('郵便番号?: ')
# zipcode = '0287302'
if len(zipcode) != 7 or not zipcode.isdigit():
    print('エラー: 7桁の数字を入力してください')
    exit()

response = requests.get(f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}')
# print(response)
# print(response.text)
res_dic = response.json()
display_address(res_dic)
