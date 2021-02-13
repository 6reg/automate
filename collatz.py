def collatz(number):
        if number % 2 == 0:
                number = number // 2
                print(number)
                return number
        number = 3 * number + 1
        print(number)
        return number

while True:
    try:
        number = int(input("enter #: "))
    except ValueError:
        print("Enter an int")
    else: 
        break

while number != 1:
    number = collatz(number)
