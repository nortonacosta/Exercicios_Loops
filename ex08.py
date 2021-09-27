from random import randint

menor = 0
maior = 0
for i in range(1, 11):
    n = randint(0, 100)
    if i == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    print(n)

print('-------')
print(f'O maior é {maior}')
print(f'O menor é {menor}')

