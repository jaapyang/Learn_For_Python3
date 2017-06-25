
""" TODO: how to get a collatz number list """

def collatz(number):
    """ TODO: how to get a collatz number list """
    result = 0
    if number == 1:
        return None
    if number % 2 == 0:
        result = number // 2
    else:
        result = int(3 * number + 1)

    print(result)
    collatz(result)


number = int(input())
collatz(number)
