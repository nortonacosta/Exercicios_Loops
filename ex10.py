soma = 0
for i in range(1, 50):

    if i % 2 == 0:
        print(i)
    i += 1
    soma += i
print(f'A soma dos numeros é de: {soma}')