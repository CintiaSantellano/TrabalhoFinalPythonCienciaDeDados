
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
    
# Quantas pessoas jovens:

jovens_18_a_25_anos = 0

for pessoa in pessoas:
    idade = pessoa["idade"]
    
    if 18 <= idade <= 25:
        jovens_18_a_25_anos += 1

print(f"O número de pessoas entre 18 e 25 anos é: {jovens_18_a_25_anos}")
