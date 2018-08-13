class Bola:
    cor = None
    circunferencia = None
    marca = None

    def __init__(self, marca):
        self.marca = marca

    def __str__(self):
        return ",".join((str(self.cor), str(self.circunferencia), str(self.marca)))
    
    @classmethod
    def all(cls):
        return cls

class Jogador:
    nome = None
    chuteira = None
    posicao = None
    
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return ",".join((self.nome, self.chuteira, self.posicao))
 
if __name__ == '__main__':
    print(dir(Bola))
    print(dir(Jogador))
    print(id(Bola))
    print(id(Jogador))
    print(Bola.all())