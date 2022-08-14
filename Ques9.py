#Check if a number is a perfect square or not
number = int(input("Enter a number: "))
flag = 0
for i in range(number//2 + 1):
    if number == i*i:
        print('True')
        flag += 1
if flag == 0:
    print('False')
