text1 = "Hello World"
text2 = "Hola Mon!!!"
count = 0
for i in range(min(len(text1), len(text2))):
    if text1[i] == text2[i]:
        count += 1
print(count)