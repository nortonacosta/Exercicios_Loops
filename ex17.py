n = int(input("Digite um número inteiro e positivo: "))

print(f"A soma dos {n} primeiros números naturais:")
soma = 0
for i in range(1, n*n):
    if i <= n:
        soma += i
print(soma)
