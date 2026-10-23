import numpy as np
import matplotlib.pyplot as plt
import math
def ganancia_parabolica(diametro_m, frecuencia_hz, eficiencia):
    c=3e8
    resultado = 10*math.log10(eficiencia*((math.pi*diametro_m/(c/frecuencia_hz))**2))
    return print("La ganancia para ",diametro_m,"m y ",frecuencia_hz,"MHz es de: ",resultado)
def main():
    diametros = [0.3,0.6,1.2]
    frecuencia = [5.8,11]
    eficiencia5 = 0.55
    for i in diametros:
        for j in frecuencia:
            f=j*1000000
            ganancia_parabolica(i,f,eficiencia5)
main()