# es necesario separar los datos en dos sets, entrenamiento y prueba
# por cada clase tenemos 700 imagenes, de las cuales se tomaran 100 para prueba
# y los otros 600 restantes para el entrenamiento

#Importamos archivo CSV como DataFrame
import matplotlib.pyplot as plt
import pandas as pd # para manejar los dataset 
import shutil # para mover los archivos
import csv

# Lectura y vizualizacion del archivo CSV con las etiquetas
data = pd.read_csv('trainLabelsBalanced.csv')
print(data.head())
print('\n')

# se muestran las clases balanceadas
#data['level'].hist()
#data['level'].value_counts()
#plt.show()

# Debemos obtener el mismo numero de imagenes en cada clase para balancear la data
levels = {
    'level_0':0, 
    'level_1':0, 
    'level_2':0, 
    'level_3':0, 
    'level_4':0, }
images = [] # nombre de las imagenes
images_name = [] # guarda el nombre de las imagenes con extención 'jpeg'
labels = [] # guarga la etiqueta correpondiente al nombre en images
train_test = [] #guarda la etiqueta con el nombre del set al que pertence


# Recorremos el DataFrame analizando el atributo 'level' de los datos
for i in data.index:
    # Recorremos los 5 nivels de RD
    for j in [0,1,2,3,4]:
        # Buscamos el nivel de RD del DataSet
        if data['level'][i] == j: # encuentra el nivel de RD 
            # si no tenemos completos los datos de esa clase se agrega 
            if levels['level_{}'.format(j)] < 600:
                # se asigna a set para entrenamiento
                train_test.append('train')
            else:
                # se asigna a set para prueba
                train_test.append('test')

            # incrementamos el valor de los datos de las clases en el diccionario
            levels['level_{}'.format(j)]+=1
            # agregamos el nombre de la imagen y el nivel
            images.append(data['image'][i])
            images_name.append(data['image_name'][i])
            labels.append(j)

with open('trainLabelsBalanced.csv', 'w+', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['image','level', 'image_name', 'train_test'])
    for i in range(len(images)):
        writer.writerow([images[i], labels[i], images_name[i], train_test[i]])

data = pd.read_csv('trainLabelsBalanced.csv')
print(data.head())
print('Fin del programa')