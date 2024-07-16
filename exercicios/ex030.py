from time import sleep
print('=='*10)
numero = int(input('Digite um numero:'))
print('=='*10)
if numero % 2 == 0:
    print('analizando o numero informado, aguarde...')
    sleep(4)
    print('Esse numero é par!')
else:
    print('analizando o numero informado, aguarde..')
    sleep(4)
    print('Esse numero é impar')
