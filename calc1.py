from math import sqrt

def calc_sum(a, e, i, o):
    return a + e + i + o

def calc_diff(a, e):
    return a - e

def calc_multi(a, e, i, o):
    return a * e * i * o

def calc_div(a, e):
    return a / e

def calc_pow(a, e):
    return a ** e

def calc_root(a):
    return sqrt(a)

def calc_prime(a):
    div = []
    for e in range(2, a):
        if a % e == 0:
            div.append(e)
    if div:
        return f"{a} is not a prime number. It can be divided by {div}."
    else:
        return f"{a} is a prime number."

def calc_lcm(a, e, i):
    o = a * e * i
    for u in range(1, o+1):
        if u % a == 0 and u % e == 0 and u % i == 0:
            return u

def calc_intdiv(a, e):
    return f"The result of the division is {a//e} with {a % e} remaining."

def calc_pcent(a, e):
    o = a * 100 / e
    return o