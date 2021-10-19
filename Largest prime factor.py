# Write your code here :-)
#Project Euler 3
#magic = 100
# Miller-Rabin primality test this problem sucks

# magic = 600851475143
# i = 2

# while i * i < magic:
#    print('i is ' + str(i))
#     while magic%i == 0:
#        print('magic is ' + str(magic))
#         magic = magic / i
#     i = i + 1
# print (magic)

#select text then ctrl k to comment

#better solution found online

#Function for prime factors
def getPrimeFactors(target) :
    #create an array
    factors = []

    #start at smallest prime
    counter = 2
    #Loop until our target has factored down to base
    while (target > 1):
        #Check if target is a factor
        if target % counter == 0 :
            #Since target is a factor split to a smaller number
            target = target / counter
            #Add this to our array
            factors.append(counter)
        else :
            #Check odd numbers since even wont be prime
            counter += 1 if counter == 2 else 2
    return factors

#Choose a number to work down
target = 600851475143
factors = getPrimeFactors(target)

print('The largest prime factor of ' + str(target) + ' is ' + str(max(factors)))
print(factors)
