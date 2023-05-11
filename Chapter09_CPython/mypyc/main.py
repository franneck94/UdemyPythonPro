import math_mypyc


def main() -> None:
    lst = [float(i) for i in range(10)]

    min_value = 2.0
    max_value = 4.0
    math_mypyc.clip_vector(lst, min_value, max_value)

    print(lst)


if __name__ == "__main__":
    main()
