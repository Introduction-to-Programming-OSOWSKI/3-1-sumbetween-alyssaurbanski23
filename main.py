def sumBetween(x, y):

    total = 0

    for i in range (x + 1, y):
        total = total + i

    return total

print (sumBetween(5,7))
