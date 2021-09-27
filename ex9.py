from random import randint

n = int(input('Digite um número para descobrir os Primeiros numeros impares: '))
for i in range(0, n):
    if i % 3 == 0:
        print(i)

