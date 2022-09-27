cadastro = {
    'id': 1,
    'nome': 'Weslley',
    'Idade': 26,
    'compras': [
        {
            'id': 458,
            'produto': 'Arroz',
            'preco': 49.99
        }
    ]
}

print(cadastro['id'])
print(cadastro['compras'])
print(cadastro['compras'][0])
print(cadastro['compras'][0]['id'])
