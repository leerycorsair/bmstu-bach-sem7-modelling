

def leonov_check(arr: list[int]) -> float:
    diff_arr = []
    initial_len = len(arr)
    iters = 0
    while len(arr) != 1:
        for i in range(len(arr)-1):
            diff_arr.append(abs(arr[i+1] - arr[i]))

        new_arr = [diff_arr[0]]
        for i in range(1, len(diff_arr)):
            if diff_arr[i] != diff_arr[i-1]:
                new_arr.append(diff_arr[i])

        arr = new_arr
        diff_arr = []
        iters += 1

    return iters/(initial_len)


if (__name__ == "__main__"):
    arr = [(i*i-i+5) % 37 for i in range(100)]
    leonov_check(arr)
    leonov_check([1, 6, 9, 4, 3, 5])
    leonov_check([1, 2, 3, 3, 2, 1])

    leonov_check([1, 6, 9, 4, 3, 5, 8, 3, 7, 1, 5, 3, 4, 5, 6, 7, 8, 9, 10])
    leonov_check([1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 4, 6, 23, 6, 2,
                 4, 5, 34, 53, 23, 424, 35, 35, 34, 23, 23, 2, 23, 23, 23, 232])
