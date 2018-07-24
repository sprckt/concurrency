#! /usr/bin/env python

import asyncio
import time


async def countdown(task, n):

    while n > 0:
        print(f'T-minus {n}, "(Task: {task})"')
        await asyncio.sleep(1)
        n -= 1


async def print_after(msg, secs):
    await asyncio.sleep(secs)
    print(msg)


async def orchestrate():
    await asyncio.gather(
        print_after("Super", 1),
        print_after("Baddies", 3),
        print_after("Films", 2),
        countdown("C", 3)
    )
    print('Finished')


async def compute(x, y):
    print(f"Computing sum of {x} and {y}")
    await asyncio.sleep(1)
    return x + y


async def squaring(x, y):
    result = await compute(x, y)
    print(f"{x} + {y} = {result}")
    print(f"Square of results = {result ** 2}")
    return


async def process_pipeline(data):
    print(f"Input into Pipeline {data}")
    results = await level_a(data)
    print(f"Results from level Process Pipeline {results}")
    return results


async def level_a(data):
    level_b_inputs = data, data ** 2, data ** 4
    results = await asyncio.gather(*[level_b(val) for val in level_b_inputs])
    print(f"Results from level A: {results}")
    return results


async def level_b(data):

    print(f"Coming at you from level B: {data}")
    time.sleep(2)

    return data + 1


async def process_records(rec, shard_id):

    time.sleep(1)
    record_body = rec['Records']
    print(f'Records to process: Shard #{shard_id} {record_body}')

    return 'Written into DB'


async def sample_function(x):

    print('Start function')
    await asyncio.sleep(1)
    print('End Function')
    return x ** 2


async def caller():
    result = await sample_function(10)
    result = float(result)
    print(f"{result}")


def main():

    print('\n** Basic useage of Tasks **')

    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(countdown("A", 3)),
        asyncio.ensure_future(countdown("B", 2))
    ]
    loop.run_until_complete(asyncio.wait(tasks))

    # Coroutine passed to another one
    print('\n** Use another coroutine control your initial one  **')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(orchestrate())

    # Chaining coroutines together
    print("\n** Chaining coroutines together **")
    loop.run_until_complete(squaring(3, 4))

    # Put together a calculation process
    print("\n** Putting together a pipeline **")

    input = [1, 10, 100]
    # group_tasks = [process_pipeline(i) for i in input]

    result = loop.run_until_complete(asyncio.gather(*[process_pipeline(i) for i in input]))
    print(f"Final result: {result}")

    loop.close()


if __name__ == '__main__':
    main()