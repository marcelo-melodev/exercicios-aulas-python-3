A=float(input('\033[1;31mDigite a altura da parede:'))
L=float(input('Digite a largura da parede:'))
R=A*L
print('A sua parede de {}x{} possui {:.2f}m², logo a quantidade de tinta a ser usada para pinta-la sera de {:.2f} litros de tinta, que equivale há {:.2f} latas de tintas'.format(A,L,R,R*2,R/2))
