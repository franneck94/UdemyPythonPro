import argparse
import sys


def main() -> None:
    """nargs
    *. All command-line arguments present are gathered into a list.
    +. Just like *, Additionally, an error if there wasnt at least one
    """
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
        "--ages",
        help="Enter the ages",
        nargs="*",
        required=True,
    )
    parser.add_argument(
        "-n",
        "--names",
        help="Enter the names",
        nargs="*",
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
