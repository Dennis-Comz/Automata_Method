from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget
from Token import Token
from Funciones import Funciones
from graphviz import Graph

class Sintactico:
    preanalisis = Token.DESCONOCIDO
    posicion = 0
    lista = []
    errorSintactico = False

    def __init__(self, lista, editor):
        self.errorSintactico = False
        self.lista_errores = []
        self.editor = editor
        self.lista = lista
        self.posicion, self.contador_claves, self.contador_rg = 0,0,0
        self.preanalisis = self.lista[self.posicion].tipo
        self.funciones = Funciones(self.lista)
        self.ingreso = False
        self.arbol_basics()
        self.Inicio()

    def arbol_basics(self):
        self.i = 0
        self.dot= Graph('arbol_derivacion', 'png')
        self.dot.format = 'png'
        self.dot.attr(splines='false')
        self.dot.node_attr.update(shape='circle')
        self.dot.edge_attr.update(color = 'blue')

        self.dot.node('0', 'Lista')
        self.dot.node('1', 'Inicio')

        self.inc()
        self.dot.edge('0', '1')

    def inc(self):
        self.i += 1
        return self.i 

    def Match(self, tipo):
        if self.preanalisis != tipo and self.errorSintactico != True:
            error = ''
            error = "Lexema: " + self.lista[self.posicion].getLexema() + " --> Error Sintactico Se Esperaba --> " + self.lista[self.posicion].findTipo(tipo)
            print(error)
            self.lista_errores.append(self.lista[self.posicion].getTipo())
            self.lista_errores.append(self.lista[self.posicion].getLexema())
            self.lista_errores.append(self.lista[self.posicion].getFila())
            self.lista_errores.append(self.lista[self.posicion].getColumna())
            self.lista_errores.append(self.lista[self.posicion].findTipo(tipo))
            self.editor.setPlainText(error)
            self.errorSintactico = True
        
        if self.preanalisis != Token.FIN and self.errorSintactico == False:
            self.posicion += 1
            self.preanalisis = self.lista[self.posicion].tipo
        elif self.preanalisis != Token.FIN and self.errorSintactico == True:
            self.posicion += 1
            self.preanalisis = self.lista[self.posicion].tipo           

        if self.preanalisis == Token.FIN:
            if self.errorSintactico == False:
                self.funciones.setInterfaz(self.editor)


    def Inicio(self):
        if Token.CLAVES == self.preanalisis:
            self.Claves()
            self.Inicio()
        elif Token.REGISTROS == self.preanalisis:
            self.Registros()
            self.Inicio()
        elif Token.COMENTARIO == self.preanalisis:
            self.Comentarios()
            self.Inicio()
        elif Token.IMPRIMIR == self.preanalisis:
            self.Imprimir()
            self.Inicio()
        elif Token.IMPRIMIRLN == self.preanalisis:
            self.Imprimirln()
            self.Inicio()
        elif Token.CONTEO == self.preanalisis:
            self.Conteo()
            self.Inicio()
        elif Token.PROMEDIO == self.preanalisis:
            self.Promedio()
            self.Inicio()
        elif Token.CONTARSI == self.preanalisis:
            self.Contar_Si()
            self.Inicio()
        elif Token.DATOS == self.preanalisis:
            self.Datos()
            self.Inicio()
        elif Token.SUMAR == self.preanalisis:
            self.Sumar()
            self.Inicio()
        elif Token.MAX == self.preanalisis:
            self.Max()
            self.Inicio()
        elif Token.MIN == self.preanalisis:
            self.Min()
            self.Inicio()
        elif Token.EXPORTAR_REPORTE == self.preanalisis:
            self.Exportar_Reporte()
            self.Inicio()       
        elif Token.FIN == self.preanalisis:
            self.Match(Token.FIN) 
    
    def Claves(self):
        self.Match(Token.CLAVES)
        tkclaves = str(self.inc())
        self.dot.node(tkclaves, "tk_claves")

        idclaves = str(self.inc())
        self.dot.node(idclaves, "Claves")

        self.Match(Token.IGUAL)
        idigual = str(self.inc())
        self.dot.node(idigual, "=")

        self.Match(Token.CORCHETE_IZQUIERDO)
        idci = str(self.inc())
        self.dot.node(idci, "[")

        idbc = str(self.inc())
        self.dot.node(idbc, "Bloque Claves")
        self.Bloque_Claves(idbc)

        self.Match(Token.CORCHETE_DERECHO)
        idcd = str(self.inc())
        self.dot.node(idcd, "]")

        self.dot.edge('1', tkclaves)
        self.dot.edge(tkclaves, idclaves)
        self.dot.edge(tkclaves, idigual)
        self.dot.edge(tkclaves, idci)
        self.dot.edge(tkclaves, idbc)
        self.dot.edge(tkclaves, idcd)
    
    def Registros(self):
        self.Match(Token.REGISTROS)
        tkrg = str(self.inc())
        self.dot.node(tkrg, "tk_registros")

        idregistros = str(self.inc())
        self.dot.node(idregistros, "Registros")

        self.Match(Token.IGUAL)
        idigual = str(self.inc())
        self.dot.node(idigual, "=")

        self.Match(Token.CORCHETE_IZQUIERDO)
        idci = str(self.inc())
        self.dot.node(idci, "[")

        idrg = str(self.inc())
        self.dot.node(idrg, "Bloque Registros")
        self.Bloque_Registros(idrg)

        self.Match(Token.CORCHETE_DERECHO)
        idcd = str(self.inc())
        self.dot.node(idcd, "]")

        self.dot.edge('1', tkrg)
        self.dot.edge(tkrg, idregistros)
        self.dot.edge(tkrg, idigual)
        self.dot.edge(tkrg, idci)
        self.dot.edge(tkrg, idrg)
        self.dot.edge(tkrg, idcd)

    def Comentarios(self):
        self.Match(Token.COMENTARIO)

        tkcomment = str(self.inc())
        self.dot.node(tkcomment, "tk_comentario")

        idcomment = str(self.inc())
        self.dot.node(idcomment, self.lista[self.posicion-1].getLexema())

        self.dot.edge('1', tkcomment)
        self.dot.edge(tkcomment, idcomment)

    def Imprimir(self):
        tkimp = str(self.inc())
        self.dot.node(tkimp, "tk_imprimir")
        
        self.Match(Token.IMPRIMIR)
        idimp = str(self.inc())
        self.dot.node(idimp, "imprimir")

        self.Match(Token.PARENTESIS_IZQUIERDO)
        idpari = str(self.inc())
        self.dot.node(idpari, "(")

        self.Match(Token.CADENA)
        idcad = str(self.inc())
        self.dot.node(idcad, self.lista[self.posicion-1].getLexema())

        self.Match(Token.PARENTESIS_DERECHO)
        idpard = str(self.inc())
        self.dot.node(idpard, ")")

        self.Match(Token.PUNTO_COMA)
        idpc = str(self.inc())
        self.dot.node(idpc, ";")

        self.dot.edge('1', tkimp)
        self.dot.edge(tkimp, idimp)
        self.dot.edge(tkimp, idpari)
        self.dot.edge(tkimp, idcad)
        self.dot.edge(tkimp, idpard)
        self.dot.edge(tkimp, idpc)

    def Imprimirln(self):
        tkimp = str(self.inc())
        self.dot.node(tkimp, "tk_imprimir_ln")

        self.Match(Token.IMPRIMIRLN)
        idimp = str(self.inc())
        self.dot.node(idimp, "imprimirln")

        self.Match(Token.PARENTESIS_IZQUIERDO)
        idpari = str(self.inc())
        self.dot.node(idpari, "(")

        self.Match(Token.CADENA)
        idcad = str(self.inc())
        self.dot.node(idcad, self.lista[self.posicion-1].getLexema())

        self.Match(Token.PARENTESIS_DERECHO)
        idpard = str(self.inc())
        self.dot.node(idpard, ")")

        self.Match(Token.PUNTO_COMA)
        idpc = str(self.inc())
        self.dot.node(idpc, ";")

        self.dot.edge('1', tkimp)
        self.dot.edge(tkimp, idimp)
        self.dot.edge(tkimp, idpari)
        self.dot.edge(tkimp, idcad)
        self.dot.edge(tkimp, idpard)
        self.dot.edge(tkimp, idpc)

    def Conteo(self):
        tkimp = str(self.inc())
        self.dot.node(tkimp, "tk_conteo")

        self.Match(Token.CONTEO)
        idimp = str(self.inc())
        self.dot.node(idimp, "conteo")

        self.Match(Token.PARENTESIS_IZQUIERDO)
        idpari = str(self.inc())
        self.dot.node(idpari, "(")

        self.Match(Token.PARENTESIS_DERECHO)
        idpard = str(self.inc())
        self.dot.node(idpard, ")")

        self.Match(Token.PUNTO_COMA)
        idpc = str(self.inc())
        self.dot.node(idpc, ";")

        self.dot.edge('1', tkimp)
        self.dot.edge(tkimp, idimp)
        self.dot.edge(tkimp, idpari)
        self.dot.edge(tkimp, idpard)
        self.dot.edge(tkimp, idpc)

    def Promedio(self):
        tkimp = str(self.inc())
        self.dot.node(tkimp, "tk_promedio")

        self.Match(Token.PROMEDIO)
        idimp = str(self.inc())
        self.dot.node(idimp, "promedio")

        self.Match(Token.PARENTESIS_IZQUIERDO)
        idpari = str(self.inc())
        self.dot.node(idpari, "(")

        self.Match(Token.CADENA)
        idcad = str(self.inc())
        self.dot.node(idcad, self.lista[self.posicion-1].getLexema())

        self.Match(Token.PARENTESIS_DERECHO)
        idpard = str(self.inc())
        self.dot.node(idpard, ")")

        self.Match(Token.PUNTO_COMA)
        idpc = str(self.inc())
        self.dot.node(idpc, ";")

        self.dot.edge('1', tkimp)
        self.dot.edge(tkimp, idimp)
        self.dot.edge(tkimp, idpari)
        self.dot.edge(tkimp, idcad)
        self.dot.edge(tkimp, idpard)
        self.dot.edge(tkimp, idpc)

    def Contar_Si(self):
        tkimp = str(self.inc())
        self.dot.node(tkimp, "tk_contar_si")

        self.Match(Token.CONTARSI)
        idimp = str(self.inc())
        self.dot.node(idimp, "contarsi")

        self.Match(Token.PARENTESIS_IZQUIERDO)
        idpari = str(self.inc())
        self.dot.node(idpari, "(")

        self.Match(Token.CADENA)
        idcad = str(self.inc())
        self.dot.node(idcad, self.lista[self.posicion-1].getLexema())

        self.Match(Token.COMA)
        idcoma = str(self.inc())
        self.dot.node(idcoma, ",")

        self.Match(Token.NUMERO)
        idnum = str(self.inc())
        self.dot.node(idnum, self.lista[self.posicion-1].getLexema())

        self.Match(Token.PARENTESIS_DERECHO)
        idpard = str(self.inc())
        self.dot.node(idpard, ")")

        self.Match(Token.PUNTO_COMA)
        idpc = str(self.inc())
        self.dot.node(idpc, ";")

        self.dot.edge('1', tkimp)
        self.dot.edge(tkimp, idimp)
        self.dot.edge(tkimp, idpari)
        self.dot.edge(tkimp, idcad)
        self.dot.edge(tkimp, idcoma)
        self.dot.edge(tkimp, idnum)
        self.dot.edge(tkimp, idpard)
        self.dot.edge(tkimp, idpc)

    def Datos(self):
        tkimp = str(self.inc())
        self.dot.node(tkimp, "tk_datos")

        self.Match(Token.DATOS)
        idimp = str(self.inc())
        self.dot.node(idimp, "datos")

        self.Match(Token.PARENTESIS_IZQUIERDO)
        idpari = str(self.inc())
        self.dot.node(idpari, "(")

        self.Match(Token.PARENTESIS_DERECHO)
        idpard = str(self.inc())
        self.dot.node(idpard, ")")

        self.Match(Token.PUNTO_COMA)
        idpc = str(self.inc())
        self.dot.node(idpc, ";")

        self.dot.edge('1', tkimp)
        self.dot.edge(tkimp, idimp)
        self.dot.edge(tkimp, idpari)
        self.dot.edge(tkimp, idpard)
        self.dot.edge(tkimp, idpc)

    def Sumar(self):
        tkimp = str(self.inc())
        self.dot.node(tkimp, "tk_sumar")

        self.Match(Token.SUMAR)
        idimp = str(self.inc())
        self.dot.node(idimp, "sumar")

        self.Match(Token.PARENTESIS_IZQUIERDO)
        idpari = str(self.inc())
        self.dot.node(idpari, "(")

        self.Match(Token.CADENA)
        idcad = str(self.inc())
        self.dot.node(idcad, self.lista[self.posicion-1].getLexema())

        self.Match(Token.PARENTESIS_DERECHO)
        idpard = str(self.inc())
        self.dot.node(idpard, ")")

        self.Match(Token.PUNTO_COMA)
        idpc = str(self.inc())
        self.dot.node(idpc, ";")

        self.dot.edge('1', tkimp)
        self.dot.edge(tkimp, idimp)
        self.dot.edge(tkimp, idpari)
        self.dot.edge(tkimp, idcad)
        self.dot.edge(tkimp, idpard)
        self.dot.edge(tkimp, idpc)

    def Max(self):
        tkimp = str(self.inc())
        self.dot.node(tkimp, "tk_max")

        self.Match(Token.MAX)
        idimp = str(self.inc())
        self.dot.node(idimp, "max")

        self.Match(Token.PARENTESIS_IZQUIERDO)
        idpari = str(self.inc())
        self.dot.node(idpari, "(")

        self.Match(Token.CADENA)
        idcad = str(self.inc())
        self.dot.node(idcad, self.lista[self.posicion-1].getLexema())

        self.Match(Token.PARENTESIS_DERECHO)
        idpard = str(self.inc())
        self.dot.node(idpard, ")")

        self.Match(Token.PUNTO_COMA)
        idpc = str(self.inc())
        self.dot.node(idpc, ";")

        self.dot.edge('1', tkimp)
        self.dot.edge(tkimp, idimp)
        self.dot.edge(tkimp, idpari)
        self.dot.edge(tkimp, idcad)
        self.dot.edge(tkimp, idpard)
        self.dot.edge(tkimp, idpc)

    def Min(self):
        tkimp = str(self.inc())
        self.dot.node(tkimp, "tk_min")

        self.Match(Token.MIN)
        idimp = str(self.inc())
        self.dot.node(idimp, "min")

        self.Match(Token.PARENTESIS_IZQUIERDO)
        idpari = str(self.inc())
        self.dot.node(idpari, "(")

        self.Match(Token.CADENA)
        idcad = str(self.inc())
        self.dot.node(idcad, self.lista[self.posicion-1].getLexema())

        self.Match(Token.PARENTESIS_DERECHO)
        idpard = str(self.inc())
        self.dot.node(idpard, ")")

        self.Match(Token.PUNTO_COMA)
        idpc = str(self.inc())
        self.dot.node(idpc, ";")

        self.dot.edge('1', tkimp)
        self.dot.edge(tkimp, idimp)
        self.dot.edge(tkimp, idpari)
        self.dot.edge(tkimp, idcad)
        self.dot.edge(tkimp, idpard)
        self.dot.edge(tkimp, idpc)
    
    def Exportar_Reporte(self):
        tkimp = str(self.inc())
        self.dot.node(tkimp, "tk_exportar_reporte")

        self.Match(Token.EXPORTAR_REPORTE)
        idimp = str(self.inc())
        self.dot.node(idimp, "exportarReporte")

        self.Match(Token.PARENTESIS_IZQUIERDO)
        idpari = str(self.inc())
        self.dot.node(idpari, "(")

        self.Match(Token.CADENA)
        idcad = str(self.inc())
        self.dot.node(idcad, self.lista[self.posicion-1].getLexema())

        self.Match(Token.PARENTESIS_DERECHO)
        idpard = str(self.inc())
        self.dot.node(idpard, ")")

        self.Match(Token.PUNTO_COMA)
        idpc = str(self.inc())
        self.dot.node(idpc, ";")

        self.dot.edge('1', tkimp)
        self.dot.edge(tkimp, idimp)
        self.dot.edge(tkimp, idpari)
        self.dot.edge(tkimp, idcad)
        self.dot.edge(tkimp, idpard)
        self.dot.edge(tkimp, idpc)

    def Bloque_Claves(self, idbc):
        if Token.CADENA == self.preanalisis:

            self.Match(Token.CADENA)
            cad = str(self.inc())
            self.dot.node(cad, self.lista[self.posicion-1].getLexema())
            self.dot.edge(idbc, cad)

            self.contador_claves += 1
            self.Bloque_Coma(idbc)
        else:
            self.Match(Token.CADENA)
            cad = str(self.inc())
            self.dot.node(cad, self.lista[self.posicion-1].getLexema())
            self.dot.edge(idbc, cad)

            self.contador_claves += 1
    
    def Bloque_Coma(self, idbc):
        if Token.COMA == self.preanalisis:
            self.Match(Token.COMA)
            coma = str(self.inc())
            self.dot.node(coma, self.lista[self.posicion-1].getLexema())
            self.dot.edge(idbc, coma)

            self.Match(Token.CADENA)
            cad = str(self.inc())
            self.dot.node(cad, self.lista[self.posicion-1].getLexema())
            self.dot.edge(idbc, cad)

            self.contador_claves += 1
            self.Bloque_Coma(idbc)
    
    def Bloque_Registros(self, idrg):
        if Token.LLAVE_IZQUIERDA == self.preanalisis:
            idregis = str(self.inc())
            self.dot.node(idregis, "Registro")
            self.dot.edge(idrg, idregis)

            self.Cuerpo_Registros(idregis)
            self.Bloque_Registros(idrg)

    def Cuerpo_Registros(self, idregis):
        self.contador_rg = 0
        self.Match(Token.LLAVE_IZQUIERDA)
        idllave = str(self.inc())
        self.dot.node(idllave, "{")
        self.dot.edge(idregis, idllave)

        self.Cuerpo_valor(idregis)

        self.Match(Token.LLAVE_DERECHA)
        idllaved = str(self.inc())
        self.dot.node(idllaved, "}")
        self.dot.edge(idregis, idllaved)
        
        if self.contador_claves != self.contador_rg:
            self.errorSintactico = True
    
    def Cuerpo_valor(self, idregis):
        if Token.NUMERO == self.preanalisis:
            self.Match(Token.NUMERO)
            idnum = str(self.inc())
            self.dot.node(idnum, self.lista[self.posicion - 1].getLexema())
            self.dot.edge(idregis, idnum)

            self.contador_rg += 1
            self.Valorc_coma(idregis)
        elif Token.CADENA == self.preanalisis:
            self.Match(Token.CADENA)
            idcad = str(self.inc())
            self.dot.node(idcad, self.lista[self.posicion - 1].getLexema())
            self.dot.edge(idregis, idcad)

            self.contador_rg += 1
            self.Valorc_coma()

    def Valorc_coma(self, idregis):
        if Token.COMA == self.preanalisis:
            self.Match(Token.COMA)
            coma = str(self.inc())
            self.dot.node(coma, self.lista[self.posicion-1].getLexema())
            self.dot.edge(idregis, coma)

            if Token.NUMERO == self.preanalisis:
                self.Match(Token.NUMERO)
                idnum = str(self.inc())
                self.dot.node(idnum, self.lista[self.posicion - 1].getLexema())
                self.dot.edge(idregis, idnum)
                self.contador_rg += 1
                self.Valorc_coma(idregis)
            elif Token.CADENA == self.preanalisis:
                self.Match(Token.CADENA)
                idcad = str(self.inc())
                self.dot.node(idcad, self.lista[self.posicion - 1].getLexema())
                self.dot.edge(idregis, idcad)
                self.contador_rg += 1
                self.Valorc_coma(idregis)
            else:
                self.errorSintactico = True

    def get_errores(self):
        return self.lista_errores

    def generar_arbol(self):
        mainw = QMainWindow()
        if self.errorSintactico == True:
            msg = QMessageBox.about(mainw, "Error", "Se detecto un error sintacto, compruebe la estructura del archivo")
            mainw.show()
        else:
            self.dot.view()
