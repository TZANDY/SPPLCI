import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense,LSTM,Dropout
import os
from datetime import datetime
from sklearn.metrics import mean_squared_error
import json


codigo1=""

def guardarimagen():
    #codigo1 = str(datetime.now())
    #cadena_codigo = str(codigo1.replace(':','').replace('-','').replace(' ','')[0:14])
    filename2 = os.path.join(current_dir,"public/images/test.jpg")
    plt.savefig(filename2)
    return True

current_dir = os.path.dirname(os.path.realpath(__file__))
filename1 = os.path.join(current_dir,"public/uploads/test.csv")
#filename2 = os.path.join(current_dir,"public/images/"+formatearnombre()+"_"+"test.jpg")

#Metodo de visualizacion de la prediccion
def visualizar(real,prediccion):
    plt.plot(real[0:len(prediccion)],color='red',label='Cantidad máxima real')
    plt.plot(prediccion,color='blue',label='Prediccion')
    plt.suptitle('Cantidad de platos vendidos por día')
    plt.xlabel('Días')
    plt.ylabel('Cantidad(unidades)')
    plt.legend()
    plt.grid(True)
    guardarimagen()
    guardarmodelo()
    #plt.savefig(filename2)
    plt.show()
    #print(prediccion[[0][0]],prediccion[[1][0]],prediccion[[2][0]],prediccion[[3][0]])
    #print(len(prediccion))
    #dato()
    #\modulos\model\MachineLearning\NeuralNets\NeuralNetwork\public\docs\modeloBin


dataset = pd.read_csv(filename1,index_col='Date',parse_dates=['Date'])
#C:\Users\Infan\OneDrive\Documentos\GitHub\TP\SPPLCI\backend\modulos\static\uploads\test.xlsx
# definir el set ede entrenamiento , el set de test
trainingSet = dataset['2021':].iloc[:,[False, False, True, False]]
testSet = dataset[:'2022'].iloc[:,[False, False, True, False]]

# Normalizacion del set de entrenamiento (valores entre 0 y 1)
sc = MinMaxScaler(feature_range=(0,1))
# Guardando estos datos en la variable traininSetScaled
trainingSetScaled = sc.fit_transform(trainingSet)

# vamos a entrenar a la red proporcionando 100 datos de entrada y 1 de salida en cada iteraccion
# timesteps = bloques de datos 
timeSteps =7
# lista de listas
xTrain = []
# salida de datos de xtrain
yTrain = []

# xTrain = lista de conjuntos de 100 datos.
# yTrain = lista de valores

for i in range(0,len(trainingSetScaled)-timeSteps):
    xTrain.append(trainingSetScaled[i:i+timeSteps,0])
    yTrain.append(trainingSetScaled[i+timeSteps,0])

# preferible usar numpy ya que:

#1. Deberemos transformar xTrain (actualmente de dos dimensiones) a tres dimensiones.
#2. Los programas que usan numpy generalmente son mas rapidos(sobretodo en IA)

xTrain, yTrain = np.array(xTrain),np.array(yTrain)

# hay que añadir una dimension a xtrain, nos lo pide la libreria keras
xTrain = np.reshape(xTrain, (xTrain.shape[0],xTrain.shape[1],1))

# parametros que debemos proporcionar a keras(sequential())
dim_entrada = (xTrain.shape[1],1)
dim_salida = 20
#numero de neuronas
na = 50

# units = neuronas de la capa | return_sequences = hay mas capas? | input_shape = dimension entrada |
# Dropout(%) = numero de neuronas que queremos ignorar en la capa de regularizacion (normalmente es de un 20%)
regresor = Sequential()

# capa 1
regresor.add(LSTM(units=na,return_sequences=True, input_shape=dim_entrada,time_major = True ))


# si se quiere agregar mas capas, se sigue lo siguiente
# capa 1
#regresor.add(LSTM(units=na,return_sequences=True,input_shape=dim_entrada))
# capa 2
regresor.add(LSTM(units=na))

# capa output
regresor.add(Dense(units=dim_salida))

regresor.compile(optimizer='rmsprop', loss='mse',metrics=['accuracy']) # mse = mean_squared_error

#encajar red neuronal en Set Entrenamiento
# epochs = iteraciones para entrenar tu modelo
# batch_size = numero ejemplos entrenamiento (cuanto mas alto, mas memoria necesitaras)
regresor.fit(xTrain,yTrain,epochs=800,batch_size=50,verbose="auto",validation_freq=1,max_queue_size=10,workers=1)
regresor.evaluate(xTrain,yTrain,batch_size=None,
    verbose="auto",
    sample_weight=None,
    steps=None,
    callbacks=None,
    max_queue_size=10,
    workers=1,
    use_multiprocessing=False,
    return_dict=False)

# Normalizar el conjunto de Test y realizamos las mismas operaciones que anteriormente hicimos
auxTest = sc.transform(testSet.values)
xTest = []

for i in range(0,len(auxTest)-timeSteps):
    xTest.append(auxTest[i:i+timeSteps,0])

xTest = np.array(xTest)
xTest = np.reshape(xTest, (xTest.shape[0],xTest.shape[1],1))


#realizamos la prediccion
prediccion = regresor.predict(xTest)

# desescalamos la prediccion para que se encuentre entre valores normales
prediccion = sc.inverse_transform(prediccion)

def guardarmodelo():
    codigo1 = str(datetime.now())
    cadena_codigo = str(codigo1.replace(':','').replace('-','').replace(' ','')[0:14])
    filename2 = os.path.join(current_dir,"public/docs/modeloBin/"+cadena_codigo+"_"+"modelo.h5")
    regresor.save(filename2)

def main():
    visualizar(testSet.values,prediccion)
    obtenerResultados()
   
def diaSemana(numero):
    if (numero==0)|(numero==7)|(numero==14)|(numero==21)|(numero==28)|(numero==35):
        return "Lunes"
    elif (numero==1)|(numero==8)|(numero==15)|(numero==22)|(numero==29)|(numero==36):
        return "Martes"
    elif (numero==2)|(numero==9)|(numero==16)|(numero==23)|(numero==30)|(numero==37):
        return "Miércoles"
    elif (numero==3)|(numero==10)|(numero==17)|(numero==24)|(numero==31)|(numero==38):
        return "Jueves"
    elif (numero==4)|(numero==11)|(numero==18)|(numero==25)|(numero==32)|(numero==39):
        return "Viernes"
    elif (numero==5)|(numero==12)|(numero==19)|(numero==26)|(numero==33)|(numero==40):
        return "Sábado"
    elif (numero==6)|(numero==13)|(numero==20)|(numero==27)|(numero==34)|(numero==41):
        return "Domingo"
        
#def diaSemana(numero):
#    match numero:
#        case 0:
#            return "Lunes"
#        case 1:
#            return "Martes"
#        case 2:
#            return "Miércoles"
#        case 3:
#            return "Jueves"
#        case 4:
#            return "Viernes"
#        case 5:
#            return "Sábado"
#        case 6:
#            return "Domingo"

def obtenerResultados():
    valores=[]
    filename3 = os.path.join(current_dir,"public/docs/modeloBin/resultados.txt")
    f = open (filename3,'w')
    n = 0
# Accedemos a cada fila (que es una lista)
    for fila in prediccion:
        
    # Accedemos a cada columna dentro de la fila
        for columna in fila:
            respuestadic ={"valor":columna,"Dia":n,"DiaSemana":diaSemana(n)}
            valores.append(respuestadic)
            n +=1
    f.write(str(valores))
    return valores
    #print(prediccion[0])
    
    #print("Coordenada (0,0) ",prediccion[[0][0]])
    #print("Coordenada (1,0) ",prediccion[[1][0]])
    #print("Coordenada (2,0) ",prediccion[[2][0]])
    #print("Coordenada (3,0) ",prediccion[[3][0]])
    #print("Coordenada (4,0) ",prediccion[[4][0]])
    #print("Coordenada (5,0) ",prediccion[[5][0]])
    #print("Coordenada (6,0) ",prediccion[[6][0]])
    #print("Coordenada (7,0) ",prediccion[[7][0]])
    #print("Coordenada (8,0) ",prediccion[[8][0]])
    #print("Coordenada (9,0) ",prediccion[[9][0]])
    #print("Coordenada (10,0) ",prediccion[[100][0]])
    #print("Coordenada (10,0) ",prediccion[[100][0]])
    #print("Coordenada (10,0) ",prediccion[[-1][0]])


