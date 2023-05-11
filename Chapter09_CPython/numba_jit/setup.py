from distutils.core import setup

from math_numba import cc


def main() -> None:
    setup(
        name="math_numba",
        version="1.0.0",
        ext_modules=[cc.distutils_extension()],
    )


if __name__ == "__main__":
    main()
