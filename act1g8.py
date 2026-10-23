import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq


def tono_dtfm(tecla,t,f):
    fila = {"1": 697, "2": 697, "3": 697, "4": 770, "5": 770, "6": 770, 
        "7": 852, "8": 852, "9": 852, "*": 941, "0": 941, "#": 941}
    columna = {"1": 1209, "2": 1336, "3": 1477, "4": 1209, "5": 1336, "6": 1477, 
           "7": 1209, "8": 1336, "9": 1477, "*": 1209, "0": 1336, "#": 1477}
    x=np.linspace(0,t,1000000)
    verNyquist(1477,f)
    teclastring=str(tecla)
    frecfila=fila[teclastring]
    freccol=columna[teclastring]
    senoidal= np.sin(frecfila*2*np.pi*x/1000)+np.sin(freccol*2*np.pi*x/1000)
    return senoidal

def verNyquist(frecuenciaTonoMayor,frecuenciaEmitida):
    frecuenciaTonoMayor=frecuenciaTonoMayor*2
    if(frecuenciaEmitida>=frecuenciaTonoMayor):
        print("Cumple Nyquist")
    else:
        print("No cumple Nyquist")
    return

def verInfo(tecla,tiempo,fs):
    funcion= tono_dtfm(tecla,tiempo,fs)
    plt.figure()
    t=np.linspace(0,tiempo,1000000)
    plt.plot(t,funcion)
    plt.title(f"Gráfico de señal para la tecla '{tecla}' ({tiempo} ms)")
    plt.xlabel("[ms]")
    plt.ylabel("Hz")
    plt.show()
    return

def main():
    verInfo(5,100,8000)
    verInfo(1,20,8000)
    verInfo(9,20,8000)

main()