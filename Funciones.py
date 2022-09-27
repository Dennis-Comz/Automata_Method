from prettytable import PrettyTable
from Reportes import Reporte_Funcion

class Funciones:
    def __init__(self, tokens):
        self.tokens = tokens
        self.reporte = Reporte_Funcion()
    
    def setInterfaz(self, interfaz):
        self.interfaz = interfaz
        self.mostrar()

    def mostrar(self):
        self.texto = ''
        for i in range(len(self.tokens)):
            if self.tokens[i].getTipo() == 'IMPRIMIR':
                self.imprimir(i)
            elif self.tokens[i].getTipo() == 'IMPRIMIR_LN':
                self.imprimir_ln(i)
            elif self.tokens[i].getTipo() == 'CONTEO':
                self.conteo()
            elif self.tokens[i].getTipo() == 'EXPORTAR_REPORTE':
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "CADENA":
                        final= ''
                        cadena = self.tokens[j].getLexema()
                        for v in cadena:
                            if v != "\"":
                                final += v
                    elif j > i and self.tokens[j].getTipo() == "PUNTO_COMA":
                        break
                self.exportar_reporte(final)
            elif self.tokens[i].getTipo() == 'PROMEDIO':
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "CADENA":
                        cadena = self.tokens[j].getLexema()
                    elif j > i and self.tokens[j].getTipo() == "PUNTO_COMA":
                        break
                self.promedio(cadena)
            elif self.tokens[i].getTipo() == 'SUMAR':
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "CADENA":
                        cadena = self.tokens[j].getLexema()
                    elif j > i and self.tokens[j].getTipo() == "PUNTO_COMA":
                        break
                self.sumar(cadena)
            elif self.tokens[i].getTipo() == 'CONTAR_SI':
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "CADENA":
                        cadena = self.tokens[j].getLexema()
                    elif j > i and self.tokens[j].getTipo() == "NUMERO":
                        numero = self.tokens[j].getLexema()
                    elif j > i and self.tokens[j].getTipo() == "PUNTO_COMA":
                        break
                self.contar_si(cadena, numero)
            elif self.tokens[i].getTipo() == 'DATOS':
                self.datos()
            elif self.tokens[i].getTipo() == 'MAX':
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "CADENA":
                        cadena = self.tokens[j].getLexema()
                    elif j > i and self.tokens[j].getTipo() == "PUNTO_COMA":
                        break
                self.max(cadena)
            elif self.tokens[i].getTipo() == 'MIN':
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "CADENA":
                        cadena = self.tokens[j].getLexema()
                    elif j > i and self.tokens[j].getTipo() == "PUNTO_COMA":
                        break
                self.min(cadena)

            elif self.tokens[i].getTipo() == 'FIN':
                self.interfaz.setPlainText(self.texto)

    def imprimir(self, iterador):
        valor = self.tokens[iterador + 2].getLexema()
        for v in valor:
            if v != "\"":
                self.texto += v
    
    def imprimir_ln(self, iterador):
        self.texto += "\n"
        valor = self.tokens[iterador + 2].getLexema()
        for v in valor:
            if v != "\"":
                self.texto += v

    def conteo(self):
        contador = 0
        for i in range(len(self.tokens)):
            if self.tokens[i].getTipo() == "REGISTROS":
                for j in range(len(self.tokens)):
                    if j > i and  self.tokens[j].getTipo() == "LLAVE_IZQUIERDA":
                        contador += 1
                    elif j > i and self.tokens[j].getTipo() == "CORCHETE_DERECHO":
                        break
        self.texto += "\n*** Conteo de Registros ***\n" + str(contador)

    def promedio(self, valor):
        posicion, subtotal, prom, n_registros = 0,0,0,0
        final = False
        for i in range(len(self.tokens)):
            if self.tokens[i].getTipo() == "CLAVES":
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "CORCHETE_DERECHO":
                        final = True
                    elif j > i and self.tokens[j].getTipo() == "CADENA" and final == False:
                        posicion += 1
                        if self.tokens[j].getLexema() == valor:
                            break
                    elif final == True:
                        break
        
        for i in range(len(self.tokens)):
            if self.tokens[i].getTipo() == "REGISTROS":
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "LLAVE_IZQUIERDA":
                        n_registros += 1
                        subtotal += float(self.tokens[j + posicion + (posicion - 1)].getLexema())
                    elif j>i and self.tokens[j].getTipo() == "CORCHETE_DERECHO":
                        break
        
        prom = round(subtotal / n_registros, 2)
        self.texto += "\n*** Promedio de " + valor + " ***\n" + str(prom)
    
    def sumar(self, valor):
        posicion, subtotal = 0,0
        final = False
        for i in range(len(self.tokens)):
            if self.tokens[i].getTipo() == "CLAVES":
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "CORCHETE_DERECHO":
                        final = True
                    elif j > i and self.tokens[j].getTipo() == "CADENA" and final == False:
                        posicion += 1
                        if self.tokens[j].getLexema() == valor:
                            break
                    elif final == True:
                        break
        
        for i in range(len(self.tokens)):
            if self.tokens[i].getTipo() == "REGISTROS":
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "LLAVE_IZQUIERDA":
                        subtotal += float(self.tokens[j + posicion + (posicion - 1)].getLexema())
                    elif j>i and self.tokens[j].getTipo() == "CORCHETE_DERECHO":
                        break
        
        self.texto += "\n*** Suma de " + valor + " ***\n" + str(subtotal)
    
    def datos(self):
        posicion = 0
        self.cabeceras, self.data = [], []
        self.info =  PrettyTable()
        final = False
        for i in range(len(self.tokens)):
            if self.tokens[i].getTipo() == "CLAVES":
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "CORCHETE_DERECHO":
                        final = True
                    elif j > i and self.tokens[j].getTipo() == "CADENA" and final == False:
                        posicion += 1
                        t_final = ''
                        valor = self.tokens[j].getLexema()
                        for v in valor:
                            if v != "\"":
                                t_final += v
                        self.cabeceras.append(t_final)
                    elif final == True:
                        break
        
        for i in range(len(self.tokens)):
            if self.tokens[i].getTipo() == "REGISTROS":
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "LLAVE_IZQUIERDA":
                        valores = []
                        for k in range(1,((posicion+1) + (posicion - 1))):
                            if self.tokens[j + k].getLexema() != ',':
                                valores.append(self.tokens[j + k].getLexema())
                    elif j > i and self.tokens[j].getTipo() == "LLAVE_DERECHA":
                        self.data.append(valores)
                    elif j>i and self.tokens[j].getTipo() == "CORCHETE_DERECHO":
                        break
        
        self.info.field_names = self.cabeceras
        self.info.add_rows(self.data)
        self.info.align = "l"
        temp = self.info.get_string()
        self.texto += "\n*** Datos en Archivo ***\n"  + temp   

    def contar_si(self, campo, valor):
        posicion = 0
        valores = []
        final = False
        for i in range(len(self.tokens)):
            if self.tokens[i].getTipo() == "CLAVES":
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "CORCHETE_DERECHO":
                        final = True
                    elif j > i and self.tokens[j].getTipo() == "CADENA" and final == False:
                        posicion += 1
                        if self.tokens[j].getLexema() == campo:
                            break
                    elif final == True:
                        break
        
        for i in range(len(self.tokens)):
            if self.tokens[i].getTipo() == "REGISTROS":
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "LLAVE_IZQUIERDA":
                        valores.append(float(self.tokens[j + posicion + (posicion - 1)].getLexema()))
                    elif j>i and self.tokens[j].getTipo() == "CORCHETE_DERECHO":
                        break
        contador = 0
        for i in range(len(valores)):
            if valores[i] == float(valor):
                contador += 1
        
        self.texto += "\n*** Contar si " + campo + " es igual a " + valor + " ***\n" + str(contador)
    
    def max(self, campo):
        posicion = 0
        valores = []
        final = False
        for i in range(len(self.tokens)):
            if self.tokens[i].getTipo() == "CLAVES":
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "CORCHETE_DERECHO":
                        final = True
                    elif j > i and self.tokens[j].getTipo() == "CADENA" and final == False:
                        posicion += 1
                        if self.tokens[j].getLexema() == campo:
                            break
                    elif final == True:
                        break
        
        for i in range(len(self.tokens)):
            if self.tokens[i].getTipo() == "REGISTROS":
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "LLAVE_IZQUIERDA":
                        valores.append(float(self.tokens[j + posicion + (posicion - 1)].getLexema()))
                    elif j>i and self.tokens[j].getTipo() == "CORCHETE_DERECHO":
                        break
        
        valores.sort(reverse=True)

        self.texto += "\n*** Valor maximo de " + campo + " ***\n" + str(valores[0])
    
    def min(self, campo):
        posicion = 0
        valores = []
        final = False
        for i in range(len(self.tokens)):
            if self.tokens[i].getTipo() == "CLAVES":
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "CORCHETE_DERECHO":
                        final = True
                    elif j > i and self.tokens[j].getTipo() == "CADENA" and final == False:
                        posicion += 1
                        if self.tokens[j].getLexema() == campo:
                            break
                    elif final == True:
                        break
        
        for i in range(len(self.tokens)):
            if self.tokens[i].getTipo() == "REGISTROS":
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "LLAVE_IZQUIERDA":
                        valores.append(float(self.tokens[j + posicion + (posicion - 1)].getLexema()))
                    elif j>i and self.tokens[j].getTipo() == "CORCHETE_DERECHO":
                        break
        
        valores.sort()

        self.texto += "\n*** Valor minimo de " + campo + " ***\n" + str(valores[0])
    
    def exportar_reporte(self, cadena):
        posicion = 0
        self.cabeceras, self.data = [], []
        final = False
        for i in range(len(self.tokens)):
            if self.tokens[i].getTipo() == "CLAVES":
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "CORCHETE_DERECHO":
                        final = True
                    elif j > i and self.tokens[j].getTipo() == "CADENA" and final == False:
                        posicion += 1
                        t_final = ''
                        valor = self.tokens[j].getLexema()
                        for v in valor:
                            if v != "\"":
                                t_final += v
                        self.cabeceras.append(t_final)
                    elif final == True:
                        break
        
        for i in range(len(self.tokens)):
            if self.tokens[i].getTipo() == "REGISTROS":
                for j in range(len(self.tokens)):
                    if j > i and self.tokens[j].getTipo() == "LLAVE_IZQUIERDA":
                        valores = []
                        for k in range(1,((posicion+1) + (posicion - 1))):
                            if self.tokens[j + k].getLexema() != ',':
                                valores.append(self.tokens[j + k].getLexema())
                    elif j > i and self.tokens[j].getTipo() == "LLAVE_DERECHA":
                        self.data.append(valores)
                    elif j>i and self.tokens[j].getTipo() == "CORCHETE_DERECHO":
                        break

        if len(self.cabeceras) != 0 and len(self.data) != 0:
            self.texto += "\n*** Generando reporte ***"
            self.reporte.generar_reporte(cadena,self.cabeceras, self.data)