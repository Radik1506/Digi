text = str(input("Give me a sentence: "))
print(f"{text} has {len(text)} characters")
print(text[::-1])
print(text.upper())
print(text.lower())
count = 0
char = "a"
for a in text:
    if a == char:
        count += 1
print(f"{count} {char}'s in {text}")