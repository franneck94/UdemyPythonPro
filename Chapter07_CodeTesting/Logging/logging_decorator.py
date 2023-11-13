import time
from datetime import datetime
from functools import wraps
from typing import Any
from typing import Callable


def log(fn: Callable) -> Callable:
    @wraps(fn)
    def logger(*args: Any, **kwargs: Any) -> Any:
        time_str = datetime.utcnow().strftime("%H:%M:%S")
        try:
            fn_result = fn(*args, **kwargs)
            print(f"Called function {fn.__name__} at {time_str}")
            return fn_result  # noqa: TRY300
        except Exception as e:  # noqa: BLE001
            print(
                f"Called function {fn.__name__} at {time_str} "
                f"with an exception: '{e}'"
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
