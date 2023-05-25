from time import time

import codon


@codon.jit
def clip_vector_codon(
    a: list[float], min_value: float, max_value: float
) -> list[float]:
    len_ = len(a)
    for i in range(len_):
        if a[i] < min_value:
            a[i] = min_value
        elif a[i] > max_value:
            a[i] = max_value
    return a


def clip_vector(
    a: list[float], min_value: float, max_value: float
) -> list[float]:
    len_ = len(a)
    for i in range(len_):
        if a[i] < min_value:
            a[i] = min_value
        elif a[i] > max_value:
            a[i] = max_value
    return a


lst = [float(i) for i in range(100_000)]
min_value = -1.0
max_value = 1.0

t0 = time()
for _ in range(1_000):
    clip_vector_codon(lst, min_value, max_value)
t1 = time()
print(f"[python] took {(t1 - t0) / 10_000} seconds")

t0 = time()
for _ in range(1_000):
    clip_vector(lst, min_value, max_value)
t1 = time()
print(f"[codon]  took {(t1 - t0) / 10_000} seconds")
