import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras


modelo = keras.Sequential([keras.layers.Dense(units=1, input_shape=[2], name='neronio',
                                              kernel_initializer = keras.initializers.RandomNormal(),
                                              bias_initializer = keras.initializers.Ones()
                                              ),])

#modelo.summary()

#keras.utils.plot_model(
    #modelo,
    #to_file='modelo.png',
    #show_shapes=True,
    #show_layer_names=True
#)

#print(modelo.layers)
#pesos, bias = modelo.layers[0].get_weights()
#print("\n", pesos.shape, "\n", pesos)
#print("\n", bias.shape, "\n", bias)
print(modelo.layers[0].get_weights())

def plot(titulo, funcao):
    x = np.arange(-5, 5, 0.05)
    y = [funcao(xi) for xi in x]
    plt.plot(x, y)
    plt.title(titulo)
    plt.show()

def relu(x):
  return max(0.0, x)
plot('ReLU',relu)

def log(x,a=1): # Função Sigmoid
    return np.divide(1,(1+np.exp(-(np.multiply(a,x)))))
plot('Sigmoid',log)

def tanh(x,a=1,b=1): # Tang. Hiperbólica
    return np.tanh(x)
plot('Tangente Hiperbólica',tanh)

def linear(x):
    return x
plot('Linear',linear)