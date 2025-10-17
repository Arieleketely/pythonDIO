numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []
for numero in numeros: 
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

        
        #ou
        
numeros_2 = [1, 30, 21, 2, 9, 65, 34]
par = [num for num in numeros_2 if num% 2 == 0]
print(par)


nr = [1, 30, 21, 2, 9, 65, 34]
quadrados = []
for numero_2 in nr: 
    quadrados.append(numero_2 ** 2)
    print("-")
    print( quadrados)


ns = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numb ** 2 for numb in ns]
print("###")
print(quadrado)