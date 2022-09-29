familia = {
    'pai': 'Fulano de Tal',
    'mae': 'Beltrana de Tal',
    'filho': 'Celtrano de Tal',
    'filha': 'Deltrana de Tal',
}

print(familia)

copia_familia = familia.copy()

print(f"Compia da Familia: {copia_familia}")

itens = familia.items()

print(f"Itens: {itens}")

for item in itens:
    print(item)

chaves = familia.keys

print(f"Chaves: {chaves}")

for chave in chaves:
    print(chave)

valores = familia.values

print(f"Chaves: {valores}")

for valor in valores:
    print(valor)
