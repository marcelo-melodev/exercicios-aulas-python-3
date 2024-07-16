import math
n = int(input('Digite um numero inteiro:'))
print('Escolha uma das bases para conversão:')
print('[1] Converter para Bínario')
print('[2] Converter para Octal')
print('[3] Converter para Hexadecimal')
op = input('sua opção')
if op == '1':
    print('{} convertido em Bínario é {}'.format(n,bin(n)))
elif op == '2':
    print('{} convertido em Octal é {}'.format(n,oct(n)))
elif op == '3':
    print('{} convertido em Hexadecimal é {}'.format(n,hex(n)))