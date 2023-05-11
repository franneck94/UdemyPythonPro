import numpy as np

from pyinstrument import Profiler
from vector import Vector2D


profiler = Profiler()
profiler.start()

for _ in range(100_000):
    v1 = Vector2D(np.random.randint(-10, 10), np.random.randint(-10, 10))
    v2 = Vector2D(np.random.randint(-10, 10), np.random.randint(-10, 10))
    c3 = v1 + v2

profiler.stop()
profiler.print()
