import math

def log(a, b):
    if a < 0 or a == 1 or b < 0:
        raise ValueError
    else:
        return math.log(a, b)

def ln(a):
    if a < 0:
        raise ValueError
    else:
        return math.log(a)

def lg(a):
    if a < 0:
        raise  ValueError
    else:
        return math.log(a, 10)

