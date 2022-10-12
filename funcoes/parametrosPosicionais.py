def funcao_com_args(arg1, arg2, *args):
    print(f"Argumento 1 é {arg1}")
    print(f"Argumento 2 é {arg2}")
    print(f"Outros argumentos {args}")


funcao_com_args(1, 2, 8, 9, 12)


def soma(maximo, *numeros):
    resultado = 0
    numeros_somados = []

    for numero in numeros:
        if (resultado + numero) > maximo:
            break
        resultado += numero
        numeros_somados.append(numero)

    return resultado, numeros_somados


resultado_soma = soma(3, 3, 4, 5, 8)
print(f"o resultado da soma é{resultado_soma}")
