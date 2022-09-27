idade = input('Digite a sua idade: ')
sexo = input('Digite a sua orientação sexual: ')
idadeInt = int(idade)

if sexo.upper() == 'M' and idadeInt >= 65:
    print('pode se aposentar')
elif sexo.upper() == 'F' and idadeInt >= 60:
    print('pode se aposentar')
elif sexo.upper() == 'M' and idadeInt < 65:
    print("Não pode se aposentar")
elif sexo.upper() == 'F' and idadeInt < 60:
    print("Não pode se aposentar")
else:
    print('Alguma das informações estão incorretas')
