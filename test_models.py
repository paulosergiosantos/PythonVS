from models import Bola
from models import Jogador

nike = Bola("Nike")
nike.cor = "Branca"
nike.circunferencia = 15

adidas = Bola("Adidas")
adidas.cor = "Amarela"
adidas.circunferencia = 15.5

print(nike)
print(adidas)
print(Bola.all())