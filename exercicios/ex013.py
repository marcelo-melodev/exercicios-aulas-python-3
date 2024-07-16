nome=input('\033[36mDigite o nome do colaborador:')
S=float(input('Digite o salário do colaborador {}'.format(nome)))
print('O novo salário do colaborador R${:.2} com o reajuste de 15% é R${:.2f}'.format(nome,S*15/100+S))
