
def sauda(nome):
    print("Olá, " + nome + "!")
    sauda2(nome)
    print("Preparando-se para dizer tchau...")
    tchau()

def sauda2(nome):
    print("Como vai, " + nome + "?")

def tchau():
    print("Ok, tchau!")

def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)
    