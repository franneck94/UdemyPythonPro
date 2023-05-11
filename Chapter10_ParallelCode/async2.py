import asyncio


async def f(name):
    await asyncio.sleep(2)
    print(f"Task {name}")


async def main1():
    L1 = await f("A")
    L2 = await f("B")
    L3 = await f("C")
    print(L1, L2, L3)


async def main2():
    L = await asyncio.gather(f("A"), f("B"), f("C"))

    my_tasks = [f("A"), f("B"), f("C")]
    L = await asyncio.gather(*my_tasks)
    print(L)


if __name__ == "__main__":
    # asyncio.run(main1())
    asyncio.run(main2())
