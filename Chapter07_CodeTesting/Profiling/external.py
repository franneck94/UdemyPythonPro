import numpy as np
from pyinstrument import Profiler

from vector import Vector2D


def main() -> None:
    profiler = Profiler()
    profiler.start()

    for _ in range(100_000):
        v1 = Vector2D(np.random.randint(-10, 10), np.random.randint(-10, 10))
        v2 = Vector2D(np.random.randint(-10, 10), np.random.randint(-10, 10))
        c3 = v1 + v2  # noqa

    profiler.stop()
    profiler.print()


if __name__ == "__main__":
    main()
