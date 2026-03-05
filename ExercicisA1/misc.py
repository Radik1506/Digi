#Input A1.2.1
text = str(input("Give me a sentence: "))
#Longitut de la frase A1.1.7
print(f"{text} has {len(text)} characters")
#Invertir la frase A1.1.10
print(text[::-1])
#Majuscules i Minuscules A1.1.13
print(text.upper())
print(text.lower())
#Contar lletres a una frase A1.1.11
count = 0
char = "a"
for a in text:
    if a == char:
        count += 1
print(f"{count} {char}'s in {text}")