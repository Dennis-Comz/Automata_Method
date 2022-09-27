class Token:
    lexemaVal = ''
    tipo = 0
    fila = 0
    columna = 0

    CLAVES = 1
    REGISTROS = 2
    IMPRIMIR = 3
    IMPRIMIRLN = 4
    CONTEO = 5
    PROMEDIO = 6
    CONTARSI = 7
    DATOS = 8
    SUMAR = 9
    MAX = 10
    MIN = 11
    EXPORTAR_REPORTE = 12
    CADENA = 13
    NUMERO = 14
    IGUAL = 15
    CORCHETE_IZQUIERDO = 16
    CORCHETE_DERECHO = 17
    COMA = 18
    LLAVE_IZQUIERDA = 19
    LLAVE_DERECHA = 20
    PARENTESIS_IZQUIERDO = 21
    PARENTESIS_DERECHO = 22
    PUNTO_COMA = 23
    COMENTARIO = 24
    DESCONOCIDO = 25
    FIN = 26

    def __init__(self, lexema, tipo, fila, columna):
        self.lexemaVal = lexema
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def getLexema(self):
        return self.lexemaVal

    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna

    def getTipo(self):
        if self.tipo == self.CLAVES:
            return 'CLAVES'
        elif self.tipo == self.REGISTROS:
            return 'REGISTROS'
        elif self.tipo == self.IMPRIMIR:
            return 'IMPRIMIR'
        elif self.tipo == self.IMPRIMIRLN:
            return 'IMPRIMIR_LN'
        elif self.tipo == self.CONTEO:
            return 'CONTEO'
        elif self.tipo == self.PROMEDIO:
            return 'PROMEDIO'
        elif self.tipo == self.CONTARSI:
            return 'CONTAR_SI'
        elif self.tipo == self.DATOS:
            return 'DATOS'
        elif self.tipo == self.SUMAR:
            return 'SUMAR'
        elif self.tipo == self.MAX:
            return 'MAX'
        elif self.tipo == self.MIN:
            return 'MIN'
        elif self.tipo == self.EXPORTAR_REPORTE:
            return 'EXPORTAR_REPORTE'
        elif self.tipo == self.CADENA:
            return 'CADENA'
        elif self.tipo == self.NUMERO:
            return 'NUMERO'
        elif self.tipo == self.IGUAL:
            return 'IGUAL'
        elif self.tipo == self.CORCHETE_IZQUIERDO:
            return 'CORCHETE_IZQUIERDO'
        elif self.tipo == self.CORCHETE_DERECHO:
            return 'CORCHETE_DERECHO'
        elif self.tipo == self.COMA:
            return 'COMA'
        elif self.tipo == self.LLAVE_IZQUIERDA:
            return 'LLAVE_IZQUIERDA'
        elif self.tipo == self.LLAVE_DERECHA:
            return 'LLAVE_DERECHA'
        elif self.tipo == self.PARENTESIS_IZQUIERDO:
            return 'PARENTESIS_IZQUIERDO'
        elif self.tipo == self.PARENTESIS_DERECHO:
            return 'PARENTESIS_DERECHO'
        elif self.tipo == self.PUNTO_COMA:
            return 'PUNTO_COMA'
        elif self.tipo == self.COMENTARIO:
            return 'COMENTARIO'
        elif self.tipo == self.DESCONOCIDO:
            return 'DESCONOCIDO'
        elif self.tipo == self.FIN:
            return 'FIN'

    def findTipo(self, tipo):
        if tipo == self.CLAVES:
            return 'CLAVES'
        elif tipo == self.REGISTROS:
            return 'REGISTROS'
        elif tipo == self.IMPRIMIR:
            return 'IMPRIMIR'
        elif tipo == self.IMPRIMIRLN:
            return 'IMPRIMIR_LN'
        elif tipo == self.CONTEO:
            return 'CONTEO'
        elif tipo == self.PROMEDIO:
            return 'PROMEDIO'
        elif tipo == self.CONTARSI:
            return 'CONTAR_SI'
        elif tipo == self.DATOS:
            return 'DATOS'
        elif tipo == self.SUMAR:
            return 'SUMAR'
        elif tipo == self.MAX:
            return 'MAX'
        elif tipo == self.MIN:
            return 'MIN'
        elif tipo == self.EXPORTAR_REPORTE:
            return 'EXPORTAR_REPORTE'
        elif tipo == self.CADENA:
            return 'CADENA'
        elif tipo == self.NUMERO:
            return 'NUMERO'
        elif tipo == self.IGUAL:
            return 'IGUAL'
        elif tipo == self.CORCHETE_IZQUIERDO:
            return 'CORCHETE_IZQUIERDO'
        elif tipo == self.CORCHETE_DERECHO:
            return 'CORCHETE_DERECHO'
        elif tipo == self.COMA:
            return 'COMA'
        elif tipo == self.LLAVE_IZQUIERDA:
            return 'LLAVE_IZQUIERDA'
        elif tipo == self.LLAVE_DERECHA:
            return 'LLAVE_DERECHA'
        elif tipo == self.PARENTESIS_IZQUIERDO:
            return 'PARENTESIS_IZQUIERDO'
        elif tipo == self.PARENTESIS_DERECHO:
            return 'PARENTESIS_DERECHO'
        elif tipo == self.PUNTO_COMA:
            return 'PUNTO_COMA'
        elif tipo == self.COMENTARIO:
            return 'COMENTARIO'
        elif tipo == self.DESCONOCIDO:
            return 'DESCONOCIDO'
        elif tipo == self.FIN:
            return 'FIN'