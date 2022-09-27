from AnalizadorLexico import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico

def leerArchivo(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

def escribirArchivo(ruta, contenido):
    archivo = open(ruta, 'w')
    archivo.write(contenido)
    archivo.close()

if __name__ == '__main__':
    cadena = leerArchivo('prueba.lfp')
    scanner = AnalizadorLexico()
    listaTokens = scanner.analizar(cadena)
    #scanner.impTokens()
    #scanner.impErrores()
    parser = AnalizadorSintactico()
    parser.analizar(listaTokens)
    #parser.impErrores()