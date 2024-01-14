# type: ignore
import asyncio


async def f(name: str) -> None:
    await asyncio.sleep(2)
    print(f"Task {name}")


async def main1() -> None:
    await f("A")
    await f("B")
    await f("C")


async def main2() -> None:
    L = await asyncio.gather(f("A"), f("B"), f("C"))  # noqa: N806

    my_tasks = [f("A"), f("B"), f("C")]
    L = await asyncio.gather(*my_tasks)  # noqa: N806
    print(L)


if __name__ == "__main__":
    # asyncio.run(main1())
    asyncio.run(main2())
