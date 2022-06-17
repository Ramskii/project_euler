# Problem 10 :
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math

def answer():
    n = 1
    primes = []
    sum = 0
    while n < 2000000:
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
            sum += n
    print(f"The sum of all the prime below 2 000 000 is {sum}")

if __name__ == "__main__":
    answer()