# Problem 4 :
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    s = str(n)
    l = len(s)
    for i in range(int(l/2) + 1):
        if s[i] != s[l - i - 1]:
            return False
    return True

def answer():
    largest_pal = 0
    largest_pal_i = 0
    largest_pal_j = 0
    for i in range(1000):
        for j in range(i + 1):
            n = i * j
            if is_palindrome(n):
                if n > largest_pal:
                    largest_pal = n
                    largest_pal_i = i
                    largest_pal_j = j
    print(f"Largest palindrome made from the product of two 3-digit numbers is {largest_pal_i} * {largest_pal_j} = {largest_pal}")

if __name__ == "__main__":
    answer()