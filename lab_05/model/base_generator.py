
from scipy.stats import uniform


class BaseGenerator:
    def __init__(self, loc: float, scale: float = 0) -> None:
        self.loc = loc
        self.scale = scale

    def generate(self) -> float:
        return uniform.rvs(loc=self.loc - self.scale, scale=2 * self.scale, size=1)[0]


def main() -> None:
    distr = BaseGenerator(5, 10)

    for _ in range(100):
        print(distr.generate())


if __name__ == "__main__":
    main()
