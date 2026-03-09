preus = {'motxilla': 45, 'llapis': 1, 'calculadora': 25}
cars = {producte: preu for producte, preu in preus.items() if preu > 20}
print(cars)