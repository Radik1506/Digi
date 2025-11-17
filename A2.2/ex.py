#1-2
car = {
    "maker": "Porsche",
    "model": "911",
    "year": "1974"
}
print(car["maker"])
car["colour"] = "red"
del car["year"]
print(car)

#3-4
capital_pais = {
    "Spain": "Madrid",
    "Italy": "Rome",
    "Australia": "Canberra"
}
for k, v in capital_pais.items():
    print(f"The capital of {k} is {v}")

ask = input("Say a country: ")
if (ask in capital_pais):
    print(f"The capital of {ask} is {capital_pais[ask]}")
else:
    print("Not found")

#5
section = {

}
ask = input("Write a word: ")
for i in ask:
    if i in section:
        section[i] += 1
    else:
        section[i] = 1
print(section)

#6
preus1 = {'pa': 1.2, 'llet': 0.9}
preus2 = {'formatge': 2.5, 'pa': 1.1}
for k, v in preus2.items():
    if k in preus1:
        del preus1[k]
    preus1[k] = v
print(preus1)