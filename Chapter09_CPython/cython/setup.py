import platform

import numpy as np
from Cython.Build import cythonize
from setuptools import Extension
from setuptools import setup


if platform.system() == "Windows":  # noqa: SIM108
    OPEN_MP = "/openmp"
else:
    OPEN_MP = "-fopenmp"


CYTHON_EXTENSIONS = [
    Extension(
        name="math_cython.cython_computations",
        sources=["math_cython/cython_computations.pyx"],
        extra_compile_args=[OPEN_MP],
        extra_link_args=[OPEN_MP],
    )
]

EXT_MODULES = cythonize(CYTHON_EXTENSIONS, language_level="3")


def main() -> None:
    setup(
        name="math_cython",
        version="0.1.0",
        packages=["math_cython"],
        ext_modules=EXT_MODULES,
        include_dirs=[np.get_include()],
    )


if __name__ == "__main__":
    main()
