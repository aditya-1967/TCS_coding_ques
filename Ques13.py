#find whether the given number is an Armstrong number or not
def Armstrong(number):
    total = 0
    while number > 0:
        n = number % 10
        total += n ** 3
        number = number // 10
    return total
number = int(input("Enter a number: "))
print(number == Armstrong(number))
