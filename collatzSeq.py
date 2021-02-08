number = input("Enter #: ")


def collatz(number):
    if number % 2 == 0:
        return print(number //2)
    return print(3 * number + 1)

while collatz(number) != 1:
    collatz(number)
