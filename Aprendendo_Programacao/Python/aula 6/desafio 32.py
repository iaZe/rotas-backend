from datetime import date

ano = int(input('Qual ano gostaria de analisar? Digite 0 para o ano anual '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0:
    print('Legal, estamos em {}, um ano bissexto'.format(ano))
else:
    print('Ainda não estamos em um ano bissexto, estamos em {}'.format(ano))
