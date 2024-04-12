dentro_intervalo = 0
fora_intervalo = 0
for i in range(10):
    numero = int(input("Digite o {}º número: ".format(i + 1)))
    if 10 <= numero <= 20:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1
print("Quantidade de números dentro do intervalo [10, 20]:", dentro_intervalo)
print("Quantidade de números fora do intervalo [10, 20]:", fora_intervalo)