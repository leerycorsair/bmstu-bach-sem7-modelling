

import random

SIZE = 1000


def gen(count: int, digits: int) -> list[int]:
    filename = {1: "dataX.txt", 2: "dataXX.txt", 3: "dataXXX.txt"}
    file = open(filename[digits], "r", encoding="utf-8")
    values = file.read().strip().split(" ")
    values = [int(value) for value in values]
    while count > len(values):
        values = values * 2
    return values[:count]


def main() -> None:
    fileX = open("dataX.txt", "w", encoding="utf-8")
    for _ in range(SIZE):
        fileX.write(str(random.randint(0, 9)) + " ")
    fileX.close()

    fileXX = open("dataXX.txt", "w", encoding="utf-8")
    for _ in range(SIZE):
        fileXX.write(str(random.randint(10, 99)) + " ")
    fileXX.close()

    fileXXX = open("dataXXX.txt", "w", encoding="utf-8")
    for _ in range(SIZE):
        fileXXX.write(str(random.randint(100, 999)) + " ")
    fileXXX.close()


if __name__ == "__main__":
    main()

    # gen(2000, 1)
