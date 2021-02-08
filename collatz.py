def collatz(number):
    if number % 2 == 0:
       return print(number // 2)
    return print(3 * number + 1)

collatz(5)
collatz(6)

