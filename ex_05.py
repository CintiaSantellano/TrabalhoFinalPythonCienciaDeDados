
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

# Quem gastou mais no total, jovens, adultos ou idosos?

gasto_jovens = 0
gasto_adultos = 0
gasto_idosos = 0

for pessoa in pessoas:
    idade = pessoa["idade"]
    compra = pessoa["compra"]
    
    if 18 <= idade <= 25:
        gasto_jovens += compra
    elif 26 <= idade <= 59:
        gasto_adultos += compra
    elif idade >= 60:
        gasto_idosos += compra

categoria_maior_gasto = ""
maior_gasto = max(gasto_jovens, gasto_adultos, gasto_idosos)

if maior_gasto == gasto_jovens:
    categoria_maior_gasto = "Jovens (18-25 anos)"
elif maior_gasto == gasto_adultos:
    categoria_maior_gasto = "Adultos (26-59 anos)"
else:
    categoria_maior_gasto = "Idosos (60 anos ou mais)"

print(f"A categoria que gastou mais no total foi: {categoria_maior_gasto}")
print(f"Valor total gasto: R$ {maior_gasto:.2f}")
