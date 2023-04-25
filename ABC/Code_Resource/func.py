# 入力関係

## 1行に2つの文字
A, B = map(int, input().split())
## 1行にN個の文字（リスト化して入力）
num_ls = list(input().split())
num_ls = list(map(int, input().split()))
## 1行に文字と列が混同している場合
N = int(input())
list = []
for i in range(N):
    a,b=input().split()
    list.append([int(a), b])


# 文字列操作

"""
大文字と小文字の変換
- すべての文字を大文字に変換
- すべての文字を小文字に変換
- 先頭の一文字を大文字、他を小文字に変換
- 単語の先頭の一文字を大文字、他を小文字に変換
- 大文字を小文字に、小文字を大文字に変換
"""
str.upper()
str.lower()
str.capitalize()
str.title()
str.swapcase()
"""
大文字と小文字の判定
- すべての文字が大文字かどうか判定
- すべての文字が小文字かどうか判定
- タイトルケースかどうか判定
"""
str.isupper()
str.islower()
str.istitle()

