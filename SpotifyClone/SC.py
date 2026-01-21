class Artista:
    def __init__(self, nom ="", estil="Desconegut"):
        self.nom = nom
        self.estil = estil
        self.albums = []


    def afegir_album(self, album):
        self.albums.append(album)


    def llistar_albums(self):
        for album in self.albums:
            print(f"- {album}")

class Album:
    def __init__(self, id, titol, data_llancament, artista):
        self.id = id
        self.titol = titol
        self.data_llancament = data_llancament
        self.artista = artista
        self.cancons = []
        artista.afegir_album(self)

    def afegir_canco(self, canco):
        self.cancons.append(canco)

    def __str__(self):
        return f"{self.titol} ({self.data_llancament})"

class Canco:
    def __init__(self, id, titol, durada, album):
        self.id = id
        self.titol = titol
        self.durada = durada
        self.album = album
        album.afegir_canco(self)

    def __str__(self):
        return f"{self.titol} - {self.durada} min"


# Objecte a
a = Artista("Dub Inc","Reggae")
print(a.nom)
print(a.estil)


# Objecte b
b = Artista("Jaco Pastorius")
print(b.nom)
print(b.estil)


# Objecte c
c = Artista(estil="Jazz")
print(c.nom)
print(c.estil)