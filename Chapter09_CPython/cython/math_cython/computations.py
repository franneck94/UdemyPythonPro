import array
from typing import List

import numpy as np

from .cython_computations import _cython_clip_vector
from .cython_computations import _cython_np_clip_vector
from .cython_computations import _naive_cython_clip_vector
from .cython_computations import _parallel_cython_clip_vector


def python_clip_vector(
    vector_in: List[float],
    min_value: float,
    max_value: float,
    vector_out: List[float],
):
    for idx in range(len(vector_in)):
        vector_out[idx] = min(max(vector_in[idx], min_value), max_value)


def naive_cython_clip_vector(
    vector_in: array.array,
    min_value: float,
    max_value: float,
    vector_out: array.array,
):
    _naive_cython_clip_vector(vector_in, min_value, max_value, vector_out)


def cython_clip_vector(
    vector_in: array.array,
    min_value: float,
    max_value: float,
    vector_out: array.array,
):
    _cython_clip_vector(vector_in, min_value, max_value, vector_out)


def parallel_cython_clip_vector(
    vector_in: array.array,
    min_value: float,
    max_value: float,
    vector_out: array.array,
):
    _parallel_cython_clip_vector(vector_in, min_value, max_value, vector_out)


def cython_np_clip_vector(
    vector_in: np.ndarray,
    min_value: float,
    max_value: float,
    vector_out: np.ndarray,
):
    _cython_np_clip_vector(vector_in, min_value, max_value, vector_out)
