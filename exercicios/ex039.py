from datetime import date
import math
nasci = int(input('Informe seu ano de nascimento:'))
data_atual = date.today().year
idade = data_atual - nasci
dezoito = 18
if idade < dezoito:
    print('Você nasceu em {}, tem {} em {}'.format(nasci, idade, data_atual))
    print('Ainda Falta {} anos para o alistamento'.format(dezoito - idade))
    print('Seu alistamento será em {}'.format(data_atual + dezoito - idade))
elif idade > dezoito:
    print('Você Nasceu em {}, tem {} anos em {}'.format(nasci, idade, data_atual))
    print('Você deveria ter se alistado há {} anos'.format(idade - dezoito))
    print('Seu alistamento foi {}'.format(data_atual + dezoito - idade))
elif idade == dezoito:
    print('Quem nasceu em {} tem {} anos em {}'.format(nasci, idade , data_atual))
    print('Você tem que se alistar IMEDIATAMENTE!')
    