
def buscarMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordernarporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscarMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordernarporSelecao([5, 3, 6, 2, 10])) # [2, 3, 5, 6, 10]