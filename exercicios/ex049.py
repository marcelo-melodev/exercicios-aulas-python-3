num = int(input('\033[033mDigite um numero:'))
print(f'Segue Abaixo a tabuada do número {num}')
print('='*10)
for tabu in range(0, 11,):
    print(f'{num} x {tabu} = {num * tabu}')
print('='*10)
print('FIM')