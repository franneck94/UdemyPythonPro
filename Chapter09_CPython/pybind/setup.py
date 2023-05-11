from pybind11.setup_helpers import Pybind11Extension
from pybind11.setup_helpers import build_ext
from setuptools import setup


ext_modules = [
    Pybind11Extension("math_cpp_python", ["math_cpp_python/clip.cpp"])
]


def main() -> None:
    setup(
        name="math_cpp_python",
        version="1.0.0",
        ext_modules=ext_modules,
        cmdclass={"build_ext": build_ext},
    )


if __name__ == "__main__":
    main()
