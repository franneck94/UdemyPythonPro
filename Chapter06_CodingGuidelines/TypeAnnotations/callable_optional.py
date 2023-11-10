from __future__ import annotations

from typing import Callable
from typing import List  # noqa: F401
from typing import Optional  # noqa: F401
from typing import Union  # noqa: F401


def print_list(values: list[int]) -> None:
    print(values)


def function(values: list[int], print_fn: Callable[[list[int]], None]) -> None:
    print_fn(values)


def append_value(value: int, my_list: list[int] | None = None) -> list[int]:
    if my_list:
        my_list.append(value)
    else:
        my_list = [value]
    return my_list


if __name__ == "__main__":
    values = [1, 2, 3]
    expand_ratio = 2

    function(values, print_list)

    my_list = append_value(1)
    print(my_list)
    my_list = append_value(2, my_list)
    print(my_list)
    my_list = append_value(3, my_list)
    print(my_list)
