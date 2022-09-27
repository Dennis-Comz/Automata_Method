from Token import Token
from Error import Error
from Expresiones import *
from Instrucciones import *

class AnalizadorSintactico:
    
    def __init__(self):
        self.listaErrores = []
        self.listaTokens = []
        self.i = 0

    def valor(self):
        if self.listaTokens[self.i].tipo == 'cadena':
            lexema = self.listaTokens[self.i].lexema
            expresion = ExpresionLiteral('cadena', lexema)
            self.i += 1
            return expresion
        elif self.listaTokens[self.i].tipo == 'entero':
            lexema = self.listaTokens[self.i].lexema
            expresion = ExpresionLiteral('entero', lexema)
            self.i += 1
            return expresion
        elif self.listaTokens[self.i].tipo == 'decimal':
            lexema = self.listaTokens[self.i].lexema
            expresion = ExpresionLiteral('decimal', lexema)
            self.i += 1
            return expresion
        elif self.listaTokens[self.i].tipo == 'identificador':
            lexema = self.listaTokens[self.i].lexema
            expresion = ExpresionIdentificador(lexema)
            self.i += 1
            return expresion
    
    def ins_imprimir(self):
        if self.listaTokens[self.i].tipo == 'console':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'punto':
                self.i += 1
                if self.listaTokens[self.i].tipo == 'log':
                    self.i += 1
                    if self.listaTokens[self.i].tipo == 'para':
                        self.i += 1
                        expresion = self.valor()
                        if self.listaTokens[self.i].tipo == 'parc':
                            self.i += 1
                            if self.listaTokens[self.i].tipo == 'puntocoma':
                                self.i += 1
                                return IntruccionImprimir(expresion)

    def ins_declaracion(self):
        if self.listaTokens[self.i].tipo == 'let':
            self.i += 1
            if self.listaTokens[self.i].tipo == 'identificador':
                lexema = self.listaTokens[self.i].lexema
                self.i += 1
                if self.listaTokens[self.i].tipo == 'igual':
                    self.i += 1
                    expresion = self.valor()
                    if self.listaTokens[self.i].tipo == 'puntocoma':
                        self.i += 1
                        return InstruccionDeclaracion(lexema, expresion)


    def instruccion(self):
        if self.listaTokens[self.i].tipo == 'let':
            ins = self.ins_declaracion()
            return IntruccionInstruccion(ins)
        elif self.listaTokens[self.i].tipo == 'console':
            ins = self.ins_imprimir()
            return IntruccionInstruccion(ins)

    def epsilon(self):
        return InstruccionEpsilon()

    def lista_instrucciones2(self):
        if self.listaTokens[self.i].tipo == 'EOF':
            print('Analisis sintactico exitoso')
            print('RETORNANDO EPSILON')
            ins = self.epsilon()
            return IntruccionListaInstrucciones2(ins, [])
        else:
            ins = self.instruccion()
            lista = self.lista_instrucciones2()
            return IntruccionListaInstrucciones2(ins, lista)

    def lista_instrucciones(self):
        ins = self.instruccion()
        lista = self.lista_instrucciones2()
        return IntruccionListaInstrucciones(ins, lista)

    def inicio(self):
        lista = self.lista_instrucciones()
        return IntruccionInicio(lista)

    def analizar(self, listaTokens):
        print()
        self.i = 0
        self.listaTokens = listaTokens
        #self.inicio()
        arbolIns = self.inicio()
        print('')
        print('')
        arbolIns.ejecutar({})
        arbolIns.getNodos()
        print('')
        print('')
        print()

    def impErrores(self):
        if len(self.listaErrores)==0:
            print('No hay errores')
        else:
            for i in self.listaErrores:
                i.imprimirData()