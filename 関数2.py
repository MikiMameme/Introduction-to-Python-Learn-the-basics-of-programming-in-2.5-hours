#引数と戻り値

def add_numbers(a, b):
    c = a + b
    d = a - b
    return c, d


added = add_numbers(b=10, a=100)
print(added)