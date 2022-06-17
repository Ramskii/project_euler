def answer(min_divisor=5):
    n = 1
    n_divisor = 0
    triangle = 0
    while n_divisor <= min_divisor:
        triangle += n
        n_divisor = 1
        for d in range(1, int(triangle / 2) + 1):
            if triangle % d == 0:
                n_divisor += 1
        n += 1
    return triangle