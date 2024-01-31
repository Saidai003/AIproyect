class TreeNode:
    def __init__(self, peso=1, palabraroot=""):
        self.peso = peso
        self.palabraroot = palabraroot
        self.left = None
        self.right = None
        self.opcion = None

    def init(self, pesoParam, palabrarootParam):
        self.peso = pesoParam
        self.palabraroot = palabrarootParam

        if self.opcion is None:
            self.opcion = TreeNode(pesoParam, palabrarootParam)
        elif self.opcion.peso <= pesoParam and self.right.opcion is None:
            self.right.opcion = TreeNode(pesoParam, palabrarootParam)
        elif self.opcion.peso > pesoParam:
            if self.left.opcion is None:
                self.left.opcion = TreeNode(pesoParam, palabrarootParam)
            else:
                self.left.left.opcion = TreeNode(pesoParam, palabrarootParam)
        elif self.right.opcion.peso < pesoParam:
            if self.right.right.opcion is None:
                self.right.right.opcion = TreeNode(pesoParam, palabrarootParam)
            else:
                self.right.right.right.opcion = TreeNode(pesoParam, palabrarootParam)
        else:
            if self.right.left.opcion is None:
                self.right.left.opcion = TreeNode(pesoParam, palabrarootParam)
            else:
                self.right.left.left.opcion = TreeNode(pesoParam, palabrarootParam)

    def LTM(self, palabra):
        if self.palabraroot == palabra:
            return self
        elif self.left and self.left.palabraroot <= palabra:
            return self.left.LTM(palabra)
        elif self.right and self.right.palabraroot > palabra:
            return self.right.LTM(palabra)
        else:
            return None


if __name__ == "__main__":
    print("Procesando")

    Cerebro = None
    peso = 1

    with open("0_palabras_todas.txt", "r", errors="ignore") as file:
        for line in file:
            palabra = line.strip()  # Elimina los espacios en blanco al principio y al final

            if Cerebro is None:
                Cerebro = TreeNode(peso, palabra)
            else:
                Cerebro.init(peso, palabra)
                peso += 1
    palabra_buscar = input("Por favor, introduce una palabra para buscar en Cerebro: ")
    nodo = Cerebro.LTM(palabra_buscar)
    if nodo:
        print(f"La palabra '{palabra_buscar}' fue encontrada en Cerebro con un peso de {nodo.peso}.")
    else:
        print(f"La palabra '{palabra_buscar}' no fue encontrada en Cerebro.")
    print("Proceso terminado, se procesaron todas las palabras del archivo")
