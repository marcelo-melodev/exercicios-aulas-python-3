from random import randint
from time import sleep
print('Suas opções:')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')
itens = ('👊', '🖐', '✌')
jogada = int(input('Qual a sua jogada?'))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sorteio = (randint(0,2))
print(f'''==========================
    Computador jogou {itens[sorteio]}
    Jogador Jogou {itens[jogada]}
============================''')
if sorteio ==0:
    if jogada ==0:
        print('EMPATE')
    elif jogada ==1:
        print('Jogador Vence')
    elif jogada ==2:
        print('Computador vence')
    else:
        print('Jogada Invalida!')
elif sorteio ==1:
    if jogada ==0:
        print('Computador Vence')
    elif jogada ==1:
        print('Empate')
    elif jogada ==2:
        print('Jogador Vence')
    else:
        print('Jogada Inválida')
elif sorteio ==2:
    if jogada == 0:
        print('jogador Vence')
    elif jogada ==1:
        print('Computador Vence')
    elif jogada ==2:
        print('Empate')
    else:
        print('Jogada Inválida')
print('==============Placar============')






