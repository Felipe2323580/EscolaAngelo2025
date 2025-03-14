fim = int(input("digite o ultimo número: "))

X = 1
while X <= fim:
    print(X ,end = " ")
    X += 1
    if fim >= 10001:
        break
    