#Find GCD of 2 numbers
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
i = num1 if num1 < num2 else num2
for j in range(i, 0, -1):
    if num1 % j == 0 and num2 % j == 0:
        print("GCD:", j)
        break
