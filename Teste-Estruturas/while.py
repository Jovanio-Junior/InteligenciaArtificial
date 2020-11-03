import numpy as np
import threading, queue


q = queue.Queue()
q.put(1)
q.put(5)
q.put(9)
q.put(12)
q.put(155)
while not q.empty():
    x = q.get()
    print(x)
