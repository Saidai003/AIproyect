import string
import random
from collections import deque

class Mente:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.STM = deque(['' for _ in range(X)], maxlen=X)
        self.LTM = {char: 50 for char in string.ascii_letters + 'áéíóúüñÁÉÍÓÚÜÑ'}

    def aprender(self, texto):
        with open(texto, 'r', encoding='utf-8') as f:
            while True:
                c = f.read(1)
                if not c:
                    break
                if c in self.LTM:
                    self.STM.append(c)
                    self.buscar()

    def buscar(self):
        for _ in range(self.Y):
            max_char = max(self.LTM, key=self.LTM.get)
            rand_num = random.randint(1, 100)
            if self.LTM[max_char] >= rand_num:
                self.LTM[max_char] = min(100, self.LTM[max_char] + 10)
            else:
                self.LTM[max_char] = max(0, self.LTM[max_char] - 10)

    def practica(self, input, Z):
        for _ in range(Z):
            self.STM = deque(list(input), maxlen=self.X)
            self.buscar()
            rand_num = random.randint(1, 100)
            chars_greater_than_rand = [char for char in self.LTM if self.LTM[char] > rand_num]
            if chars_greater_than_rand:
                input += chars_greater_than_rand[0]
        print(f'El nuevo input es: {input}')

X = int(input('Ingrese X: '))
Y = int(input('Ingrese Y: '))
Z = int(input('Ingrese Z: '))
mente = Mente(X, Y)
mente.aprender('0_palabras_todas.txt')
input = input('Ingrese un input: ')
mente.practica(input, Z)
