class Lista_simple(): 
    def __init__(self):
        self.cabeza = None
    
    def agregar_al_inicio(self, dato):
        self.cabeza = Nodo(dato=dato, siguiente=self.cabeza)

    def contador(self):
        contador = 0
        nodoActual = self.cabeza
        while nodoActual != None:
            contador = contador + 1
            nodoActual = nodoActual.siguiente
        return contador

class Nodo():
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente

    