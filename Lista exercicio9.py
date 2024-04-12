numeros = []
for i in range(10):
    numero = int(input("Digite o {}º número inteiro: ".format(i + 1)))
    numeros.append(numero)
    numeros.sort()
    print("Números em ordem crescente:", numeros)
else:
    print("Digite ola para sair:")
