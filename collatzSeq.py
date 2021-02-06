
def collatz(num):
    if num % 2 == 0:
        print(num // 2)
        return num // 2
    else:
        result = 3 * num + 1
        print(result)
        return result

num = input("Enter a number: ")
while num != 1:
    num = collatz(int(num))
