import numpy as np
import math as m
def promedio(rssi):
    promediodBm= np.mean(rssi)
    print("El promedio en dBm es: ",promediodBm)
    Watt = (10 ** (rssi / 10)) / 1000
    promedioW= np.mean(Watt)
    print("El promedio en Watts es: ",promedioW)
    return

def minmax(rssi):
    max= np.max(rssi)
    min=np.min(rssi)
    posimax=np.argmax(rssi)
    posimin=np.argmin(rssi)
    print("Valor maximo: ",max," dado a las ",posimax,"horas")
    print("Valor minimo: ",min," dado a las ",posimin,"horas")
    return
def alerta(rssi):
    mascara = rssi < -75
    minimos = rssi[mascara]
    posiciones = np.where(mascara)[0]
    print("Los valores que superaron el umbral son: ", minimos, "\n y sus horas son: ", posiciones)
    return

def riesgo(rssi):
    mascara = (rssi >= -75) & (rssi < -72)
    print("La cantidad de horas de riesgo es: ", np.sum(mascara))
    return
def main():
    rssi = np.array([-68.2, -67.9, -67.5, -67.8, -68.0, -68.9,
    -70.4, -72.8, -74.1, -75.6, -76.3, -75.9,
    -74.8, -75.2, -76.8, -77.1, -75.4, -73.9,
    -72.2, -70.8, -69.9, -69.1, -68.7, -68.4])
    promedio(rssi)
    minmax(rssi)
    alerta(rssi)
    riesgo(rssi)
    return
main()
