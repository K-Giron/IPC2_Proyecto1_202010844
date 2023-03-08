from os import system
from tkinter.filedialog import askopenfilename
from xml.dom import minidom
from classes.Muestra import Muestra
from classes.Organismo import Organismo
from classes.CeldaViva import CeldaViva
from classes.ListaSimple import Lista_simple

class Menu:

    muestraAnalizada:Muestra
    muestrasAnalizadas: Lista_simple() = Lista_simple()

    def __init__(self) -> None:
        self.opciones=[
            ' Abrir muestra',
            ' Graficar muestra',
            ' Analizar muestra',
            ' Generar XML',
            ' Acerca de',
            ' Salir'
        ]

    def mostrar(self,error:bool) -> None:
        system("cls")
        
        print('         __________________________           ')
        print('        |        Proyecto 1        |          ')
        print('        |        Muestras          |          ')
        print('        |--------------------------|          \n')

        i = 0

        
        for opcion in self.opciones:
            i = i + 1
            print("\t",i," - "+opcion)
        
        if(error):
            print('\n            OPCION INCORRECTA!!               ')

        opcion = input('\nEscribe tu opcion: ')
        self.ejecutarOpcion(opcion)
        
    
    def pausa(self):
        espera = input('Presiona cualquier tecla para continuar...\n')     
        self.mostrar(False)

    def ejecutarOpcion(self,opcion:str) -> None:
        if(opcion=='1'):
            filename = askopenfilename()
            objetoXml = minidom.parse(filename)
            self.procesarInformacion(objetoXml)
            self.pausa()
        elif(opcion=='2'):
            self.graficarMuestra(self.muestraAnalizada)
            self.pausa()
        elif(opcion=='3'):
            self.analizarMuestra()
            self.pausa()
        elif(opcion=='5'):
            espera = input('\n\tUSAC - S1\n\tProyecto 1\n\tDesarrollado por Kevin Girón-202010844...')
            self.pausa()  
        elif(opcion=='6'):
            quit()
        else:
            self.mostrar()

    def procesarInformacion(self,objetoXML):
 
        coleccionX  = objetoXML.getElementsByTagName('columnas')
        coleccionY  = objetoXML.getElementsByTagName('filas')
        muestra     = objetoXML.getElementsByTagName('muestra')

        codigoMuestra       = muestra[0].childNodes[1].firstChild.data 
        descripcionMuestra  = muestra[0].childNodes[3].firstChild.data 

        dimensionX = coleccionX[0].childNodes[0].data
        dimensionY = coleccionY[0].childNodes[0].data

        nuevaMuestra  =  Muestra(codigoMuestra,descripcionMuestra,dimensionX,dimensionY)

        organismosXML = objetoXML.getElementsByTagName('organismo')

        letra = 65
        for organismo in organismosXML:

            codigo = organismo.childNodes[1].firstChild.data
            nombre = organismo.childNodes[3].firstChild.data
            nuevoOrganismo = Organismo(codigo,nombre,letra)
            nuevaMuestra.listaOrganismos.agregar_al_inicio(nuevoOrganismo)
            letra = letra + 1

        celdasVivasXML = objetoXML.getElementsByTagName('celdaViva')

        for celdaViva in celdasVivasXML:

            fila            = celdaViva.childNodes[1].firstChild.data
            columna         = celdaViva.childNodes[3].firstChild.data
            codigoOrganismo = celdaViva.childNodes[5].firstChild.data

            nuevaCeldaViva  = CeldaViva(codigoOrganismo,int(columna),int(fila))

            nuevaMuestra.listaCeldasVivas.agregar_al_inicio(nuevaCeldaViva)

        self.muestraAnalizada = nuevaMuestra
        print('Archivo cargado con exito!!')

    def graficarMuestra(self, muestra, contador = 0):
        
        x   = muestra.dimensionX
        y   = muestra.dimensionY

        codigoGraphiz = """
            digraph structs {
                node [shape=record];
                MATRIZ [
                    label="
                    
        """
        cuentaX = -1
        cuentaY = -1
        while (cuentaX < int(x)):
            if(cuentaY == -1):
                codigoGraphiz=codigoGraphiz+'{x,y'
            else:
                codigoGraphiz=codigoGraphiz+'{'+str(cuentaX)
            
            cuentaY = 0 
            
            while (cuentaY < int(y)):
                
                if(cuentaX == -1):
                    codigoGraphiz=codigoGraphiz+'|'+str(cuentaY)
                else:
                    listaCeldasVivas  = muestra.listaCeldasVivas
                    nodoActual = listaCeldasVivas.cabeza

                    codigoOrganismo = ""
                    while nodoActual != None:
                       
                        celdaViva:CeldaViva = nodoActual.dato
                        coordenadaX = int(celdaViva.x)
                        coordenadaY = int(celdaViva.y)
                        
                        if (int(cuentaX)==int(coordenadaX) and int(cuentaY) == int(coordenadaY)):
                            
                            inicio = muestra.listaOrganismos.cabeza
                            while(inicio!=None):
                                organismo:Organismo = inicio.dato
                                
                                if(celdaViva.organismo==organismo.codigo):
                                    codigoOrganismo='|'+chr(organismo.letra)
                                    break
                                inicio=inicio.siguiente
                            break
                        else:
                            codigoOrganismo='|-'
                        nodoActual = nodoActual.siguiente

                    codigoGraphiz = codigoGraphiz + codigoOrganismo
                cuentaY = cuentaY + 1
                
            cuentaX = cuentaX + 1
            
            if(cuentaX == int(x)):
                codigoGraphiz=codigoGraphiz+'}'
            else:
                codigoGraphiz=codigoGraphiz+'}|'

        codigoGraphiz =codigoGraphiz+ """
                        "];
        """
        inicio = muestra.listaOrganismos.cabeza
        codigoGraphiz =codigoGraphiz+"\""
        while(inicio!=None):
            organismo:Organismo = inicio.dato
            codigoGraphiz =codigoGraphiz +chr(organismo.letra)+"-"+organismo.codigo+"\n"
            inicio=inicio.siguiente
        codigoGraphiz =codigoGraphiz+ """
                        \"}     
        """
        archivo = open("./img/muestra" + str(contador) + ".txt","w")
        archivo.write(codigoGraphiz)
        print("Creando imagen...")
        archivo.close()
        system("dot -Tpng ./img/muestra" + str(contador) + ".txt -o ./img/muestra" + str(contador) + ".png")
        system("start ./img/muestra" + str(contador) + ".png")

    def analizarMuestra(self):
        print('Analizando muestra...')
        respuesta = self.muestraAnalizada.analizar()
        cambios = respuesta['cambios']
        if cambios > 0:
            self.nuevaMuestra(respuesta)
        step = 0
        # recorrer muestras analizadas
        nodoActual = self.muestrasAnalizadas.cabeza
        while nodoActual != None:
            step = step + 1
            muestraAnalizada:Muestra = nodoActual.dato
            respuesta = muestraAnalizada.analizar()
            cambios = respuesta['cambios']
            print('Cambios por aca: ' + str(cambios))
            if cambios > 0:
                self.nuevaMuestra(respuesta)
            if step < 3:
                nodoActual = nodoActual.siguiente



    def nuevaMuestra(self, respuesta):
        nuevaMuestra = Muestra(self.muestraAnalizada.codigo,self.muestraAnalizada.descripcion,self.muestraAnalizada.dimensionX,self.muestraAnalizada.dimensionY)
        nuevaMuestra.listaOrganismos = self.muestraAnalizada.listaOrganismos
        nuevaMuestra.listaCeldasVivas = respuesta['listaCeldasVivas']

        self.muestrasAnalizadas.agregar_al_inicio(nuevaMuestra)
        print('Nueva muestra generada')
        self.graficarMuestra(nuevaMuestra, self.muestrasAnalizadas.contador())
        print('Muestra graficada')

        return nuevaMuestra


    def generateXml(self):
        print("Generando XML...")
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<datosMarte>'
        xml += '<listaOrganismos>'

        temp = self.head
        while temp != None:
            xml += f"""
    <organismo>
        <codigo>{temp.dato.getName()}</nombre>
        <nombre>{temp.dato.getAge()}</edad>
        <periodos>{temp.dato.getAge() }</periodos>
        <m>{temp.dato.getSize()}</m>
        <resultado>{temp.dato.getResult()}</resultado>
    </paciente>"""
            temp = temp.next

        xml += '</listaOrganismo>'
        xml += '</datosMarte>'
        file = open('pacientes-salida.xml', 'w')
        file.write(xml)
        file.close()
        print("XML generado correctamente")
    