#Check if a given number is prime or not
number = int(input("Enter a number: "))
flag = 1
for i in range(2, int(number**0.5 + 1)):
    if number % i == 0:
        flag += 1
if flag != 1:
    print("False")
else:
    print('True')
