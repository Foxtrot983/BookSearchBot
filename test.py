import asyncio

async def func():
    print("Hello ...")
    await asyncio.sleep(5)
    print("WOrld")

async def func2():
    print("Hello2")
    await asyncio.sleep(1)
    print("Hello2")
if __name__ == "__main__":
    task_list = (func(), func2())
    asyncio.gather(*task_list)