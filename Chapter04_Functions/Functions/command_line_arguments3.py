import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        description="My pip tool",
        prog="pip",
    )

    subparsers = parser.add_subparsers(
        title="Sub Parsers",
        description="Available subcommands",
        dest="subcommand",
    )

    subparser_install = subparsers.add_parser(
        "install",
        help="Pip Install command",
    )
    subparser_install.add_argument(
        "NAME",
        type=str,
        help="package to install",
    )

    subparser_list = subparsers.add_parser(
        "list",
        help="Pip List Command",
    )
    subparser_list.add_argument(
        "--verbose",
        help="Verbose print",
        action="store_true",
    )

    args = parser.parse_args()

    if args.subcommand == "install":
        print(f"command: pip {args.subcommand} {args.NAME}")
    elif args.subcommand == "list":
        print(f"command: pip {args.subcommand}")
    else:
        print("No subcommand specified.")


if __name__ == "__main__":
    main()
