import requests
# URL de l'API per obtenir les categories
url = "https://api.chucknorris.io/jokes/categories"
# Executar la petició GET
response = requests.get(url)


# Comprovar el codi d'estat
if response.status_code == 200:  # 200 OK indica que la petició ha estat exitosa
    print("✅ Èxit!")
    # response.text conté el Body (cos de la resposta)
    print(response.text)
else:
    # Capturar errors del client (4xx) o del servidor (5xx)
    print(f"❌ Error {response.status_code}")