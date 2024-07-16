#numero = input('Digite um numero:')
#print('Analisando o numero {} tem:'.format(numero))
#print('unidade {}'.format(numero[3:4]))
#print('dezena {}'.format(numero[2:3]))
#print('centena {}'.format(numero[1:2]))
#print('milhar {}'.format(numero[:1]))
num = int(input('informe um numero'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print( 'analizando o numero {}'. format(num))
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('milhar {}'.format(m))


