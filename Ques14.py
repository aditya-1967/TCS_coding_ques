#Write a program to generate Fibonacci Series.
n = int(input('Enter the number of terms: '))
a, b = 0, 1
for i in range(1, n+1):
    print(a, end = " ")
    next = a + b
    a = b
    b = next
