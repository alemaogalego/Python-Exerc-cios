class Musica():
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao


musica1 = Musica('Batis', 'Predo', '389')

print(vars(musica1))