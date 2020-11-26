def contar_rutas_mas_cortas(C):
    Filas = len(C)
    Columnas = len(C[0])    
    if C[Filas-1][Columnas-1] != 1:
        caminos = []                                            #Lista donde se guardan los caminos 
        pdinamica(C, caminos, 0, 0, Filas, Columnas)            #Funcion recursiva
        return res
    else:
        return 0
    
res = 0                                                     #variable global, guarda cantidad de caminos
 
def pdinamica(C, caminos, f, c, Filas, Columnas):
    global res                                              
    if f == Filas - 1 and c == Columnas - 1:                #Si llego a la ultima casilla
        res += 1
        return 

    caminos.append(C[f][c])                                 #Guarda la casilla en la lista
    
    if 0 <= f < Filas and 0 <= c + 1 < Columnas and C[f][c+1] != 1:         #Comprueba si se puede mover a la derecha
        pdinamica(C, caminos, f, c + 1, Filas, Columnas)
 
    
    if 0 <= f + 1 < Filas and 0 <= c < Columnas and C[f+1][c] != 1:         #Comprueba si se puede mover hacia abajo
        pdinamica(C, caminos, f + 1, c, Filas, Columnas)
 
    
    caminos.pop()                                           #Si no se puede mover, sale de la lista
