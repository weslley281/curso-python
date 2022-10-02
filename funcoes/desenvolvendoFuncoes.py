def escreva(nome, idade, emprego):
    print(
        f"Olá meu nome {nome} e tenho {idade} anos, e trabalho com {emprego}")


escreva('Weslley', 26, 'Full Stack Software Developer Engineer')
escreva('Emanuel', 21, 'Engenheiro Elétrico')


def soma(n1, n2):
    return n1 + n2


resultado = soma(10, 2)
print(f"O resultado da soma é: {resultado}")


def calculaMedia(notas):
    media = sum(notas) / len(notas)
    return media


resultadoMedia = calculaMedia([10, 10, 8.5])
print(f"O resultado da média é: {resultadoMedia}")
