print("簡単な電卓アプリです。")
a = float(input("1つ目の数字を入力してください: "))
op = input("演算子を入力（+ - * /）: ")
b = float(input("2つ目の数字を入力してください: "))

if op == "+":
    print(f"結果: {a + b}")
elif op == "-":
    print(f"結果: {a - b}")
elif op == "*":
    print(f"結果: {a * b}")
elif op == "/":
    if b != 0:
        print(f"結果: {a / b}")
    else:
        print("0では割れません！")
else:
    print("対応していない演算子です。")