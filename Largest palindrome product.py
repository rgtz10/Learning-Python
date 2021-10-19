# Write your code here :-)
#Project Euler 4
from datetime import datetime
startTime = datetime.now()

lowest = 100
highest = 999
bigPali = 0

#Test product of 3 digit numbers
for i in range(lowest,highest):
    for j in range(lowest,highest):
        #Find Product
        prod = i * j
        test = prod
        reverse = 0
        #create the reverse to test if palindrome
        while prod > 0:
            digit = prod % 10
            reverse = (reverse * 10) + digit
            prod = prod // 10
        #Test palindrome and if larger
        if test == reverse and test > bigPali:
            bigPali = test
print(bigPali)

print(datetime.now() - startTime)
