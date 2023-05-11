import math
import time


NUMBERS = [
    18014398777917439,
    18014398777917439,
    18014398777917439,
    18014398777917439,
    18014398777917439,
    18014398777917439,
    18014398777917439,
    18014398777917439,
    18014398777917439,
    18014398777917439,
    18014398777917439,
    18014398777917439,
]


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3, 5, 7):
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    upper_limit = int(math.sqrt(n)) + 1
    for i in range(11, upper_limit, 2):
        if n % i == 0:
            return False
    return True


def main() -> None:
    start = time.perf_counter_ns()

    for number in NUMBERS:
        result = is_prime(number)
        print(result)

    end = time.perf_counter_ns()
    print(f"Took: {(end - start) / 1000000.0} ms")


if __name__ == "__main__":
    main()
