from Token import Token
from Error import Error
import re
class AnalizadorLexico:
    
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []
    
    def analizar(self, cadena):  #inserta solamente al final
        #inicializar listas nuevamente
        self.listaTokens = []
        self.listaErrores = []

        #inicializar atributos del analisis
        linea = 1
        columna = 1
        centinela = '$'
        buffer = ''
        estado = 0

        #agregar caracter final a la cadena (centinela)
        cadena += centinela

        #recorrer caracter por caracter
        i = 0
        while i < len(cadena):
            c = cadena[i]
            if estado == 0:
                if c == '=':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'igual', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '(':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'para', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ')':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'parc', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ';':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'puntocoma', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '.':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'punto', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '_':
                    buffer += c
                    columna += 1
                    estado = 5
                elif c == '"': #si encuentra comillas dobles las agrega al buffer y nos vamos al estado 1
                    buffer += c
                    columna += 1
                    estado = 1
                elif re.search('\d', c): #si encuentra un digito lo agrega al buffer y nos vamos al estado 2
                    buffer += c
                    columna += 1
                    estado = 2
                elif re.search('[a-zA-Z]', c): #si encuentra una letra la agrega al buffer y nos vamos al estado 3
                    buffer += c
                    columna += 1
                    estado = 3
                elif c == ' ':#si encuentra un espacio solamente sumamos 1 al atributo columna
                    columna += 1
                elif c == '\n':#si encuentra un salto de linea solamente sumamos 1 al atributo linea
                    linea += 1
                    columna = 1
                elif c == '\t': #si encuentra un tabulador solamente sumamos 1 al atributo columna
                    columna += 1
                elif c == '\r': #si encuentra un retorno al carro no hacemos nada ya que a veces está combinado con \n
                    pass
                elif c == '$': # si encuentra un numeral se finalizó el analisis lexico
                    self.listaTokens.append(Token('$', 'EOF', linea, columna))
                    print('Se aceptó la cadena!')
                    break
                else: # si encuentra cualquier otra cosa se reconoce como error y se agrega a la lista de errores
                    buffer += c
                    print('el buffer es', buffer)
                    self.listaErrores.append(Error('Caracter ' + buffer + ' no reconocido en el lenguaje.', linea, columna))
                    buffer = ''
                    columna += 1
            elif estado == 1:
                if c == '"':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'cadena', linea, columna))
                    buffer = ''
                    columna += 1
                    estado = 0
                elif c == '\n':
                    buffer += c
                    linea += 1
                    columna = 1
                elif c == '\r':
                    buffer += c
                else:
                    buffer += c
                    columna += 1
            elif estado == 2:
                if re.search('\d', c):
                    buffer += c
                    columna += 1
                elif  c == '.': #si encuentra un punto lo agrega al buffer y nos vamos al estado 4
                    buffer += c
                    columna += 1
                    estado = 4
                else:
                    self.listaTokens.append(Token(buffer, 'entero', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0
            elif estado == 3:
                if re.search('[a-zA-Z]', c):
                    buffer += c
                    columna += 1
                elif c == '_':
                    buffer += c
                    columna += 1
                    estado = 5
                elif re.search('\d', c):
                    buffer += c
                    columna += 1
                    estado = 5
                else:
                    if buffer == 'let':
                        self.listaTokens.append(Token(buffer, 'let', linea, columna))
                    elif buffer == 'console':
                        self.listaTokens.append(Token(buffer, 'console', linea, columna))
                    elif buffer == 'log':
                        self.listaTokens.append(Token(buffer, 'log', linea, columna))
                    else:
                        self.listaTokens.append(Token(buffer, 'identificador', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0
            elif estado == 4:
                if re.search('\d', c):
                    buffer += c
                else:
                    self.listaTokens.append(Token(buffer, 'decimal', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0
            elif estado == 5:
                if re.search('[a-zA-Z]', c):
                    buffer += c
                    columna += 1
                elif c == '_':
                    buffer += c
                    columna += 1
                elif re.search('\d', c):
                    buffer += c
                    columna += 1
                else:
                    self.listaTokens.append(Token(buffer, 'identificador', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0
            i += 1
        return self.listaTokens
                    

    def impTokens(self):
        for i in self.listaTokens:
            i.imprimirData()

    def impErrores(self):
        if len(self.listaErrores)==0:
            print('No hay errores')
        else:
            for i in self.listaErrores:
                i.imprimirData()