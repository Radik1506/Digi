notes = {'Anna': [8, 9, 7], 'Pau': [5, 6, 6]}
for nom, llista in notes.items():
    mitjana = round(sum(llista) / len(llista), 2)
    print(f"{nom} → {mitjana}")