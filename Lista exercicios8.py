numero = int(input("Digite um número positivo: "))
if numero <= 0:
    print("O número digitado não é positivo.")
else:
    print("Divisores de", numero, ":")
for i in range(1, numero + 1):
        if numero % i == 0:
         print(i)