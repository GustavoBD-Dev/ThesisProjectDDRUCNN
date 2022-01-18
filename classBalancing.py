'''
El numero de muestras de imagenes del set de datos se encuentra desbalanceado.
Se cuenta con el siguiente numero de datos: 

level   total
0       25810
2        5292
1        2443
3         873
4         708

Por lo que se tomaran 700 imagenes de cada clase, el archivo CSV 
contiene el nombre de la iamgen y el nivel, con esto podemos copiar
a una carpeta nueva (train) en donde se almacenaran las imagenes
a utilizar.
'''

#Importamos archivo CSV como DataFrame
import pandas as pd # para manejar los dataset 
import shutil # para mover los archivos
import csv

# Lectura y vizualizacion del archivo CSV con las etiquetas
data = pd.read_csv('trainLabels.csv')
print(data.head())
print('\n')

# agregamos jpeg a cada valor de image para relacionarlo con las imagenes del dataset
# se guarda en una nueva columna
data['image_name'] = [i + '.jpeg' for i in data['image'].values]
print(data.head())
print('\n')

'''
      image  level     image_name
0   10_left      0   10_left.jpeg
1  10_right      0  10_right.jpeg
2   13_left      0   13_left.jpeg
3  13_right      0  13_right.jpeg
4   15_left      1   15_left.jpeg

'''

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

# Recorremos el DataFrame analizando el atributo 'level' de los datos
for i in data.index:
    # Recorremos los 5 nivels de RD
    for j in [0,1,2,3,4]:
        # Buscamos el nivel de RD del DataSet
        if data['level'][i] == j: # encuentra el nivel de RD 
            # si no tenemos completos los datos de esa clase se agrega 
            if levels['level_{}'.format(j)] < 700:
                # copiamos la imagen a la carpeta final (train)
                shutil.copy('resized_train/resized_train/{}'.format(data['image_name'][i]), "train/{}".format(data['image_name'][i]))
                # incrementamos el valor de los datos de las clases en el diccionario
                levels['level_{}'.format(j)]+=1
                # agregamos el nombre de la imagen y el nivel
                images.append(data['image'][i])
                images_name.append(data['image_name'][i])
                labels.append(j)

print(levels)
print(images)
print(labels)

with open('trainLabelsBalanced.csv', 'w+', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(['image','level', 'image_name'])
    for i in range(len(images)):
        writer.writerow([images[i], labels[i], images_name[i]])

print('Fin del programa')