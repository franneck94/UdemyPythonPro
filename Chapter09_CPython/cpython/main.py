import math_cpython


def main() -> None:
    lst = [float(i) for i in range(10)]

    min_value = 2.0
    max_value = 4.0
    math_cpython.clip_vector(lst, min_value, max_value)
    print(lst)

    lst1 = [float(i) for i in range(3)]  # 0, 1, 2
    lst2 = [float(i) * 2.0 for i in range(3)]  # 0, 2, 4
    result = math_cpython.add_vectors(lst1, lst2)
    print(result)


if __name__ == "__main__":
    main()
