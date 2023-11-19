from setuptools import Extension
from setuptools import find_packages
from setuptools import setup


ext = Extension(name="math_cpython", sources=["math_cpython/clip.c"])

setup_args = {
    "packages": find_packages(where="math_cpython"),
    "ext_modules": [ext],
}

setup(**setup_args)
