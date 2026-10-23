import numpy as np
import math as m

def calculoFSPL(d,f):
    return 20 * np.log10((4 * np.pi * (d * 1000) * (f * 1e9)) / 3e8)

def calculoPot(d,f,pTx,gTx,gRx):
        return pTx + gTx + gRx - calculoFSPL(d,f)

def verificacion(d, f, pTx, gTx, gRx):
    paperRex = calculoPot(d, f, pTx, gTx, gRx)
    margen = paperRex - (-75)
    clasificacion = np.where(margen < 0, "FALLA", "OK")
    return clasificacion

def contarfallas(d, f, pTx, gTx, gRx):
    paperRex = calculoPot(d, f, pTx, gTx, gRx)
    margen = paperRex + 75 < 0 # Forma corta de Prx - (-75)
    return np.sum(margen)

def main():
    enlace = np.array(["E1","E2","E3","E4","E5","E6","E7","E8"])
    distancia = np.array([2.5,8.0,12.0,3.0,15.0,20.0,6.5,28.0])
    frecuencia = np.array([5.8,5.8,5.8,2.4,2.4,2.4,5.8,2.4])
    potenciaTx = 23
    gananciaAntena = 15
    print("El FSPL es: ", calculoFSPL(distancia, frecuencia))
    print("Las fallas son: ", verificacion(distancia, frecuencia, potenciaTx, gananciaAntena, gananciaAntena))
    print("y en total son: ", contarfallas(distancia, frecuencia, potenciaTx, gananciaAntena, gananciaAntena))
    return
main()