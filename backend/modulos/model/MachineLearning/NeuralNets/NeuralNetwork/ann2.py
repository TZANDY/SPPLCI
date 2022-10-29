from pyexpat import model
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

entrada =np.array([1,6,30,70,43,503,201,1005,99],dtype=float)

resultados = np.array([0.0254 , 0.1524, 0.762, 0.1778 , 1.0922, 12.776, 5.1054, 25.527, 2.514,],dtype=float)


# topografia de la red
capa1 = tf.keras.layers.Dense(units=1,input_shape=[1])

modelo = tf.keras.Sequential([capa1])


# OPTIMIZADOR (Encargado de ajustar los pesos y sesgos)
modelo.compile(
    optimizer= tf.keras.optimizers.Adam(0.1),
    loss = 'mean_squared_error'
)
# 

print("* * * * * ENTRENANDO LA RED * * * * * *")

#entrenamos el modelo
entrenamiento = modelo.fit(entrada, resultados,epochs=500,verbose=False)

#guardar la red neuronal
modelo.save('ANN.h5')
modelo.save_weights('pesos.h5')

plt.xlabel("CICLOS DE ENTRENAMIENTO")
plt.ylabel("Errores")
plt.plot(entrenamiento.history["loss"])
plt.show()

#verificar que la red entreno
print("TERMINAMOS")


# PREDICCION
i = input("Ingresar el valor en pulgadas: ")
i = float(i)

prediccion = modelo.predict([i])
print("el valor en metros es: ",str(prediccion))