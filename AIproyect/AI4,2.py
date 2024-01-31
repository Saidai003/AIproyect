import string
import random
from collections import deque
from collections import Counter

class Mente:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.STM = deque(maxlen=X)
        self.LTM = {char: 50 for char in string.ascii_letters + 'áéíóúüñÁÉÍÓÚÜÑ'}

    def aprender(self, texto):
        with open(texto, 'r', encoding='utf-8') as f:
            for c in f.read():
                if c in self.LTM:
                    self.STM.append(c)
                    self.buscar()

    def buscar(self):
        for _ in range(self.Y):
            max_char = max(self.LTM, key=self.LTM.get)
            rand_num = random.randint(1, 100)
            self.LTM[max_char] = min(100, self.LTM[max_char] + 10) if self.LTM[max_char] >= rand_num else max(0, self.LTM[max_char] - 10)

    def practica(self, input, Z):
        for _ in range(Z):
            self.STM.extend(input)
            self.buscar()
            counter = Counter(self.STM)
            most_common_char = counter.most_common(1)[0][0]
            input += most_common_char
        print(f'El nuevo input es: {input}')

X = int(input('Ingrese X: '))
Y = int(input('Ingrese Y: '))
Z = int(input('Ingrese Z: '))
mente = Mente(X, Y)
mente.aprender('texto.txt')
input = input('Ingrese un input: ')
mente.practica(input, Z)
