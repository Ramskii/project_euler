# Problem 7 :
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math

def answer():
    n = 1
    primes = []
    while len(primes) < 10001:
        n += 1
        is_prime = True
        for p in primes:
            if n % p == 0:
                is_prime = False
                break
            if p > math.sqrt(n):
                break
        if is_prime:
            primes.append(n)
    print(f"The 10 001st prime number is {primes[-1]}")

if __name__ == "__main__":
    answer()