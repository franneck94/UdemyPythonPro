import numpy as np

import math_numba


def main() -> None:
    arr = np.array([float(i) for i in range(10)], dtype=np.float64)

    min_value = 2.0
    max_value = 4.0
    math_numba.clip_vector(arr, min_value, max_value)

    print(arr)


if __name__ == "__main__":
    main()
