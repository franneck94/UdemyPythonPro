import dis


def function1():
    return "{} {}".format("Jan", "Schaffranek")


def function2():
    return f'{"Jan"} {"Schaffranek"}'


def main():
    dis.dis(function1)
    dis.dis(function2)


if __name__ == "__main__":
    main()
