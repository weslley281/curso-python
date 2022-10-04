def funcao_com_args(arg1, arg2, *args):
    print(f"Argumento 1 é {arg1}")
    print(f"Argumento 2 é {arg2}")
    print(f"Otros argumentos {args}")


funcao_com_args(1, 2, 8, 9, 12)
