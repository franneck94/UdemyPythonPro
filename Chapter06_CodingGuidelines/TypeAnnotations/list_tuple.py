from __future__ import annotations


def append_list(
    lst: list[int | float],
    val: int | float,
) -> None:
    lst.append(val)


def print_3d_tuple(
    tpl: tuple[int | float, bool, str],
) -> None:
    for val in tpl:
        print(val)


def main() -> None:
    lst: list[int | float] = [1, 2, 3]
    tpl = (1, True, "")

    append_list(lst, 4)
    print_3d_tuple(tpl)


if __name__ == "__main__":
    main()
