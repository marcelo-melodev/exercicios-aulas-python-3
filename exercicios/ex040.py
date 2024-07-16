n1 = float(input(' Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
me = n1 + n2
re = me / 2
if re >= 7.0:
    print(f'Tirando {n1} e {n2} a média do aluno é {re}.')
    print('O aluno está APROVADO!')
elif re < 5.0:
    print(f'Tirando {n1} e {n2} a média do aluno é {re}.')
    print('O aluno está Reprovado!')
elif re == 5.0 or 6.9:
    print(f'Tirando {n1} e {n2} a média do aluno é {re}.')
    print('O alunot esta de RECUPERAÇÃO!')