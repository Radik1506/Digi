#Decimal to Binary 
exp = 20
dec = int(input(f"Decimal Number (limit of {((2 ** exp) * 2) - 1}): "))
bi = ""
decSearch = 0
res = 0
start = False
while res != dec:
    decSearch = 2 ** exp
    if (decSearch + res) > dec:
        if start == True:
            bi = bi + "0"
    elif (decSearch + res) <= dec:
        bi = bi + "1"
        start = True
        res = res + decSearch
    exp = exp - 1
while exp >= 0:
    bi = bi + "0"
    exp = exp - 1
print(f"Binary Number: {bi}")
print(f"Fact check through the bin function: {bin(dec)[2:]}")