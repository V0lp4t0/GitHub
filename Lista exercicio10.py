lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
numero_mais_repetido = None
contagem_mais_alta = 0
for numero in lista:
    contagem = lista.count(numero)
    if contagem > contagem_mais_alta:
        contagem_mais_alta = contagem
        numero_mais_repetido = numero
print("O número que mais se repete é:", numero_mais_repetido)
