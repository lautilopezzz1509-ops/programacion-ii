import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

import numpy as np
from scipy.fft import fft, fftfreq
def espectro(senal, fs):
    n = len(senal)
    amplitudes = 2 * np.abs(fft(senal))[: n // 2] / n
    frecuencias = fftfreq(n, 1 / fs)[: n // 2]
    return frecuencias, amplitudes

def tono_dtfm(tecla,t,f):
    """hola"""
    fila = {"1": 697, "2": 697, "3": 697, "4": 770, "5": 770, "6": 770, 
        "7": 852, "8": 852, "9": 852, "*": 941, "0": 941, "#": 941}
    columna = {"1": 1209, "2": 1336, "3": 1477, "4": 1209, "5": 1336, "6": 1477, 
           "7": 1209, "8": 1336, "9": 1477, "*": 1209, "0": 1336, "#": 1477}
    x=np.linspace(0,t,1000000)
    teclastring=str(tecla)
    frecfila=fila[teclastring]
    freccol=columna[teclastring]
    senoidal= np.sin(frecfila*2*np.pi*x/1000)+np.sin(freccol*2*np.pi*x/1000)
    ruido= generarRuido(0.8,senoidal)
    return senoidal+ruido

def generarRuido(sigma,senal):
    rng = np.random.default_rng(3)
    ruido = rng.normal(0, sigma, len(senal))
    return ruido

def decodificar_tecla(senal,fs):
    fila = {"1": 697, "2": 697, "3": 697, "4": 770, "5": 770, "6": 770, 
        "7": 852, "8": 852, "9": 852, "*": 941, "0": 941, "#": 941}
    columna = {"1": 1209, "2": 1336, "3": 1477, "4": 1209, "5": 1336, "6": 1477, 
           "7": 1209, "8": 1336, "9": 1477, "*": 1209, "0": 1336, "#": 1477} 
    frecuencias,amplitudes=espectro(senal,fs)
    mascaraFila= (frecuencias>=650) & (frecuencias<=1000)
    mascaraCol = (frecuencias>=1150) & (frecuencias<=1550)
    AmaxFila=np.max(amplitudes[mascaraFila])
    AmaxCol=np.max(amplitudes[mascaraCol])
    indiceAmaxFila=np.argmax(amplitudes[mascaraFila])
    FparaAmaxFila=frecuencias[indiceAmaxFila]
    indiceAmaxCol=np.argmax(amplitudes[mascaraCol])
    FparaAmaxCol=frecuencias[indiceAmaxCol]
    moduloFila=[abs(FparaAmaxFila-np.array(list(fila.values())))]
    moduloCol=[abs(FparaAmaxCol-np.array(list(columna.values())))]
    moduFila=np.min(moduloFila)
    moduCol=np.min(moduloCol)
    ubiFila= moduloFila.index(moduFila)
    ubiCol= moduloCol.index(moduCol)

    print("La amplitud de fila mas alta fue: ",AmaxFila)
    print("La amplitud de columna mas alta fue: ",AmaxCol)
    print("La frecuencia de fila mas probable es: ",fila[str(ubiFila)])
    print("La frecuencia de columna mas probable es: ",columna[str(ubiCol)])
    return

def verInfo(tecla,tiempo,fs):
    funcion= tono_dtfm(tecla,tiempo,fs)
    decodificar_tecla(funcion,fs)
    plt.figure()
    t=np.linspace(0,tiempo,1000000)
    plt.plot(t,funcion)
    plt.title(f"Gráfico de señal para la tecla '{tecla}' ({tiempo} ms)")
    plt.xlabel("[ms]")
    plt.ylabel("V")
    plt.show()
    return

def main():
    verInfo(5,100,8000)
    

main()