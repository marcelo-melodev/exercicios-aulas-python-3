s1 = float(input('\033[43;30;42mPrimeiro segmento:\033[m'))
s2 = float(input('\033[43;30;42mSegundo segmento:\033[m'))
s3= float(input('\033[43;30;42mTeceriro segmento:\033[m'))
if s1 < s2 +s3 and s2 < s1 +s3 and s3 < s1 +s2:
    print('\033[43;30;42mOs segmentos acima podem formar um triangulo!\033[m')
else:
    print('\033[43;30;42mOs segmentos acima não podem formar um triangulo!\033[m')
