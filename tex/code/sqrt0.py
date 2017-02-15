def sqrt(a):
    x = 1
    for i in range(5):
        x = (x + a / x) / 2
    return x
