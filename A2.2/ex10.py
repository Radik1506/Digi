frase = input("Escriu una frase: ")
frequencia = {}
for paraula in frase.split():
    frequencia[paraula] = frequencia.get(paraula, 0) + 1
print(frequencia)