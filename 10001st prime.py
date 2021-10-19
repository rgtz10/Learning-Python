# Write your code here :-)
from math import sqrt

primes =[2,3,5,7,11,13]

def inArray(x,arr):
    for k in range(0,len(arr)):
        if x == primes[k]:
            return True
    return False

def primeGenerator(n):
    p = 13
    if n < 7:
        return primes[n-1]

    while len(primes) < n:
        p+=2
        isPrime = True
        for i in range(3, int(sqrt(p)) + 1, 2):
            if p % i == 0:
                isPrime = False
                break
        if (inArray(p,primes)) == False and isPrime:
            primes.append(p)
primeGenerator(10001)
print(primes[-1])
