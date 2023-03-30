
from scipy.stats import uniform


class UniformDistribution:
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b
        self.scale = self.b - self.a

    def generate(self):
        return uniform.rvs(loc=self.a, scale=self.scale, size=1)[0]


def main():
    distr = UniformDistribution(5, 10)

    for _ in range(100):
        print(distr.generate())


if __name__ == "__main__":
    main()
