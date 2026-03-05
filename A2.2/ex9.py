alumnes = {
    'Marta': {'edat': 18, 'nota_final': 8.5},
    'Joan': {'edat': 19, 'nota_final': 6.7}
}
millor = max(alumnes, key=lambda nom: alumnes[nom]['nota_final'])
print(f"L'alumne amb millor nota és {millor}")