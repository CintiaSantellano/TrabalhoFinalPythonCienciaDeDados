
nome_arquivo = "compras.csv"
arquivo = open (nome_arquivo , "r")
conteudo = arquivo.readlines ()

cabecalho = conteudo [0]
dados = conteudo [1:]

pessoas = []

for linha in dados:
    registro = linha.split (",")
    pessoa = {
        "nome": registro [0],
        "sobrenome": registro [1],
        "idade": int (registro [2]),
        "gênero": registro [3],
        "compra": float (registro [4]),
        "ano": int (registro [5]),
        "pagamento": registro [6].replace ("\n","")
    }
    pessoas.append (pessoa)
    
    quantidade_pessoas = len (pessoas)
    for i in range (quantidade_pessoas):
        pessoa = pessoas [i]
        

# Quantos homens e mulheres existem na base de dados?

quantidade_mulheres = 0

for i in range (quantidade_pessoas):
    pessoa = pessoas [i]
    if pessoa ["gênero"] == "F":
        quantidade_mulheres += 1
        
quantidade_homens = 0

for i in range (quantidade_pessoas):
    pessoa = pessoas [i]
    if pessoa ["gênero"] == "M":
        quantidade_homens += 1
        
print (f"Há {quantidade_mulheres} mulheres na base de dados")
print (f"Há {quantidade_homens} homens na base de dados")
