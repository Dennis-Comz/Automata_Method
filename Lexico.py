from Token import Token
from Sintactico import Sintactico

lexema = ''
tipo = ''
tokens = []
estado = 0
fila = 1
columna = 1
generar = False

tipos = Token("lexema", -1, -1, -1)

class Analizador:
    def reader(self, entrada):
        self.estado = 0
        self.lexema = ''
        self.tokens = []
        self.errores = []
        self.fila = 1
        self.columna = 1
        self.tipo = ''
        self.generar = True

        ultimas = ''
        primeras_validas = False
        ultimas_validas = False

        entrada += '$'
        actual = ''
        longitud = len(entrada)
        i = 0
        while i < longitud:
            actual = entrada[i]

            if self.estado == 0:
                if actual.isalpha():
                    self.estado = 1
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                elif actual.isdigit():
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                elif actual == '"':
                    self.estado = 4
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                elif actual == '#':
                    self.estado = 5
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                elif actual == "'":
                    self.estado = 6
                    self.columna += 1
                    self.lexema += actual
                    primeras = True
                    i += 1
                elif actual == '=':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.IGUAL)
                    i += 1
                elif actual == '[':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.CORCHETE_IZQUIERDO)
                    i += 1
                elif actual == ']':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.CORCHETE_DERECHO)
                    i += 1
                elif actual == ',':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.COMA)
                    i += 1
                elif actual == '{':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.LLAVE_IZQUIERDA)
                    i += 1
                elif actual == '}':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.LLAVE_DERECHA)
                    i += 1
                elif actual == '(':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.PARENTESIS_IZQUIERDO)
                    i += 1
                elif actual == ')':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.PARENTESIS_DERECHO)
                    i += 1
                elif actual == ';':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.PUNTO_COMA)
                    i += 1
                elif actual == ' ':
                    self.columna += 1
                    self.estado = 0
                    i += 1
                elif actual == '\n':
                    self.fila += 1
                    self.estado = 0
                    self.columna = 1
                    i += 1
                elif actual  == '\r':
                    self.estado = 0
                    i += 1
                elif actual == '\t':
                    self.columna += 8
                    self.estado = 0
                    i += 1
                elif actual == '$' and i == longitud - 1:
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.FIN)
                    self.sintactico = Sintactico(self.tokens, self.editor)
                    i += 1
                else:
                    self.lexema += actual
                    self.agregarError(tipos.DESCONOCIDO)
                    self.columna += 1
                    self.generar = False
                    i += 1

            elif self.estado == 1:
                if actual.isalpha():
                    self.estado = 1
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                else:
                    if self.palabra_reservada(self.lexema):
                        self.agregarToken(self.tipo)
                    elif self.instrucciones(self.lexema):
                        self.agregarToken(self.tipo)
                    else:
                        self.agregarError(tipos.DESCONOCIDO)
                        self.generar = False
            
            elif self.estado == 2:
                if actual.isdigit():
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                elif actual == '.':
                    self.estado = 2
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                else:
                    self.agregarToken(tipos.NUMERO)
            
            elif self.estado == 4:
                if actual != '"':
                    self.estado = 4
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                elif actual == '"':
                    self.columna += 1
                    self.lexema += actual
                    self.agregarToken(tipos.CADENA)
                    i += 1

            elif self.estado == 5:
                if actual != '\n':
                    self.estado = 5
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                else:
                    self.agregarToken(tipos.COMENTARIO)
            
            elif self.estado == 6:
                if actual == "'":
                    self.estado = 6
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                elif self.lexema == "'''":
                    self.estado = 7
                    primeras_validas = True
                else:
                    primeras_validas = False
                    self.estado = 7
            
            elif self.estado == 7:
                if actual == '\n':
                    self.columna = 1
                    self.fila += 1
                    i += 1
                elif actual == ' ':
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                elif actual == "'":
                    self.estado = 8
                    ultimas += actual
                    self.lexema += actual
                    self.columna += 1
                    i += 1
                else:
                    if actual == '$' and ultimas == '':
                        self.agregarError(tipos.DESCONOCIDO)
                        self.generar = False
                    else:
                        self.estado = 7
                        self.columna += 1
                        self.lexema += actual
                        i += 1


            elif self.estado == 8:
                if actual == "'":
                    self.estado = 8
                    ultimas += actual
                    self.columna += 1
                    self.lexema += actual
                    i += 1
                elif ultimas == "'''" and ultimas_validas == False:
                    ultimas_validas = True
                elif primeras_validas == True and ultimas_validas == True:
                    self.agregarToken(tipos.COMENTARIO)
                else:
                    self.agregarError(tipos.DESCONOCIDO)
                    self.generar = False


    def agregarToken(self, tipo):
        self.tokens.append(Token(self.lexema, tipo, self.fila, self.columna))
        self.lexema = ''
        self.estado = 0
    
    def agregarError(self, tipo):
        self.errores.append(Token(self.lexema, tipo, self.fila, self.columna))
        self.lexema = ''
        self.estado = 0

    def palabra_reservada(self, entrada = ''):
        entrada = entrada.upper()
        valor = False
        palabras = ['CLAVES', 'REGISTROS']
        if entrada in palabras:
            valor = True
        
        if valor == True:
            if entrada == 'CLAVES':
                self.tipo = tipos.CLAVES
            elif entrada == 'REGISTROS':
                self.tipo = tipos.REGISTROS

        return valor

    def instrucciones(self, entrada = ''):
        entrada = entrada.upper()
        valor = False
        instrucciones = ['IMPRIMIR', 'IMPRIMIRLN', 'CONTEO', 'PROMEDIO', 'CONTARSI', 'DATOS', 'SUMAR', 'MAX', 'MIN', 'EXPORTARREPORTE']
        if entrada in instrucciones:
            valor = True
        
        if valor == True:
            if entrada == 'IMPRIMIR':
                self.tipo = tipos.IMPRIMIR
            elif entrada == 'IMPRIMIRLN':
                self.tipo = tipos.IMPRIMIRLN
            elif entrada == 'CONTEO':
                self.tipo = tipos.CONTEO
            elif entrada == 'PROMEDIO':
                self.tipo = tipos.PROMEDIO
            elif entrada == 'CONTARSI':
                self.tipo = tipos.CONTARSI
            elif entrada == 'DATOS':
                self.tipo = tipos.DATOS
            elif entrada == 'SUMAR':
                self.tipo = tipos.SUMAR
            elif entrada == 'MAX':
                self.tipo = tipos.MAX
            elif entrada == 'MIN':
                self.tipo = tipos.MIN
            elif entrada == 'EXPORTARREPORTE':
                self.tipo = tipos.EXPORTAR_REPORTE

        return valor

    def can_generate(self):
        if self.generar == True:
            return True
        else:
            return False

    def getTokens(self):
        return self.tokens
    
    def getErrores(self):
        return self.errores
    
    def getErroresSint(self):
        return self.sintactico.get_errores()
    
    def generar_arbol(self):
        self.sintactico.generar_arbol()
        
    def imprimir(self):
        print("=== LECTURA DE TOKENS VALIDOS ===")
        for i in self.tokens:
            if i.tipo != tipos.DESCONOCIDO:
                print('Lexema: ' + i.getLexema() + "; Fila: " + str(i.getFila()) + '; Columna: ' + str(i.getColumna()) +  '; Tipo: ' + i.getTipo())
        print("=== FIN DE LECTURA DE TOKENS ===\n")
        print("=== LECTURA DE TOKENS CON ERROR ===")
        for i in self.tokens:
            if i.tipo == tipos.DESCONOCIDO:
                print('Lexema: ' +  i.getLexema() + "; Fila: " + str(i.getFila()) + '; Columna: ' + str(i.getColumna()) +  '; Tipo: ' + i.getTipo())

        print("=== FIN DE LECTURA DE TOKENS CON ERROR ===")

    def setTextEditor(self, editor):
        self.editor = editor