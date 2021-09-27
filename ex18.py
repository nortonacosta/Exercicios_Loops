n = int(input('Digite quantos numeros a ser digitados: '))
maior = 0
contM = 0
for i in range(0, n):
    num = int(input(f'Digite o {i}º numero: '))
    if i == 1:
        maior = num
    elif num > maior:
        maior = num
        contM += 1
print(f'O maior número é {maior} e foi digitado {contM} vezes')

