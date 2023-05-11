from __future__ import annotations

from typing import Callable
from typing import List
from typing import Optional
from typing import Union


def print_list(values: List[int]) -> None:
    print(values)


def function(values: List[int], print_fn: Callable[[List[int]], None]) -> None:
    print_fn(values)


def append_value(value: int, my_list: Optional[List[int]] = None) -> List[int]:
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
