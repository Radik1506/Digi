list_num = [2, 7, 4, 2, 5, 1, 8, 3, 9, 6, 10]
#Count numbers in list
count = 0
for x in list_num:
    if (x == 2):
        count += 1
sum = 0
print(count)
#Sum
for x in list_num:
    sum += x
print(sum)
#Max & Min
maxNum = 0
minNum = 1000
for x in list_num:
    if (x > maxNum):
        maxNum = x
    if (x < minNum):
        minNum = x
print(maxNum)
print(minNum)
#delete dupes
list_dupe = []
count = 0
for x in list_num:
    inList = False
    for y in list_dupe:
        if (x == y):
            inList = True
    if (inList == False):
        list_dupe.append(x)
    else:
        list_num.pop(count)
    count += 1
print(list_num)
#Invert
list_dupe = []
for x in list_num:
    list_dupe.insert(0, x)
print(list_dupe)
#add lists
list_num = [2, 7, 4, 5, 1]
list_num2 = [8, 3, 9, 6, 10]
list_num = list_num + list_num2
print(list_num)
#Pertinence
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
num = int(input("Tell me a number "))
count = False
for x in list_num:
    if (x == num):
        count = True
print(count)
#Orderer
list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
count = 0
for x in list_num:
    j = 0
    while (j < len(list_num) and j < count and list_num[count-j] < list_num[count-j-1]):
        tempNum = list_num[count-j-1]
        list_num[count-j-1] = list_num[count-j]
        list_num[count-j] = tempNum
        j += 1
    count += 1
print(list_num)