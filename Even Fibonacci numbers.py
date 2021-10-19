# Write your code here :-)
#project euler 2
x = 1
y = 2
temp = 0
sum = 2
while temp <= 4000000:
    temp = 0
    temp = x + y
    if temp % 2 == 0:
        sum += temp
    x = y
    y = temp
print(sum)

