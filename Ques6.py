#Check if a given number is strong or not
#A number is strong when it is equal to the sum of factorials of its digits
#ex 145 = 1! + 4! + 5!

def fact(num):
    if num <= 1:
        return 1
    return num * fact(num-1)
number = int(input("Enter a number: "))
total = 0
num = number
while number > 0:
    n = number % 10
    total += fact(n)
    number = number // 10
print(total == num)
