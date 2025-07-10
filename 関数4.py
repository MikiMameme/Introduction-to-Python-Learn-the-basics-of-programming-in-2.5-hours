#うるう年かどうか表示する

def is_leap_yeas(year):
    if year % 400 == 0:
        return True

    elif year % 100 == 0:
        return False

    elif year % 4 == 0:
        return True

    else:
        return False



year =2024
result = is_leap_yeas(year)
print(result)