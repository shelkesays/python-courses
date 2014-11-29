def is_int(num):
    if num == int(num):
        num = int(num)
    if type(num) == int:
        return True
    else:
        return False


print is_int(5.0)
