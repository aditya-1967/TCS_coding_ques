#Consider the following series: 1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187…
#Find nth term
n = int(input('Enter term: '))
if n % 2 != 0:
    term = (n+1)/2
    print(int(2**(term-1)))
else:
    term = n/2
    print(int(3**(term-1)))
