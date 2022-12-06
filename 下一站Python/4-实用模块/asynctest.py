from time import strftime, sleep
from random import randint
import asyncio

def f(name, n):  # 一个普通的函数
    print(name, strftime("%X"), "START", n)
    for i in range(n):
        sleep(1)
    print(name, strftime("%X"), "END")

async def fcpu(name, n):  # 异步函数（模拟CPU密集型）
    print(name, strftime("%X"), "START", n)
    for i in range(n):
        sleep(1)  # 普通的sleep，啥都不干，但要占着CPU
    print(name, strftime("%X"), "END")

async def fio(name, n):  # 异步函数（模拟IO密集型）
    print(name, strftime("%X"), "START", n)
    for i in range(n):
        await asyncio.sleep(1)  # 异步sleep，啥都不干，可以让出CPU
    print(name, strftime("%X"), "END")

async def main():
    print(f"started main at {strftime('%X')}")
    async with asyncio.TaskGroup() as tg:
        for i in range(5):
            #tg.create_task(fio(f"f{i:02d}", randint(1, 5)))
            tg.create_task(asyncio.to_thread(f, f"f{i:02d}", randint(1, 5)))
    print(f"finished main at {strftime('%X')}")

asyncio.run(main())