frase = str(input('Digite uma frase: ')).strip()
minusculo = frase.lower()
n = minusculo.count('a')
print('A quantidade de A(s) que tem na frase são: {}'. format(n))
p1 = minusculo.find('a')
print('A posição em que a primeira letra A está é: {}'.format(p1))
p2 = minusculo.rfind('a')
print('A posição em que a ultima letra A está é: {}'.format(p2))