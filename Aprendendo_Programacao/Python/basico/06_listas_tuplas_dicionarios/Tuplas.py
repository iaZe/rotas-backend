tupla = ('Daniel', 'Bruna', 'Cauã', 'Dantas') # não precisa dos parênteses
#tuplas são imutáveis

for cont in range(0, len(tupla)):
    print(tupla[cont])

print('-=-'*10)
print(tupla[3])
print('-=-'*10)
print(tupla[2:])
print('-=-'*10)
print(tupla[-3])
print('-=-'*10)
for c in tupla:
    print(c)
print(tupla.count('Daniel')) #Quantas vezes apareçe o nome
print(tupla.index('Bruna')) #Posição