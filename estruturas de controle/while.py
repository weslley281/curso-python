from random import randint


capacidadeMaxima = 1000

balde = 0

while balde <= capacidadeMaxima:
    volume = randint(95, 100)
    print(f"O copo foi encido com {volume}")
    balde += volume
    print(f"O balde está com {balde}")
