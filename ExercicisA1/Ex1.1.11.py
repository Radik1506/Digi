text "atggatcattta"
count = 0
char = "a"
for a in text:
    if a == char:
        count += 1
print(f"{count} {char}'s in {text}")