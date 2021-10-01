from sklearn import datasets
import pandas as pd

#data = datasets.load_iris()
#print(data)
'''
data = pd.DataFrame(datasets.load_iris().data, columns=["largo Sepal","Ancho Sepalo", "largo Petalo", "ancho Petalo"])
print(data)
'''
## vemos la data del csv
data = pd.read_csv("{0}".format("C:\\Users\\Joseluis\\Documents\\Python\\Mineria de datos\\avocado.csv")  , encoding = 'latin9')
#print(data)

#metodo shape  para conocer el tamaño de informaciones
print(data.shape)

# metodo para ver las columnas del archivo 
print(data.columns)
#nos muestra los 5 primeros datos y 5 ultimos datos de la info 
print (data.info)

#el metodo head nos muestra los primeros registros
print(data.head())
#para retornar los elementos que se desea se especifica la cantidad 
print(data.head(25))

# para ver los ultimos datos usamos el metodo TAIL 
print(data.tail())
#de la misma manera podemos observar los elementos que especifiquemos 
print(data.tail(25))