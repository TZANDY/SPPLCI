import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons, make_circles

#Funcion de activacion

def sigmoid(x, deriv = False):
    if deriv:
        return x * (1-x)
    return 1/(1+np.e**-x)


def tanh(x, deriv = False):
    if deriv:
        return (1 - (np.tanh(x))**2)
    return np.tanh(x)


#RMSE (error cuadratico medio)
#Yp = valor predicho
#Yr = valor real
def RMSE(Yp,Yr,deriv = False):
    if deriv:
        return (Yp-Yr)
    return np.mean((Yp-Yr)**2)

#Primera Capa
class Layer:
   def __init__(self, con,neuron):
    self.b = np.random.rand(1,neuron)*2-1
    self.W = np.random.rand(con, neuron) *2 -1
    

class ArtificialNeuralNetwok:
    def __init__(self,top = [],act_fun = sigmoid):
       self.top = top
       self.act_fun = act_fun
       self.model = self.define_model()
    
    def define_model(self):

        ArtificialNeuralNetwok = []

        for i in range(len (self.top[:-1])):
            ArtificialNeuralNetwok.append(Layer(self.top[i], self.top[i+1]))
        return ArtificialNeuralNetwok

    def predict(self, X =[]):

        out = X

        for i in range(len(self.model)):
            z = self.act_fun( out @ self.model[i].W + self.model[i].b )
            out = z
        return out

    # aqui entrena la red neuronal
    # Learning_Rate : gradiente es la derivada del vector con respecto X, Y, Z (hacia donde crece mas rapido una funcion)
    # Que tanto caso se le haremos a la tendencia(gradiente)
    # nota* si el learning_rate es muy alto a la ANN le cueta mucho encontrar el resultado / si es muy bajo aprendera lento(se queda en el minimo local)
    def fit(self,X = [], Y = [], epochs = 1000, learning_rate = 0.5):
        for k in range(epochs):

            out = [(None,X)]

            for i in range(len(self.model)):
                z= out[-1][1] @ self.model[i].W + self.model[i].b

                # a es una matriz de valores
                a=sigmoid(z,deriv=False)
                out.append((z,a))

            deltas = []

            # castigar los errores, por eso vamos hacia atras
            for i in reversed(range(len(self.model))):
                z= out[i+1][0]
                a = out[i+1][1]

                # que tanto se equivoco en cada layer
                if i == len(self.model) -1:
                    deltas.insert(0,RMSE(a,Y, deriv=True)* sigmoid(a, deriv=True))

                else:
                    deltas.insert(0,deltas[0] @ _W.T * sigmoid(a, deriv=True))
                
                # guardando los pesos en la matriz de pesos ( _W )
                _W = self.model[i].W

                # guiando al peso
                # Calculamos el vector promedio de los Deltas (Vector columna)
                # Se va a mover hacia donde decrece el gradiente
                self.model[i].b = self.model[i].b - np.mean(deltas[0], axis=0, keepdims= True )* learning_rate


                #corregimos la matriz de pesos
                # derivacion en cadena
                self.model[i].W = self.model[i].W - out[i][1].T @ deltas[0] * learning_rate

        print('¡Red Neuronal artificial entrenada con exito!')

# Perceptron
def random_points(n=100):
    x = np.random.uniform(0.0 , 1.0 , n)
    y = np.random.uniform(0.0 , 1.0 , n)

    return np.array([x,y]).T


def main():
    brain_xor = ArtificialNeuralNetwok(top = [2,4,1], act_fun = tanh)

    # Compuerta XOR
    # 0 v 0 = 0
    # 0 v 1 = 1
    # 1 v 0 = 1
    # 1 v 1 = 0
    X = np.array([
        [0,0],
        [0,1],
        [1,0],
        [1,1],
    ])

    Y = np.array([
        [0],
        [1],
        [1],
        [0],
    ])

    # EJECUCION

    # Conjunto entrenado
    brain_xor.fit(X = X, Y = Y, epochs = 10000, learning_rate=0.05)

    x_test = random_points(n = 5000)
    y_test = brain_xor.predict(x_test)

    plt.scatter(x_test[:,0],x_test[:,1], c = y_test , s = 25 , cmap='GnBu')
    plt.savefig('XOR_Fitted.jpg')
    #plt.show()

    #CIRCULAR    
    brain_circles = ArtificialNeuralNetwok(top = [2, 4, 8, 1], act_fun = sigmoid)

    X, Y = make_circles(n_samples = 500, noise = 0.05, factor = 0.5)
    Y = Y.reshape(len(X), 1)


    # y_test = brain_circles.predict(X)
    # plt.scatter(X[:,0], X[:,1], c = y_test, cmap = 'winter', s = 25)
    # plt.show()

    brain_circles.fit(X = X, Y = Y, epochs = 10000, learning_rate = 0.05)

    y_test = brain_circles.predict(X)
    plt.scatter(X[:,0], X[:,1], c = y_test, cmap = 'winter', s = 25)
    plt.savefig('Circle_fitted.jpg')
    plt.show()

    # Media luna
    brain_moon = ArtificialNeuralNetwok(top = [2, 4, 8, 1], act_fun = sigmoid)

    X, Y = make_moons(n_samples = 500, noise = 0.05)
    Y = Y.reshape(len(X), 1)

    y_test = brain_moon.predict(X)
    # plt.scatter(X[:,0], X[:,1], c = y_test, cmap = 'winter')

    brain_moon.fit(X = X, Y = Y, epochs = 10000, learning_rate = 0.05)

    y_test = brain_moon.predict(X)
    plt.scatter(X[:,0], X[:,1], c = y_test, cmap = 'winter')
    plt.savefig('Moon_fitted.jpg')
    plt.show()


if __name__ == '__main__':
    main()
        
#Prueba
#brain = ArtificialNeuralNetwok(top =[2,4,2],act_fun = sigmoid)
#print(brain.predict(X=[0,0]))
#print(brain.predict(X=[0,1]))
#print(brain.predict(X=[1,0]))
#print(brain.predict(X=[1,1]))

