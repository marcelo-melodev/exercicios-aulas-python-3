numero = int(input('Digite um numero:'))
if numero >= 1:
    for i in range(1,numero):
        if numero % i  == 0:
            print(f'{numero}, é primo')
        else:
            print(f'{numero}, não é primo')
elif numero == 0:
    print(f'{numero}, é zero')
else:
    print(f'{numero}, é negativo')