def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    number = 3 * number + 1
    print(number)
    return number

number = input("enter #: ")
while number != 1:
    number = collatz(int(number))
