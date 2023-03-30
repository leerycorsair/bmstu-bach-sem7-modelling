

from math import exp, factorial
import numpy as np


def ud_cdf(x: float, a: float, b: float):
    if x < a:
        return 0
    elif x > b:
        return 1
    else:
        return (x - a) / (b - a)


def ud_pdf(x: float, a: float, b: float):
    if x >= a and x <= b:
        return 1 / (b - a)
    return 0


def erlang_cdf(x: float, k: float, theta: float):
    return 1 - exp(-x / theta) * sum((x/theta)**i/factorial(i) for i in range(k))


def erlang_pdf(x: float, k: float, theta: float):
    return x**(k-1) * exp(-x*theta) * theta**k / factorial(k-1)


def calc_ud_cdf(left: float, right: float, a: float, b: float):
    x = np.arange(left, right, (right-left)/1000)
    y = [ud_cdf(x, a, b) for x in x]
    return x, y


def calc_ud_pdf(left: float, right: float, a: float, b: float):
    x = np.arange(left, right, (right-left)/1000)
    y = [ud_pdf(x, a, b) for x in x]
    return x, y


def calc_erlang_cdf(max: float, k: int, theta: float):
    x = np.arange(0, max, max/1000)
    y = [erlang_cdf(x, k, theta) for x in x]
    return x, y


def calc_erlang_pdf(max: float, k: int, theta: float):
    x = np.arange(0, max, max/1000)
    y = [erlang_pdf(x, k, theta) for x in x]
    return x, y
