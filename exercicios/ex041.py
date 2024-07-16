from datetime import date
ano = int(input('Ano de nascimento:'))
data = date.today().year
idade = data - ano
if idade <= 9:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: Mirim')
elif idade <= 14:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: Infantil')
elif idade <= 19:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: Junior')
elif idade == 20:
    print(f'O atleta tem {idade} anos.')
    print('Classificação: Sênior')
else:
    print(f'Atleta possui {idade} anos.')
    print('Classificação: Master')