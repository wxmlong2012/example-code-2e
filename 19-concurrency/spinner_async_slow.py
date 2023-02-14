# spinner_async.py

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/675659.html

# tag::SPINNER_ASYNC_TOP[]
import asyncio
import itertools
import time


async def spin(msg: str) -> None:  # <1>
    print("start spinning")
    for char in itertools.cycle(r'\|/-'):
        status = f'{char} {msg}'
        print(status)
        try:
            await asyncio.sleep(0.5)  # <2>
        except asyncio.CancelledError:  # <3>
            print("spinner will be broken ...")
            break
    blanks = ' ' * len(status)
    print(f'\r{blanks}\r', end='')
async def slow() -> int:
    print("start slow process")
    await asyncio.sleep(3)  # <4>
    return 42
# end::SPINNER_ASYNC_TOP[]

# tag::SPINNER_ASYNC_START[]
def main() -> None:  # <1>
    result = asyncio.run(supervisor())  # <2>
    print(f'Answer: {result}')

async def supervisor() -> int:  # <3>
    spinner = asyncio.create_task(spin('thinking!'))  # <4>
    print(f'spinner object: {spinner}')  # <5>
    result = await slow()  # <6>

    print("0.8 wait starts")
    await asyncio.sleep(0.8)
    print("0.8 wait ends")
    print("start cancel spinning")
    spinner.cancel() # <7>

    return result

if __name__ == '__main__':
    main()
# end::SPINNER_ASYNC_START[]
