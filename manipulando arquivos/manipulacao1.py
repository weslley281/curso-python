# text = 'Jornada Python'
#
# arquivo_w = open("C:\\Users\\Wesll\\Documents\\apps\\curso-python\\manipulando arquivos\\dados.txt", 'w')
#
# escreva = arquivo_w.write(text)
#
# if(escreva):
#     print("Escreveu")

# arquivo_r = open("C:\\Users\\Wesll\\Documents\\apps\\curso-python\\manipulando arquivos\\dados.txt", 'r')
#
# leitura = arquivo_r.read()
#
# if(leitura):
#     print(leitura)

novo_texto = "\n mais texto"

arquivo_a = open("C:\\Users\\Wesll\\Documents\\apps\\curso-python\\manipulando arquivos\\dados.txt", 'a')

mais_texto = arquivo_a.write(novo_texto)

if(mais_texto):
    arquivo_a.close()
    print("Você adcionou mais texto")
