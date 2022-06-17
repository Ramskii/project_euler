# Problem 6 :
# The sum of the squares of the first ten natural numbers is,
# 385
# The square of the sum of the first ten natural numbers is,
# 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def answer():
    s1 = 0
    s2 = 0
    for i in range(1, 101):
        s1 += i**2
        s2 += i
    s2 = s2**2
    print(f"The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is {s2 - s1}")

if __name__ == "__main__":
    answer()