import array
from typing import Any

import numpy as np

import math_cython


NUM_ELEMENTS = 100_000
LST = [float(i) for i in range(NUM_ELEMENTS)]
NP_ARR = np.array(list(range(NUM_ELEMENTS))).astype(np.float32)
PY_ARR = array.array("f", list(range(NUM_ELEMENTS)))


NUM_ROUNDS = 50
NUM_ITERATIONS = 100


# def test_python_clip(benchmark: Any) -> None:
#     benchmark.pedantic(
#         math_cython.python_clip_vector,
#         args=(LST, -1.0, 1.0, LST),
#         rounds=NUM_ROUNDS,
#         iterations=NUM_ITERATIONS,
#     )


def test_numpy_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        np.clip,
        args=(NP_ARR, -1.0, 1.0, NP_ARR),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )


def test_naive_cython_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_cython.naive_cython_clip_vector,
        args=(PY_ARR, -1.0, 1.0, PY_ARR),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )


def test_cython_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_cython.cython_clip_vector,
        args=(PY_ARR, -1.0, 1.0, PY_ARR),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )


def test_parallel_cython_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_cython.parallel_cython_clip_vector,
        args=(PY_ARR, -1.0, 1.0, PY_ARR),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )


def test_cython_np_clip(benchmark: Any) -> None:
    benchmark.pedantic(
        math_cython.cython_np_clip_vector,
        args=(NP_ARR, -1.0, 1.0, NP_ARR),
        rounds=NUM_ROUNDS,
        iterations=NUM_ITERATIONS,
    )
