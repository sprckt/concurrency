#! /usr/bin/env python3


def lazy_range(up_to):
    """
    Generator to return the sequence of
    integers from 0 to up_to, exclusive.
    """
    index = 0
    while index < up_to:
        yield index
        index += 1


def jumping_range(up_to):
    """
    Generator for the sequence of integers
    from 0 to up_to, exclusive.
    Sending a value into the generator will
    shift the sequence by that amount.
    """
    index = 0
    while index < up_to:
        jump = yield index
        print('Jump value: {}'.format(jump))
        if not jump:
            jump = 1
        index += jump


def grep(pattern):
    print(f'\n ** Looking for {pattern} **')

    while True:
        line = yield
        if pattern in line:
            print(f'Found "{pattern}" in line')


def bottom_stack():
    return (yield 'end_flag')


def middle_stack():
    return (yield from bottom_stack())


def top_stack():
    return (yield from middle_stack())


def main():

    # Simple generator example
    print('\n** Standard incrementing generator **')
    counter = 0
    store = []
    gennie = lazy_range(10)
    while counter < 4:
        p = next(gennie)
        print(p)
        store.append(p)
        counter += 1

    # Sending input into a generator (also known as a coroutine)
    print('\n** Sending information back into generator **')

    jump_gennie = jumping_range(10)

    print('Normal (jump) generators')
    print(next(jump_gennie))
    print(next(jump_gennie))

    print('Send 4')
    print(jump_gennie.send(4))
    print(next(jump_gennie))
    print('Send -2')
    print(jump_gennie.send(-2))
    print(next(jump_gennie))

    # Sending more data into generator
    g = grep("rocks")
    # Prime this
    next(g)
    g.send('Get you honey')
    g.send('Get your rocks off')
    g.send('That is all')

    # Sending items up and down the a message stack
    print('\n** Yield from to send up and down the stack **')
    top = top_stack()
    value = next(top)
    print(f'Value from the top: {value}')

    # Now lets send something back into the message stack
    try:
        value = top.send(value + ' - back at you')
    except StopIteration as exc:
        value = exc.value
    print(f'Value sent back into stack: {value}')


if __name__ == '__main__':
    main()
