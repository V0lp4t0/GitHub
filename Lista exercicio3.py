while True:
    valor = int(input("Digite um numero inteiro de 1 A 10: "))
    print("Digite -1 para sair...")
    if valor == -1:
        print("Saiando do programa")
        break
    if  valor >= 1 and valor <= 10:   # 1 <= valor <= 10
        print(f"Tabuada do numero:{valor}") 
        for i in range(1,11):
            print(valor,"X", i, "=", valor*i)
    else:
        print("Valor invalido...")
        continue

    