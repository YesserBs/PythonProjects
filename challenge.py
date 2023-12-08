from random import *
import random

import matplotlib.pyplot as plt
import numpy as np


def lancer_dé():
    return randint(1, 6)

def lancer_monnaie(p):
    return int(random.random() < p)


def lancer(x, p):
    s = 0
    for i in range(x):
        s += lancer_monnaie(p)
    return s

def sim(p):
    #DEBUT
    L = lancer_dé()
    X = lancer(L, p)
    #print("Vous avez obtenu" , L , ", et" , X ,"piles")
    return X


def esperence(p):
    total = 10000
    T = [sim(p) for i in range(total)]
    Esp = sum(T)/total
    return Esp


# Générer les valeurs de l'axe des abscisses dans l'intervalle [0, 1]
x_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# Calculer les valeurs de l'axe des ordonnées en utilisant la fonction 2i+1
y_values = [esperence(i) for i in x_values]
print(y_values)

# Créer la courbe
plt.scatter(x_values, [3.5 * (i) for i in x_values], color='blue', label='Points spécifiques')
plt.plot(x_values, y_values, 'r--')
plt.show()



