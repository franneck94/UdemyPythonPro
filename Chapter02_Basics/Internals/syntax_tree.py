def function1():
    return "{} {}".format("Jan", "Schaffranek")


def function2():
    return f'{"Jan"} {"Schaffranek"}'


def main():
    function1()
    function2()


if __name__ == "__main__":
    main()
