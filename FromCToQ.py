'''Programa de simulacion de lo clasico a lo cuantico
    Mateo Olaya Garzon
    Septiembre 2021 '''

def matriz_nxn(tamaño):
    '''Funcion que se encarga de crear una matriz cuadrada del tamaño indicado
        ( int ) -> list'''
    a= []
    for i in range(tamaño):
        fila = [0] * tamaño
        a += [fila]
    return a

def c_matriz(filas, columnas):
    '''Funcion que se encarga de crear una matriz del tamaño indicado
        ( int, int ) -> list'''
    a = []
    for i in range(filas):
        fila = [0] * columnas
        a += [fila]
    return a

def vector(tamaño):
    '''Funcion que crea un vector del tamaño indicado
        ( int ) -> list'''
    a = []
    for i in range(tamaño):
        a += [0]
    return a

def v_estado(matriz, v_inicial):
    '''Funcion que multiplica la matriz inicial y el vector de estado (siempre y cuando se cumplan los requisitos de la multipicacion de matrices)
        ( list, list ) -> list'''
    a = vector(len(v_inicial))
    for i in range(len(v_inicial)):
        temp  = 0
        for j in range(len(matriz)):
            temp += matriz[i][j] * v_inicial[j]
        a[i] = temp
    return a
    
#Programing Drill 3.1.1
def v_final(matriz, v_inicial, clicks):
    '''Funcion que entrega el vector de estado despues de un numero de clicks especifico
        ( list, list, int) -> list'''
    a = vector(len(v_inicial))
    b = vector(len(v_inicial))
    x = 0
    while x < clicks:
        if x == 0:
            for i in range(len(v_inicial)):
                temp  = 0
                for j in range(len(matriz)):
                    temp += matriz[i][j] * v_inicial[j]
                b[i] = temp
            a = list(b)
        else:
            for i in range(len(v_inicial)):
                temp  = 0
                for j in range(len(matriz)):
                    temp += matriz[i][j] * b[j]
                a[i] = temp
            b = list(a)
        x += 1
    return a

#Programing Drill 3.2.1
def v_final(matriz, v_inicial, clicks):
    '''Funcion que entrega el vector de estado despues de un numero de clicks especifico
        ( list, list, int) -> list'''
    a = vector(len(v_inicial))
    b = vector(len(v_inicial))
    x = 0
    while x < clicks:
        if x == 0:
            for i in range(len(v_inicial)):
                temp  = 0
                for j in range(len(matriz)):
                    temp += matriz[i][j] * v_inicial[j]
                b[i] = temp
            a = list(b)
        else:
            for i in range(len(v_inicial)):
                temp  = 0
                for j in range(len(matriz)):
                    temp += matriz[i][j] * b[j]
                a[i] = temp
            b = list(a)
        x += 1
    return a

#Programing Drill 3.2.2 
def matxmat(matriz):
    '''Funcion que multiplica una matriz por si misma
        ( list ) -> list'''
    a = matriz_nxn(len(matriz))
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            temp = 0
            for k in range(len(matriz[i])):
                temp += matriz[i][k] * matriz[k][j]
            a[i][j] = temp
    return a

def v_probabilidad(matriz, v_inicial):
    '''Funcion que calcula el vector de estado de una matriz de probabilidad de posicion (M^2X)
        ( list, list ) -> list'''
    a = matxmat(matriz)
    b = v_estado(a, v_inicial)
    return b

#Programig Drill 3.3.1
def v_final(matriz, v_inicial, clicks):
    '''Funcion que entrega el vector de estado despues de un numero de clicks especifico
        ( list, list, int) -> list'''
    a = vector(len(v_inicial))
    b = vector(len(v_inicial))
    x = 0
    while x < clicks:
        if x == 0:
            for i in range(len(v_inicial)):
                temp  = 0
                for j in range(len(matriz)):
                    temp += matriz[i][j] * v_inicial[j]
                b[i] = temp
            a = list(b)
        else:
            for i in range(len(v_inicial)):
                temp  = 0
                for j in range(len(matriz)):
                    temp += matriz[i][j] * b[j]
                a[i] = temp
            b = list(a)
        x += 1
    return a

#Programing Drill 3.3.2
def mat_interference(matriz):
    '''Funcion que multiplica una matriz por si misma y halla las posiciones donde se presenta una interferencia
        ( list ) -> list'''
    a = []
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            temp = 0
            for k in range(len(matriz[i])):
                temp1 = matriz[i][k] * matriz[k][j] + temp
                if temp1 == temp and (matriz[i][j] != 0 or matriz[j][i] != 0):
                    a += [[i,j]]
    return a