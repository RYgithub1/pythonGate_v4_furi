from pathlib import Path
# 必要なオブジェクト(今回datetime)だけfrom_import
from datetime import date, timedelta
import modulefile


# 配列リスト[ハッシュ辞書(dict型)]
data = [
    {"name": "ケビン", "bill": 55500, "crg": True},
    {"name": "レイチェル", "bill": 22200, "crg": False}
]
print(data[1]["name"])
print(data[1]["bill"])

for rec in data:
    bill = rec["bill"]
    if rec["crg"]:
        bill = modulefile.add_charge(bill)
    modulefile.create_mail(rec["name"], bill)


one_week = "月火水木金土日"
# データ保存して使いたい->対象の型でオブジェクトを用意する必要がある
# dateオブジェクトの作成
start = date(2020, 8, 20)
for d in range(14):
    cur = start + timedelta(days=d)
    wd = cur.weekday()
    print(cur, one_week[wd])


# fileオブジェクトの作成(にはopen関数を使う)。fileを開き変数rfileへ代入
rfile = open("sample.txt", encoding="utf-8")
# readメソッドで読み込み
text = rfile.read()
rfile.close()
text = text.replace("1", "x")
print("")
print(text)
print("")

# 引数w指定でwrite書き込みのオブジェクトを生成
wfile = open("output.txt", mode="w", encoding="utf-8")
# writeメソッドで書き込み
wfile.write(text)
wfile.close()


# ファイルやフォルダを操作するモジュールとして、pathlibモジュールのPathオブジェクトを利用
terms = {"for": 0, "if": 0, "else": 0}
path = Path()
for filepath in path.glob('*.py'):
    rfile = open(filepath, encoding="utf-8")
    text = rfile.read()
    rfile.close()

    for term in terms:
        # cnt = text.count("for")
        cnt = text.count(term)
        print(filepath, cnt)
        terms[term] += cnt
print("")


howOld = input("年齢は？ : ")
if howOld.isdigit():
    age = int(howOld)
    if age < 20:
        if 6 <= age <= 15:
            print("未成年＿義務教育")
        else:
            print("未成年＿他")
            print("EOL(end of line)＝行末")
    elif age < 65:
        print("成人")
    else:
        print("高齢者")


print("")
programing_language = ["Python", "Java", "R", "Flutter", "PHP"]
print(programing_language)
programing_language.pop()
print("配列リストの最後を削除")
print(programing_language)
del programing_language[1]
print("指定した要素を削除")
print(programing_language)
programing_language.append("Ruby")
print("配列リストに要素を追加")
print(programing_language)
programing_language.remove("R")
print("配列リストから値と一致する最初の要素を削除")
print(programing_language)


# タプル：要素を変更できない配列リスト
print("")
example_Tuple = ("ラーメン", 500)
example_Array = ["寿司", 1000]
print("Tuple :" + example_Tuple[0])
print("Array :" + example_Array[0])
# example_Tuple[0] = "カレー"
example_Array[0] = "天ぷら"
print("Tuple :" + example_Tuple[0])
print("Array :" + example_Array[0])


# 総当り対戦表
print("")
team = ["A", "B", "C", "D", "E"]
opps = ["A", "B", "C", "D", "E"]
for t1 in team:
    opps.remove(t1)
    for t2 in opps:
        print(t1, " vs ", t2)
