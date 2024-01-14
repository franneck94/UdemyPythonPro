cimport cython
cimport numpy as np

import numpy as np
from cython.parallel import prange


np.import_array()


def _naive_cython_clip_vector(
    vector_in,
    min_value,
    max_value,
    vector_out,
):
    for idx in range(len(vector_in)):
        vector_out[idx] = min(max(vector_in[idx], min_value), max_value)


@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)  # Deactivate negative indexing
def _cython_clip_vector(
    float[:] vector_in,
    float min_value,
    float max_value,
    float[:] vector_out,
):
    for idx in range(len(vector_in)):
        vector_out[idx] = min(max(vector_in[idx], min_value), max_value)


@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)  # Deactivate negative indexing
def _cython_np_clip_vector(
    np.ndarray[np.float32_t, ndim=1] vector_in,
    float min_value,
    float max_value,
    np.ndarray[np.float32_t, ndim=1] vector_out,
):
    for idx in range(len(vector_in)):
        vector_out[idx] = min(max(vector_in[idx], min_value), max_value)


@cython.boundscheck(False)  # Deactivate bounds checking
@cython.wraparound(False)  # Deactivate negative indexing
def _parallel_cython_clip_vector(
    float[:] vector_in,
    float min_value,
    float max_value,
    float[:] vector_out,
):
    cdef signed int idx = 0
    cdef signed int length = len(vector_in)
    with nogil:
        for idx in prange(length):
            if vector_in[idx] < min_value:
                vector_out[idx] = min_value
            elif vector_in[idx] > max_value:
                vector_out[idx] = max_value
            else:
                vector_out[idx] = vector_in[idx]
