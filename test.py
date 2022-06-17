import time
import answer12

def answer():
    t = time.time()
    triangle = answer12.answer(300)
    print(f"The value of the first triangle number to have over five hundred divisors is {triangle}")
    print(f"Execution time : {round(time.time() - t, 1)} sec")

if __name__ == "__main__":
    answer()