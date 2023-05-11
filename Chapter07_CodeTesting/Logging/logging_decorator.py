import time
from datetime import datetime
from functools import wraps


def log(fn):
    @wraps(fn)
    def logger(*args, **kwargs):
        time_str = datetime.utcnow().strftime("%H:%M:%S")
        try:
            fn_result = fn(*args, **kwargs)
            print(f"Called function {fn.__name__} at {time_str}")
            return fn_result
        except Exception as e:
            print(
                f"Called function {fn.__name__} at {time_str} "
                f"with an exception: '{e}'"
            )

    return logger


@log
def divide_integers(a: int, b: int) -> float:
    result = a / b
    return result


def main() -> None:
    print(divide_integers(10, 0))
    time.sleep(2.0)
    print(divide_integers(10, 0))
    time.sleep(2.0)
    print(divide_integers(10, 0))


if __name__ == "__main__":
    main()
