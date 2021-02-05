


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    else:
        result = 3 * number + 1
        print(result)
        return result


number = input("Enter a number: ")
while number != 1:
    number = collatz(int(number))
