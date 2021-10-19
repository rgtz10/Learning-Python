# Write your code here :-)
def sumOfSquares(magic):
    value = 0
    temp = 0
    for i in range(magic+1):
        value = i * i
        temp += value
    return temp

def squareOfTheSum(magic):
    value = 0
    for i in range(magic+1):
        value += i
    answer = value * value
    return answer

print(squareOfTheSum(100) - sumOfSquares(100))
