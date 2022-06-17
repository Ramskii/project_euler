# Problem 3 :
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

def answer():
    n = 600851475143
    largest_prime_factor = 1
    primes = []
    for i in range(2, int(math.sqrt(n)) + 1):
        is_prime = True
        for p in primes:
            if i % p == 0:
                is_prime = False
                break
            if p > math.sqrt(i):
                break
        if is_prime:
            primes.append(i)
            if n % i == 0:
                largest_prime_factor = i
    print(f"The largest prime factor of {n} is {largest_prime_factor}")

if __name__ == "__main__":
    answer()