a = input('Escreva algo: ')

print(
    f'''
    O tipo primitivo é, {type(a)}
    É número:       {a.isnumeric()}
    É alfabético:   {a.isalpha()}
    É alfanumérico: {a.isalnum()}
    É maiúscula:    {a.isupper()}
    É minúscula:    {a.islower()}
    Só espaços:     {a.isspace()}
    É capitalizada: {a.istitle()}''')

print('O tipo primitivo desse valor é ', type(a))
print('É um número? ', a.isnumeric())