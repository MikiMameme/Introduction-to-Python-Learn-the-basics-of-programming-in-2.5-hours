#breakとfor文
numbers = [10, 21, 100, 18, 2]

for n in numbers:
    if n >= 100: #100以上の数が出たらfor分を抜けたい
        break
    print(f"{n}：繰り返し")
print("for文の外")