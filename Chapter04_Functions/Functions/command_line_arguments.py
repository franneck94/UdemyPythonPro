import argparse


def check_for_boolean_value(val):
    if val == "True":
        return True
    else:
        return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--age", help="Enter your age (int)", type=int, required=True
    )
    parser.add_argument(
        "--name", help="Enter your name (str)", type=str, required=True
    )
    parser.add_argument(
        "--admin",
        help="Are your an admin? (bool)",
        type=check_for_boolean_value,
        required=False,
        default=False,
    )
    args = parser.parse_args()

    age = args.age
    name = args.name
    is_admin = args.admin

    print(age, type(age))
    print(name, type(name))
    print(is_admin, type(is_admin))


if __name__ == "__main__":
    main()
