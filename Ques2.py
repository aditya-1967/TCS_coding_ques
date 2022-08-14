#Consider the following series: 0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8
#Find nth term
n = int(input('Enter term: '))
if n % 2 != 0:
    term = (n+1)/2
    print(int(2**(term-1)))
else:
    term = n/2
    print(int(term-1))
