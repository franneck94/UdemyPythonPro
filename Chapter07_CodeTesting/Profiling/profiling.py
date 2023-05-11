"""Test code.
"""
import cProfile
import io
import pstats
import random
from functools import wraps
from pathlib import Path

import numpy as np

from vector import Vector2D


FILE_PATH = Path(__file__).parent.joinpath("profiling_stats.prof")


def profile(fn):
    @wraps(fn)
    def profiler(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        fn_result = fn(*args, **kwargs)
        profiler.disable()
        stream = io.StringIO()
        stats = pstats.Stats(profiler, stream=stream)
        stats.sort_stats(pstats.SortKey.TIME)
        stats.print_stats()
        print(stream.getvalue())
        stats.dump_stats(filename=FILE_PATH)
        return fn_result

    return profiler


@profile
def test_addition_own_implementation():
    for _ in range(100_000):
        v1 = Vector2D(np.random.randint(-10, 10), np.random.randint(-10, 10))
        v2 = Vector2D(np.random.randint(-10, 10), np.random.randint(-10, 10))
        c3 = v1 + v2  # noqa


def main():
    test_addition_own_implementation()


if __name__ == "__main__":
    main()
