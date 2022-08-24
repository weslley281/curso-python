from weakref import WeakSet


lista = []

#adiciona um item a lista
lista.append("a")

nome = "weslley"
idade = 26
admin = True

itens = {
    nome,
    idade,
    admin,
}

lista.append("b")
lista.append("c")

lista.append(itens)
print(lista)

#lista.sort(1)

print(lista)

lista.remove("b")

print(lista)

print(lista[1])

nome = "Weslley Ferraz"

lista_nome = nome.split(" ")

print(nome)
print(lista_nome)

primeiro_nome = lista_nome[0]

print(primeiro_nome)