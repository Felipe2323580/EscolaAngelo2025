# Faça uma função que retorne um jogo da mega sena com valores aleatórios não repitidos.
# O usuário deverá dizer quantos números quer jogar, de 6 até 10
# Imprima o resultado solicitado.

import random

def gerar_jogo_mega_sena(qtd_numeros):
    if qtd_numeros < 6 or qtd_numeros > 10:
        return "A quantidade de números deve ser entre 6 e 10."
    
    # Gera uma lista de números de 1 a 60
    numeros = random.sample(range(1, 61), qtd_numeros)
    
    # Ordena os números para melhor visualização
    numeros.sort()
    
    return numeros

# Solicita ao usuário a quantidade de números
qtd = int(input("Quantos números você quer jogar (de 6 a 10)? "))
resultado = gerar_jogo_mega_sena(qtd)

print("Seu jogo da Mega Sena é:", resultado)