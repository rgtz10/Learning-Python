# Write your code here :-)
#Project Euler 1
sum = 0
for var in range(1000):
    if var % 3 == 0 or var % 5 == 0:
        sum += var
print(sum)
