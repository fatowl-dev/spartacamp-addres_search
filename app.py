import requests


# 郵便番号を入力すると住所のリストを返す
# エラーの場合は空のリストを返す
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


def main():
    zipcode = input('郵便番号?: ')
    # zipcode = '0287302'

    if len(zipcode) != 7 or not zipcode.isdigit():
        print('エラー: 7桁の数字を入力してください')
        exit()

    address_list = search_address(zipcode)
    for address in address_list:
        print(address)


if __name__ == '__main__':
    main()
