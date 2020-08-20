def create_mail(recv, bill):
    # トリプルクオート->長文文字列
    tmp = '''{}様
企画のジョンです。
今月の請求額は{}円です。
'''
    # formatメソ＝{フィールド}へ任意の値を差し込む
    msg = tmp.format(recv, bill)
    print("create_mail()")
    print(msg)
    print("")


create_mail("ケビン", 77700)


def add_charge(bill):
    if bill < 0:
        return 0
    return int(bill*1.07)


print("add_charge()")
print(add_charge(40000))
# print(add_charge(-1000))
print("")


# - 標準ライブラリ(import文のみで使用可能)
# datetime, json, math, pathlib, random, tkinter
# - 外部ライブラリ(pipピップでダウンロード)
# 画像処理, Excel操作, 科学技術計算, 機会学習, Webサーバ構築
