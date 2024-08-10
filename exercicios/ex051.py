print('='*30)
print('10 Temos de uma P.A')
print('='*30)
termo = int(input('Digite um termo: '))
razão = int(input('Digite a razão: '))
decimo = termo +(10 - 1) * razão
for c in range(termo,decimo + razão,razão):
    print(f'{c}', end = ' ➡ ')
print('FIM')
