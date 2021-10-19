# Write your code here :-)
#Project Euler 5

#bruteforce

# i = 20
# while(i%1 != 0 or i%2 != 0 or i%3 != 0 or i%4 != 0  or i%5 != 0
# or i%6 != 0 or i%7 != 0  or i%8 != 0  or i%9 != 0  or i%10 != 0
# or i%11 != 0 or i%12 != 0  or i%13 != 0  or i%14 != 0  or i%15 != 0
# or i%16 != 0 or i%17 != 0  or i%18 != 0  or i%19 != 0  or i%20 != 0):
#     i= i+20
# print(i)


#Keep track of our factors
i = 1
for k in (range(1, 21)):
    if i % k > 0:
        for j in range(1, 21):
            #If evenly divisible
            if (i*j) % k == 0:
                #Increase prime factorization
                i *= j
                break
print (i)
