
from scipy.stats import erlang


class ErlangDistribution:
    def __init__(self, alpha: int,  beta: float, loc: float) -> None:
        self.alpha = alpha
        self.beta = beta
        self.loc = loc

    def generate(self):
        return erlang.rvs(self.alpha, loc=self.loc, scale=1/self.beta, size=1)[0]


def main():
    distr = ErlangDistribution(1, 1, 0)

    for _ in range(100):
        print(distr.generate())


if __name__ == "__main__":
    main()
