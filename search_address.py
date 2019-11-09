import requests


def search_address(zipcode: str) -> list:
    response = requests.get(f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}')
    res_dic = response.json()
    if res_dic['message'] is not None:
        print('エラー:', res_dic['message'])
        return []

    if res_dic['results'] is None:
        print('エラー: 存在しない郵便番号です')
        return []

    address_list = []
    for address_dic in res_dic['results']:
        text = address_dic["address1"]
        text += address_dic["address2"]
        text += address_dic["address3"]
        address_list.append(text)

    return address_list
