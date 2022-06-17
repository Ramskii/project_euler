# Problem 5 :
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time

def is_divisible_by_1_to_20(n):
    for d in [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 20]:
        if n % d != 0:
            return False
    return True

def answer():
    t = time.time()
    correct = False
    n = 0
    while not correct: # and n < 10000000:
        n += 1
        correct = is_divisible_by_1_to_20(n)       
    print(f"Smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {n}")
    print(f"Execution time : {round(time.time() - t, 1)} sec")

if __name__ == "__main__":
    answer()