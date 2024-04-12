idades = 0
contador = 0 
while True:
    idade = input("Coloque uma idade ( ou 'fim' para terminar):")
    if idade.lower() == 'fim':
        break
idade = int(idade)
idades += idades
contador+=1
if contador > 0:
    media = idades / contador 
    print("A media das idades fornecidas é :", media)
else:
    print("Nenhuma idade foi fornecida.")

