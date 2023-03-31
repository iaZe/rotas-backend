frase = 'Curso em vídeo Python'

transform = frase.replace('Python', 'Android')
frase.upper()
frase.lower()
frase.capitalize() #Só a primeira letra da frase fica up
frase.title() #Capitalize, as primeiras letras de cada palavra
frase.strip() #Remove os espaços inuteis
frase.rstrip() #Remove os espaços inuteis a direita (ou .lstrip)


print(transform)