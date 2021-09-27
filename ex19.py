num = int(input('Digite um numero entre 100 e 999: '))
if 100 <= num <= 999:
    lista = str(num)
    for i, v in enumerate(lista):
        print(v)
else:
    print('O numero nao esta entre 100 e 999')