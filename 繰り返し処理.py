#continueとfor文
numbers =[ 10, 21, 32, 65]

for n in numbers:
    print(f"{n}：前処理")
    if n % 2 == 0:
        continue
    print(f"{n}:後処理")