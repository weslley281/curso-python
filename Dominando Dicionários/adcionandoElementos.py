from tkinter import font


computador = {
    'cpu': 'core i7',
    'ram': 'DD4 16GB',
    'ssd': 'Sansung 1TB',
    'gpu': 'RTX 2080ti',
}

print(f"Computador v1: {computador}")

computador['ram'] = 'DDR5 32Gb'

print(f'Computador v2: {computador}')

computador['fonte'] = 'Fonte 600W'

print(f'Computador v3: {computador}')

computador.update({'fonte': 'Fonte 800W', 'gpu': 'GTX 710'})

print(f'Computador v4: {computador}')
