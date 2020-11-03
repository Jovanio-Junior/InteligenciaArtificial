import numpy as np
v = np.array([1, 3, 5, 6])
print("Array V")
print(v)
print("#######################")
#meios de criar matriz, pode declarar a mesma como um arrey multidimensional
x = np.array([[1, 2], [3, 4]])
#ai usa a 'asmatrix' que faz com que o arrey seja interpretado como uma matriz 
m = np.asmatrix(x)
# m pode ser usado como arreu agora
x[0,0] = 5
print("Matriz usando array com asmatrix")
print("X ", x)
print("M ", m)
print("#######################")
# vale lembrar que as asmatrix gera como se fosse um ponteiro e não uma copia, então eu modifiquei a posição 
# x[0,0] a posição m[0,0] tambem foi modificada,
#
#
# outro meio de criar matriz
k = np.mat([[1,2],[2,3]])
print(k)
k[0,0] = 5
print(k)