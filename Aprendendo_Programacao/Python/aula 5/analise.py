frase = 'Curso em vídeo Python'

        #(frase[0])
fatia = (frase[15:21])
        #(frase[0:21:2])
        #(frase[:5])
        #(frase[15:])
        #(frase[9::3])

len(frase) #contar
frase.count('o') #contar a letra 'o'
frase.count('o', 0, 13) #conta quantos 'o' existem do 0 ao 13
frase.find('em') # procura o 'em'
op = 'Curso' in frase

print(fatia)
print(len(frase))
print(frase.count('o'))
print(op)