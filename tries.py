import time

def tries():
    n = 1
    triangle = 0
    max_divisor = 0
    for i in range(100):
        triangle += n
        n_divisors = []
        for d in range(1, int(triangle / 2) + 1):
            if triangle % d == 0:
                n_divisors.append(d)
            if triangle % d != 0 and d in []:
                break
        n_divisors.append(triangle)
        if len(n_divisors) > max_divisor:
            max_divisor = len(n_divisors)
            print(f"NEW RECORD -> {max_divisor}")
        print(f"T{n} = {triangle} -> Divisors : {n_divisors}")
        n += 1
if __name__ == "__main__":
    t = time.time()
    tries()
    print(f"Execution time : {round(time.time() - t, 1)}")