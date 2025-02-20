valor = int(input("Digite um inteiro entre 10 e 100"))
if valor <= 10 or valor >= 100:
    print("Valor inválido")
else: 
    if valor % 2 == 0:
        if valor == 50:
            print("Valor é 50")
        else:
            print("Você não digitou 50")
    else:
        print("Valor ímpar")