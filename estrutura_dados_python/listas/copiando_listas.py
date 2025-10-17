lista = [1, "Python", [40, 30, 20]] 
lista_dois=lista.copy()
print(lista)

print(id(lista_dois),id(lista))

lista_dois[0]=2

print(lista_dois)
print(lista)

#copia com mesmos valores sem afetar a lista principal