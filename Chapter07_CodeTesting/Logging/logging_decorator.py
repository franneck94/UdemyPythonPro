import time
from collections.abc import Callable
from datetime import datetime
from datetime import timezone
from functools import wraps
from typing import Any


def log(fn: Callable) -> Callable:
    @wraps(fn)
    def logger(*args: Any, **kwargs: Any) -> Any:
        time_str = datetime.now(tz=timezone.utc).strftime("%H:%M:%S")
        try:
            fn_result = fn(*args, **kwargs)
            print(f"Called function {fn.__name__} at {time_str}")
            return fn_result
        except Exception as e:
            print(
                f"Called function {fn.__name__} at {time_str} "
                f"with an exception: '{e}'",
            )

    return logger


@log
def divide_integers(a: int, b: int) -> float:
    return a / b


def main() -> None:
    print(divide_integers(10, 0))
    time.sleep(2.0)
    print(divide_integers(10, 0))
    time.sleep(2.0)
    print(divide_integers(10, 0))


if __name__ == "__main__":
    main()
