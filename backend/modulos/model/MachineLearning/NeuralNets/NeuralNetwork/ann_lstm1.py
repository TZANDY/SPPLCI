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


def formatearnombre():
    codigo1 = str(datetime.now())
    cadena_codigo = str(codigo1.replace(':','').replace('-','').replace(' ','')[0:14])
    filename2 = os.path.join(current_dir,"public/images/"+cadena_codigo+"_"+"test.jpg")
    plt.savefig(filename2)
    return True

current_dir = os.path.dirname(os.path.realpath(__file__))
filename1 = os.path.join(current_dir,"public/uploads/test.csv")
#filename2 = os.path.join(current_dir,"public/images/"+formatearnombre()+"_"+"test.jpg")

#Metodo de visualizacion de la prediccion
def visualizar(real,prediccion):
    plt.plot(real[0:len(prediccion)],color='red',label='cantidad maxima real de venta')
    plt.plot(prediccion,color='blue',label='Prediccion de la venta')
    plt.xlabel('Tiempo')
    plt.ylabel('Cantidad')
    plt.legend()
    plt.grid(True)
    formatearnombre()
    guardarmodelo()
    #plt.savefig(filename2)
    plt.show()
    
    #\modulos\model\MachineLearning\NeuralNets\NeuralNetwork\public\docs\modeloBin


dataset = pd.read_csv(filename1,index_col='Date',parse_dates=['Date'])
#C:\Users\Infan\OneDrive\Documentos\GitHub\TP\SPPLCI\backend\modulos\static\uploads\test.xlsx
# definir el set ede entrenamiento , el set de test
trainingSet = dataset['2020':].iloc[:,[False, False, True, False]]
testSet = dataset[:'2021'].iloc[:,[False, False, True, False]]

# Normalizacion del set de entrenamiento (valores entre 0 y 1)
sc = MinMaxScaler(feature_range=(0,1))
trainingSetScaled = sc.fit_transform(trainingSet)

# vamos a entrenar a la red proporcionando 100 datos de entrada y 1 de salida en cada iteraccion
timeSteps = 100
xTrain = []
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
dim_salida = 1
na = 50

# units = neuronas de la capa | return_sequences = hay mas capas? | input_shape = dimension entrada |
# Dropout(%) = numero de neuronas que queremos ignorar en la capa de regularizacion (normalmente es de un 20%)
regresor = Sequential()

# capa 1
regresor.add(LSTM(units=na, input_shape=dim_entrada))

# capa 2
#regresor.add(LSTM(units=na,return_sequences=True,input_shape=dim_entrada))

# capa output
regresor.add(Dense(units=dim_salida))
regresor.compile(optimizer='rmsprop', loss='mse') # mse = mean_squared_error

#encajar red neuronal en Set Entrenamiento
# epochs = iteraciones para entrenar tu modelo
# batch_size = numero ejemplos entrenamiento (cuanto mas alto, mas memoria necesitaras)
regresor.fit(xTrain,yTrain,epochs=20,batch_size=32)

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

def dato():
    arr = np.array(prediccion)
    json_str = json.dumps({'data':arr.tolist()})
    return json_str

def main():
    visualizar(testSet.values,prediccion)
    


