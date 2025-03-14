lista = [1, 2, 3, 4, 5, 6, 7, 3, 8, 9, 0]
len(lista)
print(len(lista))
print(lista) 
print(lista[2:len(lista)-1])

print(max(lista))

print(min(lista))

print(sum(lista))

tamanho = len(lista)
print(tamanho)

lista.insert(7, 69)
print(lista)
while 3 in lista:
    lista.remove(3)
    print(lista)