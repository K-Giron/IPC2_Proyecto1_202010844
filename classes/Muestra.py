from classes.ListaSimple import Lista_simple

class Muestra:
    def __init__(self,codigo,descripcion,dimensionX,dimensionY) -> None:
        self.codigo=codigo
        self.descripcion=descripcion
        self.dimensionX=dimensionX
        self.dimensionY=dimensionY
        self.listaOrganismos = Lista_simple()
        self.listaCeldasVivas = Lista_simple()