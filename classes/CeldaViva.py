class CeldaViva:
    def __init__(self,organismo,x,y) -> None:
        self.x=x
        self.y=y
        self.organismo=organismo

    def obtenerPosicion(self,dimensionXdeMatriz)->int:
        return self.x+self.y * dimensionXdeMatriz;

    def analizar(self, lista):
        nuevaCelda = None
        
        vertical = self.analizarVertical(lista)
        horizontal = self.analizarHorizontal(lista)
        diagonal = self.analizarDiagonal(lista)

        if (vertical != None):
            return CeldaViva(vertical, self.x, self.y)
        if (horizontal != None):
            return CeldaViva(horizontal, self.x, self.y)
        if (diagonal != None):
            return CeldaViva(diagonal, self.x, self.y)

        return nuevaCelda

    def analizarVertical(self, lista):
        a = [0, 0, 0]
        b = [0, 0, 0]
        nodoActual = lista.cabeza
        while nodoActual != None:
            celdaViva = nodoActual.dato
            for i in range(2, 0, -1):
                if (celdaViva.x == self.x and celdaViva.y == self.y + i):
                    if (self.organismo == self.organismo):
                        a[i] = celdaViva.organismo
                if (celdaViva.x == self.x and celdaViva.y == self.y - i):
                    if (self.organismo == self.organismo):
                        b[i] = celdaViva.organismo

            for i in range(2, 0, -1):
                if (a[i] == self.organismo and b[i] == self.organismo):
                    return celdaViva.organismo

            nodoActual = nodoActual.siguiente

        return None

    def analizarHorizontal(self, lista):
        a = [0, 0, 0]
        b = [0, 0, 0]
        nodoActual = lista.cabeza
        while nodoActual != None:
            celdaViva = nodoActual.dato

            for i in range(2, 0, -1):
                if (celdaViva.x == self.x + i and celdaViva.y == self.y):
                    if (self.organismo == self.organismo):
                        a[i] = celdaViva.organismo
                if (celdaViva.x == self.x - i and celdaViva.y == self.y):
                    if (self.organismo == self.organismo):
                        b[i] = celdaViva.organismo

            for i in range(2, 0, -1):
                if (a[i] == self.organismo and b[i] == self.organismo):
                    return celdaViva.organismo

            nodoActual = nodoActual.siguiente
        return None

    def analizarDiagonal(self, lista):
        a = [0, 0, 0]
        b = [0, 0, 0]
        nodoActual = lista.cabeza
        while nodoActual != None:
            celdaViva = nodoActual.dato

            for i in range(2, 0, -1):
                if (celdaViva.x == self.x + i and celdaViva.y == self.y + i):
                    if (self.organismo == self.organismo):
                        a[i] = celdaViva.organismo
                if (celdaViva.x == self.x - i and celdaViva.y == self.y - i):
                    if (self.organismo == self.organismo):
                        b[i] = celdaViva.organismo

            for i in range(2, 0, -1):
                if (a[i] == self.organismo and b[i] == self.organismo):
                    return celdaViva.organismo

            nodoActual = nodoActual.siguiente

        return None