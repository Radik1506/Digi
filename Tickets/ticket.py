from datetime import datetime

class Usuari:
    def __init__(self, nom, email, contrasenya):
        self.nom = nom
        self.email = email
        self.__contrasenya = contrasenya 

    def registrar(self):
        return f"Usuari {self.nom} registrat amb èxit."

    def iniciar_sessio(self, email, password):
        if self.email == email and self.__contrasenya == password:
            return True
        return False

class Client(Usuari):
    def __init__(self, nom, email, contrasenya):
        super().__init__(nom, email, contrasenya)
        self.historial_compres = []

    def cercar_esdeveniment(self, llista_esdeveniments, nom):
        return [e for e in llista_esdeveniments if nom.lower() in e.nom.lower()]

    def comprar_entrada(self, entrada, pagament):
        if entrada.estat == "Disponible":
            entrada.estat = "Venuda"
            self.historial_compres.append(entrada)
            return f"Compra confirmada per a l'esdeveniment: {entrada.esdeveniment_nom}"
        return "L'entrada ja no està disponible."

class Administrador(Usuari):
    def crear_esdeveniment(self, nom, descripcio, data, ubicacio, n_entrades):
        nou_ev = Esdeveniment(nom, descripcio, data, ubicacio, n_entrades)
        return nou_ev

    def modificar_esdeveniment(self, esdeveniment, nou_nom):
        esdeveniment.nom = nou_nom
        return f"Esdeveniment actualitzat a: {nou_nom}"

    def eliminar_esdeveniment(self, llista, esdeveniment):
        llista.remove(esdeveniment)
        return "Esdeveniment eliminat."

class Esdeveniment:
    def __init__(self, nom, descripcio, data, ubicacio, n_entrades):
        self.nom = nom
        self.descripcio = descripcio
        self.data = data
        self.ubicacio = ubicacio
        self.entrades_disponibles = n_entrades
        self.entrades = [Entrada(15.0, self.nom) for _ in range(n_entrades)]

    def actualitzar_disponibilitat(self):
        self.entrades_disponibles = sum(1 for e in self.entrades if e.estat == "Disponible")
        return self.entrades_disponibles

class Entrada:
    def __init__(self, preu, esdeveniment_nom):
        self.preu = preu
        self.esdeveniment_nom = esdeveniment_nom
        self.estat = "Disponible"

class Pagament:
    def __init__(self, import_total, metode):
        self.import_total = import_total
        self.metode = metode
        self.data_pagament = datetime.now()

    def processar_pagament(self):
        return f"Pagament de {self.import_total}€ processat correctament via {self.metode}."