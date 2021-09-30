MyStr = "hello world"

#Con el comando dir podemos ver las funciones de una variable
print( dir(MyStr))

#upper (convierte texto a mayuscula)
print (MyStr.upper())

#lower (convierte el texto a minuscula)
print (MyStr.lower())
#Entre otros metodos.

#este metodo remplaza los valores anteriores
print( MyStr.replace('hello','bye World').upper())

#metodo count ( cuenta los caracteres definidos)
print(MyStr.count('l'))
#len ( permite saber la longitud )
print(len(MyStr))

#buscamos el indice de la palabra e 
print(MyStr.index('e'))

#preguntamos si es numerico 
print(MyStr.isnumeric())