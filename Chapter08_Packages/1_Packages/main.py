from my_package.computations import addition
from my_package.computations import subtraction
from my_package.printing import hello_world


def main() -> None:
    hello_world()
    print(addition(1, 1))
    print(subtraction(1, 1))


if __name__ == "__main__":
    main()
