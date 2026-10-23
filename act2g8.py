import numpy as np
import matplotlib.pyplot as plt
import math as m
from scipy.fft import fft, fftfreq
def generarTono(frec,tiempomS):
    x=np.linspace(0,1000,8000)
    senalSenoidal = np.sin(frec*2*np.pi*x/1000)
    return senalSenoidal

def generarRuido(sigma,senal):
    rng = np.random.default_rng(2)
    ruido = rng.normal(0, sigma, len(senal))
    return ruido

def calculoPot(funcion):
    return np.mean(funcion**2)

def snr_db(senal,ruido):
    Psenal=calculoPot(senal)
    Pruido=calculoPot(ruido)
    return 10*m.log10(Psenal/Pruido)

def sigma_para_snr(senal,snr_db):
    Psenal=calculoPot(senal)
    return (Psenal/(10**(snr_db/10)))**0.5

def mostrarInfo(senal,ruido1,ruido2,ruido3,ruido4,tmS):
    plt.figure()
    x=np.linspace(0,tmS,8000)
    plt.subplot(2,2,1)
    plt.plot(x,(senal+ruido1))
    plt.title("Para SNR=20")
    plt.xlabel("tiempo [ms]")
    plt.ylabel("SNR [dB]")
    plt.subplot(2,2,2)
    plt.plot(x,senal+ruido2)
    plt.title("Para SNR=10")
    plt.xlabel("tiempo [ms]")
    plt.ylabel("SNR [dB]")
    plt.subplot(2,2,3)
    plt.plot(x,senal+ruido3)
    plt.title("Para SNR=0")
    plt.xlabel("tiempo [ms]")
    plt.ylabel("SNR [dB]")
    plt.subplot(2,2,4)
    plt.plot(x,senal+ruido4)
    plt.title("Para SNR=-5")
    plt.xlabel("tiempo [ms]")
    plt.ylabel("SNR [dB]")
    plt.show()
    return

def ordenarCalculos(f,tS,snr1,snr2,snr3,snr4):
    senal = generarTono(f,tS)
    sigma1 =sigma_para_snr(senal,snr1)
    ruido1 = generarRuido(sigma1,senal)
    sigma2 =sigma_para_snr(senal,snr2)
    ruido2 = generarRuido(sigma2,senal)
    sigma3 =sigma_para_snr(senal,snr3)
    ruido3 = generarRuido(sigma3,senal)
    sigma4 =sigma_para_snr(senal,snr4)
    ruido4 = generarRuido(sigma4,senal)
    mostrarInfo(senal,ruido1,ruido2,ruido3,ruido4,tS)
    return

def main():
    tiempoMuestreoms=5
    frecuencia=8000
    ordenarCalculos(8000,5,20,10,0,-5)
    return
main()