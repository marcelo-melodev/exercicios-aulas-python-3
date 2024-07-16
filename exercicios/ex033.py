primeiro = int(input('Digite o segundo valor:'))
segundo = int(input('Digite o segundo valor:'))
terceiro = int(input('Digite o terceiro valor'))
maenor = primeiro
#Verificando menor valor
if segundo < primeiro and segundo > terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro
#Verificando maior valor
maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))