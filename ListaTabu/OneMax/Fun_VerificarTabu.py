import numpy as np
import threading, queue

def VerificarTabu(tabu,m):
    
    for x in range(tabu.qsize()):
        if tabu.queue[x] == m:
            return True
    
    return False


q = queue.Queue()

q.put(4)
q.put(5)
if VerificarTabu(q,4):
    print("aaaaaaaaa")
else:
    print("bbbbbbbbbbbbbbbb")