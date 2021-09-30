# listas en python 
#en las listas cuando se usan [] se pueden agregar diferentes tipos de datos.
lista_ejemplo =[1,'strings',1.34,True,[1,2,3]]
colores = ['red','blue','green']

# Cuando se usa parentesis se usan datos del mismo tipo 
lista_numeros = ((1,2,3,4,5))
print (lista_numeros)
print (type (lista_numeros))

 # lista usando range , que te da el rango definido 
datos = list( range(1, 10))
print( datos )

#impreme valor si el green esta en la lista
print ('green' in colores)
print ('violet' in colores)

#podemos sustituir valores de una lista especificando su lugar 
colores [2] = 'yellow'
print(colores)

#metodos que podemos usar con lista
print(dir(colores))

#para agregar fatos a la lista usamos el metodo append
colores.append('violet')

# metodo extend agrega mas de un dato a una lista 
colores.extend(['marron','amarillo'])
print(colores)

# inserta el dato en la posicion definida por el user
colores.insert(2, ' azul')

# para eliminar algun dato usamos el metodo POP
colores.pop()
print(colores)

# para eliminar todos los datos usamos el metodo clear 
#colores.clear()

# para ordenar los items del arreglo usamos el metodo Sort
print(colores.sort()) #ordena alfabeticamente
print (colores.sort(reverse=True)) # ordena de manera inversa   

# para imprimir un indice que queramos:
print(colores.index('red'))    