
import random as r


def __gen_seed():
    m = r.randint(100000, 1000000)
    a = r.randint(10000, 100000)
    c = r.randint(10000, 100000)
    x0 = r.randint(10000, 100000)
    return m, a, c, x0


def gen(count: int, min: int, max: int) -> list[int]:
    m, a, c, x0 = __gen_seed()
    values = [x0]
    for _ in range(count):
        curr_value = (values[-1] * a + c) % m
        values.append(min + curr_value % (max - min + 1))
    return values[1:]


if __name__ == "__main__":
    genX = gen(100, 0, 9)
    print(genX)
    print(sorted(genX))
    print("\n")
    genXX = gen(100, 10, 99)
    print(genXX)
    print(sorted(genXX))
    print("\n")
    genXXX = gen(100, 100, 999)
    print(genXXX)
    print(sorted(genXXX))




