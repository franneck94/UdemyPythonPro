from __future__ import annotations

from typing import Any  # noqa: F401
from typing import List
from typing import Tuple
from typing import Union


Number = Union[int, float]


def append_list(lst: list[Number], val: Number) -> None:
    lst.append(val)


def print_3d_tuple(tpl: tuple[Number, bool, str]) -> None:
    for val in tpl:
        print(val)


if __name__ == "__main__":
    lst: list[Union[int, float]] = [1, 2, 3]
    tpl = (1, True, "")

    append_list(lst, 4)
    print_3d_tuple(tpl)
