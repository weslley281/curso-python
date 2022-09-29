fila = {
    '0': 'AAA',
    '1': 'BBB',
    '2': 'CCC',
    '3': 'DDD',
    '4': 'FFF',
}

print(f'Fila Inicial {fila}')

del fila['0']

print(f'Fila Atual {fila}')

valor_retirado = fila.pop('1')

print(f'Fila Retirada {valor_retirado}')
print(f'Fila Atual {fila}')

fila.popitem()
print(f'Fila Atual {fila}')

fila.clear()
print(f'Fila Atual {fila}')
