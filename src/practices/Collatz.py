
""" TODO: how to get a collatz number list """

def collatz(number):
    """ TODO: how to get a collatz number list """
    if number == 1:
        return None
    if number % 2 == 0:
        number == int(number / 2)
    else:
        number = int(3 * number + 1)

    print(number)
    collatz(number)


number = int(input())
collatz(number)
