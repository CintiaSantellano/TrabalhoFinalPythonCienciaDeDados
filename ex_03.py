
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

# Quantas compras no crédito foram feitas em 2010?

compras_credito_2010 = 0

for pessoa in pessoas:
    ano = pessoa["ano"]
    pagamento = pessoa["pagamento"]
    
    if ano == 2010 and pagamento == "credito":
        compras_credito_2010 += 1

print(f"O número de compras no crédito feitas em 2010 é: {compras_credito_2010}")

