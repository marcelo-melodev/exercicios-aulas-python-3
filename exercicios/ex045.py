from random import randint
from time import sleep
print('Suas opções:')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')
pedra = 'Pedra'
papel = 'Papel'
tesoura = 'Tesoura'
jogada = (input('Qual a sua jogada?'))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sorteio = (randint(0,2))
if sorteio <= 0  or sorteio == 1 or sorteio >= 2:
    print(f'''==========================
    Computador jogou {sorteio}
    Jogador Jogou {jogada}
============================''')
