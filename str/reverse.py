print("入力された文字を逆順に並べ替えるプログラムです。")
print("Please input a word : ")
sentence = input()
revesed_sentense = sentence[::-1]
print(revesed_sentense)

# スライスは[start:stop:end]の形で範囲や増分を指定する。
# start, stopを省略すると全体を選択し、stepを-1とすると後ろから一つずつ要素を取得することになるので
# [::-1]とすると逆順に並べ替えられたオブジェクトが取得できる。
# 今回の例では、sentence配列を逆順に(後ろから)取り出し、reversed_sentense配列に全体を入れていく