#辞書内の数値を表示する

fruits = {"apple":130, "banana":350, "lemon":100}

for name, price in fruits.items():
    print(f"{name}は{price}円です")