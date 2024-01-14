from __future__ import annotations

from typing import Callable  # noqa: UP035


def print_list(
    values: list[int],
) -> None:
    print(values)


def function(
    values: list[int],
    print_fn: Callable[[list[int]], None],
) -> None:
    print_fn(values)


def main() -> None:
    values = [1, 2, 3]
    function(values, print_list)


if __name__ == "__main__":
    main()
