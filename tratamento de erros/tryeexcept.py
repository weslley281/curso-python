def divide_dois_numeros(dividendo, divisor):
    return dividendo/divisor

try:
    n1 = int(input('digite o dividendo: '))
    n2 = int(input('digite o divisor: '))

    resultado = divide_dois_numeros(n1, n2)
except TypeError:
    print("Erro de Tipagem")
except ZeroDivisionError:
    print("Não suporta divisão por zero")
except Exception:
    print("Ocorreu um erro")
else:
    print(resultado)
finally:
    print("O programa terminou")