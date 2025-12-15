from flask import Flask, request, jsonify


app = Flask(__name__)


# Base de dades temporal (memòria)
articles = []


# --- GET: obtenir tots els articles ---
@app.route('/articles', methods=['GET'])
def obtenir_articles():
    return jsonify(articles), 200




# --- POST: afegir un article nou ---
@app.route('/articles', methods=['POST'])
def afegir_article():
    global seguent_id
    dades = request.get_json()


    # Validació bàsica
    if not dades or 'nom' not in dades or 'preu' not in dades:
        return jsonify({'error': 'Falten camps obligatoris (nom, preu)'}), 400


    # Crear i afegir article
    article = {
        'nom': dades['nom'],
        'preu': dades['preu']
    }
    articles.append(article)
    print(articles)
	


    return jsonify(article), 201




if __name__ == '__main__':
    app.run(debug=True)
