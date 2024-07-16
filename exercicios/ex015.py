dias = int(input('\033[7;30;41mDigite a quantidade de dias:'))
km = float(input('Digite a quantidade de KM:'))
Vk = km*0.15
Vd = dias * 60
VT = Vk + Vd
print('O valor a ser cobrado do aluguel do carro é de R${:.2f}'.format(VT))
