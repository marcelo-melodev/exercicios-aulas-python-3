from random import randint
from time import sleep
print('Suas opções:')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')
pedra = 0
papel = 1
tesoura = 2
jogada = (input('Qual a sua jogada?'))
p0 = pedra
p1 = papel
t2 = tesoura
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sorteio = int(randint(0,2))
if sorteio == 0:
    print(f'''====================
          Computador jogou Pedra
          ==============================''')
elif sorteio == 1:
    print('''===================
          Computador jogou Papel
          ===============================''')
elif sorteio >= 2:
    print('''======================
          Computador jogou Tesoura
          ===============================''')




