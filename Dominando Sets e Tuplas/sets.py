set_1 = {1, 2, 3}
print(set_1)

set_2 = set()
print(set_2)

carteira = {'AAAA', 'BBBB', 'CCCC', 'DDDD'}
print(f'carteira inicial: {carteira}')

carteira.add('AAAA')
print(f'não acdiciona o mesmo item: {carteira}')

carteira.add('EEEE')
print(f'acdicionar item: {carteira}')

carteira.discard('AAAA')
print(f'discartando um item: {carteira}')

carteira.remove('BBBB')
print(f'remove um item: {carteira}')

carteira.pop()
print(f'remove o ultimo item: {carteira}')

carteira.clear()
print(f'remove todos itemsa: {carteira}')
