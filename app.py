# 郵便番号を入力すると住所のリストを返す
# エラーの場合は空のリストを返す
from search_address import search_address


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
