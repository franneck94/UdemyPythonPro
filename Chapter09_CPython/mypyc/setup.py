from mypyc.build import mypycify
from setuptools import setup


def main() -> None:
    setup(
        name="math_mypyc",
        version="1.0.0",
        packages=["math_mypyc"],
        ext_modules=mypycify(["math_mypyc/__init__.py"]),
    )


if __name__ == "__main__":
    main()
