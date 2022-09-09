import traceback
import webbrowser
import xml.etree.cElementTree as ET #para escribir el xml
from xml.dom import minidom as MD #para leer el xml
from lista import Lista

class Persona:
    def __init__(self,nombre:str,apellido:str,dpi:int,edad:int,correo:str,hermanos:int,porcentaje:float):
        self.nombre = nombre
        self.apellido = apellido
        self.dpi = dpi
        self.edad = edad
        self.correo = correo
        self.hermanos = hermanos
        self.porcentaje = porcentaje #no se ni que es esto :v jaja solo lo puse para tener un atributo float xd

    def mostrar(self): #metodo para mostrar atributos del paciente en consola
        print(f"      PERSONA:\n      Nombre:{self.nombre}\n      Apellido:{self.apellido}\n      DPI:{self.dpi}\n      Edad:{self.edad}\n" #estos son datos personales
             +f"      Correo:{self.correo}\n      Hermanos:{self.hermanos}\n      Porcentaje:{self.porcentaje}\n\n      ***********\n") #estos ya no son datos personales

#Voy a declarar una lista global donde se guardaran las personas
personas = Lista()

def escribir(): #Este metodo me sirve para escribir el archivo xml
    #0. vamos a llamar a nuestra variable global personas dentro de este metodo
    global personas
    if personas.elemento(0)==None:
        print("   --NO HAY PERSONAS REGISTRADAS--")
    else:
        try:
            #1. crear el nodo donde se van a almacenar todas las personas, en este caso el nodo es personas_xml
            personas_xml = ET.Element("personas") #se esta usando el importe xml.cElementTree como ET (linea 2 de este codigo)
            #2. crearemos cada nodo persona y lo agregaremos a nodo personas, iniciamos un ciclo for
            for iteracion in range(personas.longitud()):
                #aqui cree un nodo paciente, sin sus subnodos todavia
                persona = ET.SubElement(personas_xml,"paciente")
                #3. Creo el nodo de datospersonales, sin agregar informacion todavia
                datospersonales = ET.SubElement(persona,"datospersonales")
                #4. ahora agregare los atributos de la persona a datospersonales.
                ET.SubElement(datospersonales,"nombre").text=personas.elemento(iteracion).nombre
                ET.SubElement(datospersonales,"apellido").text=personas.elemento(iteracion).apellido
                ET.SubElement(datospersonales,"dpi").text=str(personas.elemento(iteracion).dpi)
                ET.SubElement(datospersonales,"edad").text=str(personas.elemento(iteracion).edad)
                #5. ahora agregare los atributos de la persona que no son datos personales
                ET.SubElement(persona,"correo").text=personas.elemento(iteracion).correo
                ET.SubElement(persona,"hermanos").text=str(personas.elemento(iteracion).hermanos)
                ET.SubElement(persona,"porcentaje").text=str(personas.elemento(iteracion).porcentaje)
            #6. despues de agregar todas las personas al nodo personas, vamos a conseguir la ruta donde
            #se va a crear el archivo xml de salida, en este caso siempre se va a crear en la misma ruta
            #porque estoy usando el mismo nombre cada vez que se escriba el archivo de salida xml xdd
            ruta = str(__file__).replace("\\","/").replace("main.py","")+"personas_salida.xml"
            #7. se escribe el archivo xml de salida:
            archivo_xml = ET.ElementTree(personas_xml)
            archivo_xml.write(ruta,xml_declaration=True,encoding='utf-8')
            #8. se abre el archivo de salida xml en el navegador (OPCIONAL) :v
            webbrowser.open(ruta) #se esta usando el importe webbrowser de la linea 1 
            print("   --PERSONAS ESCRITAS EXITOSAMENTE--")
        except:
            print("   **HUBO UN ERROR ESCRIBIENDO PERSONAS**")
            print(traceback.format_exc())
            
            
def leer(): #Este metodo me sirve para leer el archivo xml 
    #0. vamos a llamar a nuestra variable global personas dentro de este metodo
    global personas
    try:
        #1. Se pedira la ruta en donde esta el archivo xml a leer. Se usa try except si ocurre un error
        ruta = input("   INGRESE RUTA ARCHIVO XML:")
        #2.  creare la variable donde se va a almacenar el archivo xml, se va a llamar archivo_xml
        archivo_xml = MD.parse(ruta) #se esta usando el importe minidom como MD (linea 3 de este codigo)
        
        #3. vamos a obtener al nodo que contiene todas las personas, en este caso "personas". 
        # Los guardare en la variable todas_personas_xml
        todas_personas_xml = archivo_xml.getElementsByTagName("personas")[0] #se le pone un [0] porque
        #getElementsByTagName retorna un arreglo, como sabemos que solo hay un nodo personas en nuestro
        #archivo xml ponemos [0] porque es el unico elemento en la lista que se retorno de archivo_xml.getElementsByTagName("personas")
        
        #4. Ahora de todas_personas_xml debemos obtener todos los nodos persona, volvemos a hacer lo mismo que en el caso anterior
        #pero sin agregar [0], los nodos persona se van a guardar en la variable personas_xml
        personas_xml = todas_personas_xml.getElementsByTagName("persona") #No se agrego el [0] porque queremos todo el arreglo que
        #nos retorno todas_personas_xml.getElementsByTagName("persona")
        
        #5. Ahora recorreremos nuestro arreglo personas_xml con un for
        for persona_xml in personas_xml:
            #6. Vamos a obtener los datos personales, solo tenemos 1 nodo datospersonales por persona, 
            #entonces agregaremos el [0] despues del getElementsByTagName
            datospersonales = persona_xml.getElementsByTagName("datospersonales")[0]
            #de datospersonales, vamos a obtener nombre, apellido, dpi y edad PERO
            #no vamos a obtener directamente el nodo, sino la informacion que contiene el nodo, asi:
            nombre = datospersonales.getElementsByTagName("nombre")[0].firstChild.data
            apellido = datospersonales.getElementsByTagName("apellido")[0].firstChild.data
            dpi = int(datospersonales.getElementsByTagName("dpi")[0].firstChild.data)
            edad = int(datospersonales.getElementsByTagName("edad")[0].firstChild.data)
            #7 ahora vamos a obtener el resto de datos que no son datos personales
            correo = persona_xml.getElementsByTagName("correo")[0].firstChild.data
            hermanos = int(persona_xml.getElementsByTagName("hermanos")[0].firstChild.data)
            porcentaje = float(persona_xml.getElementsByTagName("porcentaje")[0].firstChild.data)
            #8. Ahora que tengo todos los datos para crear un objeto Persona, creo la persona
            persona = Persona(nombre,apellido,dpi,edad,correo,hermanos,porcentaje)
            #9. agrego a la persona a la mi lista personas
            personas.agregar(persona)
            #termina la iteracion para esta persona, continua el ciclo for
        print("   --PERSONAS LEIDAS EXITOSAMENTE--")
    except:
        print("   --ERROR CON ARCHIVO XML--")
        print(traceback.format_exc())

corriendo = True #variable que permite que el programa se siga ejecutando
if __name__ == "__main__":
    while corriendo:
        try:            
            print(
                "***MENU***"
                +"\n1.Leer xml"
                +"\n2.Escribir xml"
                +"\n3.Mostrar personas"
                +"\n4.Terminar")
            opcion = int(input("OPCION: "))
            if opcion == 1:
                leer()
            elif opcion == 2:
                escribir()
            elif opcion == 3:
                if personas.elemento(0)==None:
                    print("   **NO HAY PERSONAS REGISTRADAS")
                else:
                    print("\n      **********\n")
                    for iteracion in range(personas.longitud()):
                        personas.elemento(iteracion).mostrar()
            elif opcion == 4:
                corriendo = False
            else:
                print("   **OPCION NO DISPONIBLE**")
        except:
            print("   **OPCION NO VALIDA**")
