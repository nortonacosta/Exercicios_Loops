somaPar = 0
multImpar = 1

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro numero: '))

if num1 < num2:
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            somaPar += i
        else:
            multImpar *= i
else:
    for i in range(num2, num1 + 1):
        if i % 2 == 0:
            somaPar += i
        else:
            multImpar *= i


print(f'A soma dos pares é: {somaPar}')
print(f'A soma dos ímpares é: {multImpar}')
