class Lista:
    #constructor de Lista
    def __init__(self):
        self.__cabecera=Nodo(None) #cabecera es el nodo raiz de la lista

    #agrega un objeto a la lista
    def agregar(self,atributo:any):
        if self.__cabecera.getAtributo() == None:
            self.__cabecera.setAtributo(atributo)
        else:
            nodoAux = self.__ultimo(self.__cabecera)
            nodoAux.setSiguiente(Nodo(atributo))
    
    #funcion recursiva que retorna el ultimo nodo de una lista
    def __ultimo(self,nodo):
        if nodo.getSiguiente()==None:
            return nodo
        else:
            return self.__ultimo(nodo.getSiguiente())
    
    #retorna el atributo del ultimo nodo
    def ultimo(self):
        return self.__ultimo(self.__cabecera).getAtributo()
    
    #funcion que retorna el atributo del nodo en la posicion n
    # retorna None si la posicion no existe en la lista
    def elemento(self,n):
        try:
            nodo = self.__cabecera
            contador = 0
            while contador < int(n):
                nodo = nodo.getSiguiente()
                if nodo == None:
                    return None
                contador+=1
            return nodo.getAtributo()
        except:
            return None

    #retorna la cantidad de atributos en la lista antes de encontrar None
    def longitud(self):
        contador = 0
        while self.elemento(contador)!=None:
            contador+=1
        return contador
    
class Nodo:
    def __init__(self,atributo):
        self.__atributo=atributo
        self.__siguiente=None
    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def setAtributo(self,atributo):
        self.__atributo = atributo
    def getAtributo(self):
        return self.__atributo