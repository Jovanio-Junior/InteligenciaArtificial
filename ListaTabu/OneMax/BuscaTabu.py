import numpy as np
import threading, queue

def Verificar(slinha):
    cont=0
    for x in slinha:
        cont = cont + x
    return cont

def VerificarTabu(tabu,m):
    
    for x in range(tabu.qsize()):
        if tabu.queue[x] == m:
            return True
    
    return False


def ListaTabu(s,BTmax,T):
    slinha = s.copy()
    iter = 0
    melhor_iter = 0
    tabu = queue.Queue()
    while (iter-melhor_iter) <= BTmax:
        iter = iter + 1
        slinha = s.copy()
        scorrrent = np.zeros(len(s), dtype=int)
        moviment = -1
        for i in range(len(slinha)):
            slinha[i] = not slinha[i]
            if Verificar(slinha) > Verificar(scorrrent):
                if tabu.empty() or not VerificarTabu(tabu,i):
                    scorrrent = slinha.copy()
                    moviment = i
            slinha[i] = not slinha[i]
        if moviment >= 0:
            if tabu.qsize() == T:
                tabu.get()
            tabu.put(moviment)
            if Verificar(scorrrent) > Verificar(s):
                melhor_iter = iter
            s = scorrrent
        
            print(scorrrent)
        print(iter)
    print(melhor_iter)




s = np.zeros(100, dtype=int)
ListaTabu(s,2,2)
#vet = np.array([0,0,0,1])
