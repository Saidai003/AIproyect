import os
import random

class TreeNode:
    def __init__(self, peso=1, palabraroot=""):
        self.peso = peso
        self.palabraroot = palabraroot
        self.left = None
        self.right = None
        self.height = 1

    def init(self, pesoParam, palabrarootParam):
        nuevo_nodo = TreeNode(pesoParam, palabrarootParam)
        if not self.palabraroot:
            self.peso = pesoParam
            self.palabraroot = palabrarootParam
            self.height = 1
        else:
            actual = self
            while True:
                if palabrarootParam < actual.palabraroot:
                    if actual.left is None:
                        actual.left = nuevo_nodo
                        break
                    else:
                        actual = actual.left
                else:
                    if actual.right is None:
                        actual.right = nuevo_nodo
                        break
                    else:
                        actual = actual.right
            self.rebalance_tree()

    def rebalance_tree(self):
        balance = self.getBalance(self)
        if balance > 1:
            if self.left and self.left.getBalance() < 0:
                self.left = self.leftRotate(self.left)
            self = self.rightRotate(self)
        elif balance < -1:
            if self.right and self.right.getBalance() > 0:
                self.right = self.rightRotate(self.right)
            self = self.leftRotate(self)
        return self


    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return x

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def recorrer_nodos(self, Cerebro):
        nodos = []
        if Cerebro is not None:
            nodos.append(Cerebro)
            nodos.extend(self.recorrer_nodos(Cerebro.left))
            nodos.extend(self.recorrer_nodos(Cerebro.right))
        return nodos

def LTM(cerebro: TreeNode, palabra: str):
    if palabra is not None:
        print(cerebro.palabraroot)
        if cerebro is None:
            return None
        if palabra == cerebro.palabraroot:
            return cerebro
        elif palabra < cerebro.palabraroot:
            return LTM(cerebro.left, palabra)
        else:
            return LTM(cerebro.right, palabra)


def process_file(filename, Cerebro):
        with open(filename, "r", errors="ignore") as file:
            for line in file:
                palabras = line.strip().split()  # Divide la línea en palabras
                for i in range(0, len(palabras), 11):  # Procesa cada grupo de 11 palabras
                    nodos = []
                    for j in range(10):  # Procesa las primeras 10 palabras
                        palabra = palabras[i + j]
                        nodo = Cerebro.LTM(palabra)
                        if nodo:
                            nodos.append(nodo)
                    # Compara la palabra número 11 con la palabra encontrada en los nodos
                    if i + 10 < len(palabras) and nodos and nodos[-1].palabraroot == palabras[i + 10]:
                        for nodo in nodos:
                            nodo.peso = min(10, nodo.peso + 1)
                    else:
                        for nodo in nodos:
                            nodo.peso = max(1, nodo.peso - 1)

def recorrer_nodos_y_mostrar(Cerebro):
    if Cerebro is not None:
        recorrer_nodos_y_mostrar(Cerebro.left)
        print(f"Palabra: {Cerebro.palabraroot}, Peso: {Cerebro.peso}")
        recorrer_nodos_y_mostrar(Cerebro.right)


if __name__ == "__main__":
    print("Procesando")

    Cerebro = None
    peso = 1

    # Procesa el primer archivo
    with open("0_palabras_todas", "r", errors="ignore") as file:
        for line in file:
            palabra = line.strip()  # Elimina los espacios en blanco al principio y al final

            if Cerebro is None:
                Cerebro = TreeNode(peso, palabra)
            else:
                Cerebro.init(peso, palabra)
                
    # Procesa los archivos restantes en el directorio
    for filename in os.listdir("Aprender"):  # Cambia "." por el nombre de tu directorio
        if filename.endswith(".txt") and filename != "0_palabras_todas":
            process_file(os.path.join("Aprender", filename), Cerebro)

    print("Proceso terminado, se procesaron todas las palabras de los archivos")

    # Uso de la función para recorrer el árbol y mostrar las palabras y pesos
    recorrer_nodos_y_mostrar(Cerebro)

    
    # Solicita al usuario una palabra para buscar en Cerebro
    #while(input != 0):
        #palabra_buscar = input("Por favor, introduce una palabra para buscar en Cerebro: ")
        #nodo = Cerebro.LTM(str(input))
        #nodo = LTM(Cerebro, palabra_buscar)
        #if nodo:
        #    print(f"La palabra '{palabra_buscar}' fue encontrada en Cerebro con un peso de {nodo.peso}.")
        #else:
        #    print(f"La palabra '{palabra_buscar}' no fue encontrada en Cerebro.")
    
    
            