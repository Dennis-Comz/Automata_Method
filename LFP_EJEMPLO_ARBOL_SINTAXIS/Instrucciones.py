from Expresiones import *
from graphviz import Graph

class InstruccionEpsilon() :
    def __init__(self) :
        pass
    
    def ejecutar(self, entorno):
        pass

    def getNodos(self):
        global dot

        #padre
        idnodo = str(inc())
        dot.node(idnodo, "Epsilon")

        return idnodo

class InstruccionDeclaracion() :
    def __init__(self, id, expresion) :
        self.id = id
        self.expresion = expresion
    def ejecutar(self, entorno):
        valor = self.expresion.getValor(entorno)
        entorno.update({self.id: valor})
        print("DECLARANDO VARIABLE... ", self.id)
        #return entorno.get(self.id)

    def getNodos(self):
        global dot

        #padre
        idnodo = str(inc())
        dot.node(idnodo, "INS_DECLARACION")

        #let
        idlet = str(inc())
        dot.node(idlet, "let")

        #identificador
        idid = str(inc())
        dot.node(idid, "identificador")

        ididlex = str(inc())
        dot.node(ididlex, self.id)

        dot.edge(idid, ididlex)

        #igual
        idigual = str(inc())
        dot.node(idigual, "=")

        #expresion
        idexp = self.expresion.getNodos()

        #puntocoma
        idpuntocoma = str(inc())
        dot.node(idpuntocoma, ";")

        #enlaces
        dot.edge(idnodo, idlet)
        dot.edge(idnodo, idid)
        dot.edge(idnodo, idigual)
        dot.edge(idnodo, idexp)
        dot.edge(idnodo, idpuntocoma)

        return idnodo

class IntruccionImprimir() :
    def __init__(self, expresion) :
        self.expresion = expresion

    def ejecutar(self, entorno):
        valor = self.expresion.getValor(entorno)
        print(valor)

    def getNodos(self):
        global dot
        idnodo = str(inc())
        dot.node(idnodo, "INS_IMPRIMIR")

        idconsole = str(inc())
        dot.node(idconsole, "console")

        idpunto = str(inc())
        dot.node(idpunto, "punto")

        idlog = str(inc())
        dot.node(idlog, "log")

        idpara = str(inc())
        dot.node(idpara, "(")

        hijo = self.expresion.getNodos()

        idparc = str(inc())
        dot.node(idparc, ")")

        idpuntocoma = str(inc())
        dot.node(idpuntocoma, ";")        

        dot.edge(idnodo, idconsole)
        dot.edge(idnodo, idpunto)
        dot.edge(idnodo, idlog)
        dot.edge(idnodo, idpara)
        dot.edge(idnodo, hijo)
        dot.edge(idnodo, idparc)
        dot.edge(idnodo, idpuntocoma)
        return idnodo

class IntruccionInstruccion() :
    def __init__(self, instruccion) :
        self.instruccion = instruccion

    def ejecutar(self, entorno):
        self.instruccion.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo = str(inc())
        dot.node(idnodo, "INSTRUCCION")

        hijo = self.instruccion.getNodos()

        dot.edge(idnodo, hijo)
        return idnodo

class IntruccionListaInstrucciones2() :
    def __init__(self, instruccion, lista) :
        self.instruccion = instruccion
        self.lista = lista

    def ejecutar(self, entorno):
        if self.instruccion:
            self.instruccion.ejecutar(entorno)
            if self.lista:
                self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo = str(inc())
        dot.node(idnodo, "LISTAINSTRUCCIONES2")
        if self.instruccion:
            hijo = self.instruccion.getNodos()
            dot.edge(idnodo, hijo)
            if self.lista:
                hijo2 = self.lista.getNodos()
                dot.edge(idnodo, hijo2)
        return idnodo

class IntruccionListaInstrucciones() :
    def __init__(self, instruccion, lista) :
        self.instruccion = instruccion
        self.lista = lista

    def ejecutar(self, entorno):
        if self.instruccion:
            self.instruccion.ejecutar(entorno)
            if self.lista:
                self.lista.ejecutar(entorno)
    
    def getNodos(self):
        global dot
        idnodo = str(inc())
        dot.node(idnodo, "LISTAINSTRUCCIONES")
        if self.instruccion:
            hijo = self.instruccion.getNodos()
            dot.edge(idnodo, hijo)
            if self.lista:
                hijo2 = self.lista.getNodos()
                dot.edge(idnodo, hijo2)
        return idnodo

class IntruccionInicio() :
    def __init__(self,lista) :
        self.lista = lista

    def ejecutar(self, entorno):
        self.lista.ejecutar(entorno)

    def getNodos(self):
        global dot
        idnodo = str(inc())
        dot.node(idnodo, "INICIO")
        hijo = self.lista.getNodos()
        dot.edge(idnodo, hijo)
        dot.view()
        return idnodo