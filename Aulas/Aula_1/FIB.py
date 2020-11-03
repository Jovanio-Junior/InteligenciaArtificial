def fib(n):  # declarando a funcao de Fibonacci
    # vai imprimir a serie de fibonacci ao N
    cont,a, b = 0,0, 1
    while (cont < n):
        print(a)
        a, b = b, a + b
        cont = cont + 1


# agora vamos chamar a funcao
fib(10)