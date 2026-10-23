import numpy as np
import math as m
import matplotlib.pyplot as plt
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

def mostrarInfo(pTx,gTx):
     x=np.linspace(0.5,40,100)
     plt.figure()
     plt.subplot(2,1,1)
     potencia24= calculoPot(x,2.4,pTx,gTx,gTx)
     posimax24=np.argmax(potencia24)
     plt.plot(x,potencia24)
     plt.title("Potencia recibida para 2.4GHz")
     plt.axhline(-75,color="red",linestyle="--")
     plt.axvline(posimax24,color="black",linestyle="--")
     plt.grid()
     plt.xlabel("[Km]")
     plt.ylabel("dBm")


     plt.subplot(2,1,2)
     potencia58=calculoPot(x,5.8,pTx,gTx,gTx)
     posimax58=np.argmax(potencia58)
     plt.plot(x,potencia58)
     plt.title("Potencia recibida para 5.8GHz")
     plt.axhline(-75,color="red",linestyle="--")
     plt.axvline(posimax58,color="black",linestyle="--")
     plt.grid()
     plt.xlabel("[Km]")
     plt.ylabel("dBm")
     plt.tight_layout()
     plt.show()
     return

def main():
    distancia = np.array([2.5,8.0,12.0,3.0,15.0,20.0,6.5,28.0])
    frecuencia = np.array([5.8,5.8,5.8,2.4,2.4,2.4,5.8,2.4])
    potenciaTx = 23
    gananciaAntena = 15
    calculoPot(distancia,frecuencia,potenciaTx,gananciaAntena,gananciaAntena)
    mostrarInfo(potenciaTx,gananciaAntena)
    return
main()