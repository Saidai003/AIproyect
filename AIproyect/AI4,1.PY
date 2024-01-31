import random
from collections import deque

class Nodo:
    def __init__(self, caracter):
        self.caracter = caracter
        self.almacenamiento = {}
        self.LTM = [chr(i) for i in range(128)]
        self.LTMsetup = sorted(self.LTM)

class Cerebro:
    def __init__(self):
        self.STM = {}

    def llenar_LTMsetup(self):
        for nodo in self.STM.values():
            nodo.LTMsetup = sorted(nodo.LTM)

    def reemplazar_LTM(self):
        for nodo in self.STM.values():
            nodo.LTM = nodo.LTMsetup[:]

    def aprender(self, texto, tamano_memoria):
        memoria = deque(maxlen=tamano_memoria)
        with open(texto, 'r') as f:
            while True:
                caracter = f.read(1)
                if not caracter:
                    break
                memoria.append(caracter)
                self.analizar(memoria)

    def analizar(self, memoria):
        for caracter in sorted(memoria):
            if caracter in self.STM:
                nodo = self.STM[caracter]
                indice = random.randint(0, len(nodo.LTMsetup) - 1)
                caracter_encontrado = nodo.LTMsetup[indice]
                # Aquí se realiza el resto de la lógica de análisis

def main():
    cerebro = Cerebro()
    tamano_memoria = int(input("Ingrese el tamaño de la memoria: "))
    cerebro.aprender('texto.txt', tamano_memoria)

if __name__ == "__main__":
    main()
