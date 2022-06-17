# Problem 9 :
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def wrap():
    for a in range(1000):
        for b in range(a + 1, 1000):
            for c in range(b + 1, 1000):
                if a + b + c == 1000 and a**2 + b**2 == c**2:
                    return a, b, c

def answer():
    a, b, c = wrap()
    print(f"The product of the Pythagorean triplet for wich a + b + c = 1000 is {a * b * c} (a = {a}, b = {b}, c = {c})")

if __name__ == "__main__":
    answer()