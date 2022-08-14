#Sum of all prime number in a given range
low = int(input('Enter lower limit: '))
high = int(input('Enter upper limit: '))
prime = []
for i in range(low, high+1):
    count = 1
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            count += 1
    if count == 1:
        prime.append(i)
print(sum(prime))
