num = 0
contNum = 0
contPar = 0

while num != 1000:
    num = int(input('Digite um número (1000 para parar): '))

    if num % 2 == 0:
        contPar += 1

    contNum += 1

print(f'Foram lidos {contNum} numeros')
print(f'Foram lidos {contPar} numeros pares')

