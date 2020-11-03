import numpy as np
import threading, queue

def Verificar(slinha):
    cont=0
    for x in slinha:
        cont = cont + x
    return cont


vet = np.array([0,0,0,1])

print(Verificar(vet))