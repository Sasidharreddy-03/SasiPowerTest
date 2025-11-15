def sasi_power_test(x, y):
    if x == 1:
        return False
    if y == 1:
        return True
    if x == y:
        return True

    step = (x*x) - x
    for i in range(x, int(y/x) + 1, step):
        if x * i == y:
            return True

    return False
