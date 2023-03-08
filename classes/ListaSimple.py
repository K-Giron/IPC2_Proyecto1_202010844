class Lista_simple(): 
    def __init__(self):
        self.cabeza = None
    
    def agregar_al_inicio(self, dato):
        self.cabeza = Nodo(dato=dato, siguiente=self.cabeza)

class Nodo():
    def __init__(self, dato = None, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente