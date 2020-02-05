import numpy as np

def sigmoid(x):
    return 1 / (1+np.exp(-x))
def relu(x):
    return np.maximum(x,0)
def sigmoid_(x):
    return sigmoid(x)*(1-sigmoid(x))
def relu_(x):
    return (x > 0) * 1.0 + (x == 0) * 0.5 + (x < 0) * 0

class fonction_activation():
    def __init__(self, type_fonction = 'sigmoid'):
        self.type_fonction = type_fonction
    def evaluate(self,x):
        return {
            'sigmoid': sigmoid ,
            'relu': relu
        }[self.type_fonction](x)
    def derivative(self,x):
        return {
            'sigmoid': sigmoid_ ,
            'relu': relu_
        }[self.type_fonction](x)

