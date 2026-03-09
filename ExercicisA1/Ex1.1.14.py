text = "hola"
textRev = ""
pos = len(text) - 1
for i in range(len(text)):
    textRev += text[pos]
    pos -= 1
print(textRev)