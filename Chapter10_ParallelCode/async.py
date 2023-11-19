import asyncio
import sys


async def foo() -> int:
    print("start foo")
    await asyncio.sleep(2.0)
    print("end foo")
    return 0


async def bar() -> int:
    print("start bar")
    await asyncio.sleep(4.0)
    print("end bar")
    return 0


async def main_await() -> int:
    print("before await foo")
    await foo()
    print("after await foo")
    return 0


async def main_task() -> int:
    task = asyncio.create_task(foo())
    i = 2
    j = i * 2
    print(j)
    await task
    return 0


async def main_future() -> int:
    task_foo = asyncio.create_task(foo())
    task_bar = asyncio.create_task(bar())
    ret_foo = await task_foo
    print(ret_foo)
    ret_bar = await task_bar
    print(ret_bar)
    return 0


def main() -> None:
    # code = asyncio.run(main_await())
    # code = asyncio.run(main_task())
    code = asyncio.run(main_future())
    sys.exit(code)


if __name__ == "__main__":
    main()
