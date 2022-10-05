def monta_computador(cpu, memoria, hd, monitor="sansung", **maisargs):
    print(
        f"O computador montado foi \n CPU: {cpu} \n Memória: {memoria}Gb \n HD: {hd}Tb \n Monitor: {monitor}"
    )

    for chave, arg in maisargs.items():
        print(f"{chave}: {arg}")


monta_computador(
    cpu="Core i7",
    hd=2,
    memoria=16,
    teclado="multilaser",
    mouse="da Dataplus",
)
