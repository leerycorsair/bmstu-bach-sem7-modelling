from numpy import linalg
import random

TIME_DELTA = 1e-3
EPS = 1e-5


def random_mtr(size: int) -> list[list[float]]:
    mtr = [[round(random.random(), 2) * random.randint(0, 1)
            for _ in range(size)] for _ in range(size)]
    return mtr


def get_coef_mtr(mtr: list[list[float]]) -> list[list[float]]:
    size = len(mtr)
    coef_mtr = [[0.0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if (i == j):
                coef_mtr[i][i] = -sum(mtr[i]) + mtr[i][i]
            else:
                coef_mtr[i][j] = mtr[j][i]
    return coef_mtr


def calc_prob(mtr: list[list[float]]) -> list[float]:
    size = len(mtr)

    coef_mtr = get_coef_mtr(mtr)
    coef_mtr[size - 1] = [1 for _ in range(size)]

    ordinate_values = [0 if i != size - 1 else 1 for i in range(size)]
    return linalg.solve(coef_mtr, ordinate_values).tolist()


def calc_prob_delta(mtr: list[list[float]], prob_curr: list[float]):
    size = len(mtr)

    prob_delta = []
    coef_mtr = get_coef_mtr(mtr)

    for i in range(size):
        for j in range(size):
            coef_mtr[i][j] *= prob_curr[j]
        prob_delta.append(sum(coef_mtr[i]) * TIME_DELTA)
    return prob_delta


def calc_time(mtr: list[list[float]], prob: list[float]):
    size = len(mtr)

    time_curr = 0.0
    prob_curr = [1.0 / size for _ in range(size)]

    time = [0.0 for _ in range(size)]
    while not all(time):
        prob_delta = calc_prob_delta(mtr, prob_curr)
        for i in range(size):
            if not time[i] and abs(prob_curr[i] - prob[i]) <= EPS:
                time[i] = time_curr
            prob_curr[i] += prob_delta[i]
        time_curr += TIME_DELTA

    return time


def calc_res(mtr: list[list[float]]) -> tuple[list[float], list[float]]:
    prob = calc_prob(mtr)
    time = calc_time(mtr, prob)
    return prob, time
