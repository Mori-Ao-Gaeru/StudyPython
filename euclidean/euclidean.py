def gcf(a, b):
  if b == 0: #bが0のときは割れないのでaとbを入れ替える
    (a, b) = (b, a)
  while b != 0:
    (a, b) = (b, a % b)
  return a
 
print("ユークリッドの互除法で最大公約数を求める")
print("スペース区切りで2つの自然数を入力してください")
x, y = input().split() # スペース区切りの標準入力
a = int(x)
b = int(y)

print(gcf(a, b))