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


def main():
    print('** Standard incrementing generator **')
    counter = 0
    store = []
    gennie = lazy_range(10)
    while counter < 4:
        p = next(gennie)
        print(p)
        store.append(p)
        counter += 1


    print('** Sending information back into generator **')

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




if __name__ == '__main__':
    main()
