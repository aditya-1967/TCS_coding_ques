#Check if a given number is palindrome or not
number = int(input('Enter a number: '))
number = list(str(number))
print(number == number[::-1])
