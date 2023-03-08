from classes.ListaSimple import Lista_simple

class Muestra:
    def __init__(self,codigo,descripcion,dimensionX,dimensionY) -> None:
        self.codigo=codigo
        self.descripcion=descripcion
        self.dimensionX=dimensionX
        self.dimensionY=dimensionY
        self.listaOrganismos = Lista_simple()
        self.listaCeldasVivas = Lista_simple()
        self.listaCeldasMuertas = Lista_simple()                                    

    def analizar(self):
        listaCeldasRegresar = Lista_simple()
        cambios = 0
        nodoActual = self.listaCeldasVivas.cabeza
        while nodoActual != None:
            celdaViva = nodoActual.dato
            nuevaCelda = celdaViva.analizar(self.listaCeldasVivas)
            if nuevaCelda != None:
                listaCeldasRegresar.agregar_al_inicio(nuevaCelda)
                cambios = cambios + 1
                    
            nodoActual = nodoActual.siguiente
        return {'listaCeldasVivas':listaCeldasRegresar, 'cambios':cambios}

    def buscarCeldaViva(self,x,y):
        nodoActual = self.listaCeldasVivas.cabeza
        while nodoActual != None:
            celdaViva = nodoActual.dato
            coordenadaX = celdaViva.x
            coordenadaY = celdaViva.y
            if (int(x)==int(coordenadaX) and int(y) == int(coordenadaY)):
                return celdaViva
            nodoActual = nodoActual.siguiente
        return None