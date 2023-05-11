from __future__ import annotations

from typing import Any
from typing import Callable
from typing import Union


def f(*args: int, **kwargs: Union[int, float]) -> None:
    print(f"{args}, {kwargs}")


def call(f: Callable[..., None], *args: int, **kwargs: int) -> None:
    return f(*args, **kwargs)


def main() -> None:
    call(f, 1, 2, 3, a=1, b=2, c=3)


if __name__ == "__main__":
    main()
