s = 0
for c in range(0,6):
    num = int(input('Digite um numero:'))
    s+=num
if num %2 == 0:
    print(s)
else:
    print('Não foram digitados numeros pares')
