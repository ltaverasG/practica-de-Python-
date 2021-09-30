# funciones 
def hola():
    print('hola mundo')

hola()

# Ojo las funciones pueden recibir parametros 
def saludo(nombre):
    print('hola ' + nombre)

saludo('Luis')

## tambien tenemos funciones lambda
add = lambda numberOne , numberTwo: numberOne + numberTwo

print(add(10,30))