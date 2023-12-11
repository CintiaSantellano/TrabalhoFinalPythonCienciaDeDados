
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

# Qual foi o valor total de compras realizadas por mulheres em 2014?

compras_mulheres_2014 = 0

for pessoa in pessoas:
    ano = pessoa["ano"]
    genero = pessoa["gênero"]
    compra = pessoa["compra"]
    
    if ano == 2014 and genero == "F":
        compras_mulheres_2014 += compra

print(f"O valor total de compras realizadas por mulheres em 2014 foi: R$ {compras_mulheres_2014:.2f}")

