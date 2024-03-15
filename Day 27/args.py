def add(*args):
    result = 0
    print(type(args))
    for n in args:
        result += n
    return result


print(add(6, 4, 5, 5))
