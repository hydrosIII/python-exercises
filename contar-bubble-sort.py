### algoritmos para contar cuantas veces un numero cambia de lugar usando el algoritmo bubble sort.
#### también ordena lso números.


def contar_bubbleSort(n):
    a = 0
    for numero in range(len(n)-1,0,-1):
        for i in range(numero):
            if n[i]>n[i+1]:
                temp = n[i]
                n[i] = n[i+1]
                n[i+1] = temp
                a = a + 1
    return a
       
alist1 = [34, 80, 6, 66, 8, 7, 97, 63, 3, 27, 1, 1, 89]
print contar_bubbleSort(alist1)
print(alist1)
