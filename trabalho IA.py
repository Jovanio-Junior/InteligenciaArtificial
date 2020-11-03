#ERIK LOPES DA SILVA

import numpy as np

def calc_SQT(vet):
      soma = 0
      i = 0
      while i < len(vet):
            soma = soma + (vet[i] - (sum(vet) / len(vet)))**2
            i = i + 1
      return soma

      
def calc_SQR(vet, vet_hat):
      soma = 0
      i = 0
      while(i < len(vet)):
            soma = soma + (vet_hat[i] - (sum(vet) / len(vet)))**2
            i = i + 1
      return soma

def calc_SQE(vet, vet_hat):
      soma = 0
      i = 0
      while(i < 13):
            soma = soma + (vet[i] - vet_hat[i])**2
            i = i + 1
      return soma

#criando os arrays X
x = np.array([[1.0000,  1.7400,  5.3000, 10.8000],
              [1.0000,  6.3200,  5.4200,  9.4000],
              [1.0000,  6.2200,  8.4100,  7.2000],
              [1.0000, 10.5200,  4.6300,  8.5000],
              [1.0000,  1.1900, 11.6000,  9.4000],
              [1.0000,  1.2200,  5.8500,  9.9000],
              [1.0000,  4.1000,  6.6200,  8.0000],
              [1.0000,  6.3200,  8.7200,  9.1000],
              [1.0000,  4.0800,  4.4200,  8.7000],
              [1.0000,  4.1500,  7.6000,  9.2000],
              [1.0000, 10.1500,  4.8300,  9.4000],
              [1.0000,  1.7200,  3.1200,  7.6000],
              [1.0000,  1.7000,  5.3000,  8.2000]])

#transposta de X
xt = x.transpose()

#criando o array de Y
y = [  25.500, 31.200, 25.900, 38.400, 18.400, 26.700, 26.400, 25.900, 32.000, 25.200, 39.700, 35.700, 26.500]

#criando indíce B
aux = np.dot(xt, x)
aux1 = np.linalg.inv(aux)
aux2 = np.dot(xt,y)
b = np.dot(aux1, aux2)

#calculando y hat
y_hat = np.dot(x,b)

#calculando SQT
SQT = calc_SQT(y)

#Calculando SQR
SQR = calc_SQR(y, y_hat)

#Calculando SQE
SQE = calc_SQE(y, y_hat)

#Calculando R²
R_quadrado = 1 - (SQE / SQT)

#Calculando R² ajustado
R_ajustado = 1 - (((13-1)/((13+1)-1))*(1-R_quadrado))

print("SQT =", SQT)
print("SQR =", SQR)
print("SQE =", SQE)
print("R² =", R_quadrado)
print("R² aj =", R_ajustado)

