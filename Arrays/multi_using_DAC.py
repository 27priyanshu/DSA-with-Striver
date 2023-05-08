import timeit
import random
def dac_multiply(x, y):
    if x < 10 or y < 10:
        return x * y
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    a = x // 10**m
    b = x % 10**m
    c = y // 10**m
    d = y % 10**m

    ac = dac_multiply(a, c)
    bd = dac_multiply(b, d)
    add = dac_multiply(a+b, c+d) - ac - bd
    return ac * 10**(2*m) + add * 10**m + bd
def naive_multiply(x, y):
    prod = 0
    for i, digit_x in enumerate(str(x)[::-1]):
        for j, digit_y in enumerate(str(y)[::-1]):
            prod += int(digit_x) * int(digit_y) * 10**(i+j)
            return prod
values = [4, 8, 16, 32, 64]
for n in values:
    x = random.randint(10**(n-1), 10**n-1)
    y = random.randint(10**(n-1), 10**n-1)

    dac_time = timeit.timeit(lambda: dac_multiply(x, y), number=100)
    naive_time = timeit.timeit(lambda: naive_multiply(x, y), number=100)

    print(f"N={n}:")
    print(f"Divide and conquer time: {dac_time:.8f} seconds")
    print(f"Naive time: {naive_time:.8f} seconds\n")