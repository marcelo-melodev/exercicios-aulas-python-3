sl = float(input('\033[4;34;40mInsira o salário de um funcionário:\033[m'))
sm = sl * (15/100)
rsm = sm + sl
if rsm <= 1250:
    print('\033[4;34;40mO salario informado é de {}\033[m'.format(rsm))
else:
    sl >= 1250
    sm = sl * (10/100)
    rsm = sm + sl
    print('\033[4;34;40mO salario informado é {}\033[m'.format(rsm))