
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
    
print(quicksort([10, 5, 2, 3]))
print(quicksort([10, 5, 2, 3, 1, 7, 8, 9, 4, 6]))