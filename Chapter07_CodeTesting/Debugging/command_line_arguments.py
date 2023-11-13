import argparse
import sys


def main() -> None:
    print(f"argv: {sys.argv}")
    print(f"argc: {len(sys.argv)}")

    parser = argparse.ArgumentParser(
        prog="ProgramName",
        usage="How to",
        description="What the program does",
        epilog="Text at the bottom of help",
    )
    parser.add_argument(
        "-a",
        "--age",
        help="Enter your age (int)",
        type=int,
        required=True,
    )
    parser.add_argument(
        "-n",
        "--name",
        help="Enter your name (str)",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        help="Verbose print",
        action="store_true",
    )
    args = parser.parse_args()

    age = args.age
    name = args.name
    verbose = args.verbose

    if verbose:
        print(age, type(age))
        print(name, type(name))
    else:
        print(age)
        print(name)


if __name__ == "__main__":
    main()
