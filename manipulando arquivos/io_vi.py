arquivo = open('pessoas.csv')
dados = arquivo.read()
arquivo.close()
for dado in dados.splitlines():
    print('Nome: {}, idade: {}'.format(*dado.split(',')))