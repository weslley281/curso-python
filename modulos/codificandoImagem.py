import base64

with open("./dados/logo.png", 'rb') as arquivo:
    arquivo_b64 = base64.b64encode(arquivo.read())
    print(arquivo_b64)