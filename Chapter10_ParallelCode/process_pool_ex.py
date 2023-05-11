import math
import time
from concurrent.futures import ProcessPoolExecutor


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


def main():
    start = time.perf_counter_ns()

    with ProcessPoolExecutor() as ex:
        for number, prime in zip(NUMBERS, ex.map(is_prime, NUMBERS)):
            print(f"{number} is prime: {prime}")

    end = time.perf_counter_ns()
    print(f"time: {(end - start) / 1000000.0} ms")


if __name__ == "__main__":
    main()
