age = int(input("あなたの年齢は?: "))
if age < 4:
    print("入場料は無料です")
elif age < 13:
    print("子供料金で入場できます")
elif age < 65:
    print("大人料金で入場できます")
else: 
    print("シニア料金で入場できます")