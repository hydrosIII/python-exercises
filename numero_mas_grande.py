## función para sacar el número mas grande de un arreglo de números

def largest_element(array):
    #if len(array) == 1
    #return array
    m= array[0]
    for i in array:
          if i > m:
            m = i
    return m
        
array = [34, 80, 6, 66, 8, 7, 97, 63, 3, 27, 1, 1, 89]
print largest_element(array)
