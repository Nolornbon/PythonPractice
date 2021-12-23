def fact(x):
    if x < 0:
        raise ValueError ("x<0, що неможливо")
    if x == 0:
        return 1
    else:
        return x * fact(x-1)