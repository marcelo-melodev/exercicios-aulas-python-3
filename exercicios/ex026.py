frase = str(input('Digite uma Frase:')).strip()
a= frase.lower()
primeira = a.find('a')+1
ultima = a.rfind('a')+1
print('A letra A aparece {} vezes'.format(a.count('a')))
print('A primeira letra A aparece na posição {}'.format(primeira))
print('A ultima letra A aparece na posição {}'.format(ultima))


