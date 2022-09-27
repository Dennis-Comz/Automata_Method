class Error:
    
    def __init__(self, descripcion, linea, columna):
        self.descripcion = descripcion
        self.linea = linea
        self.columna = columna
    
    def imprimirData(self):
        print(self.descripcion,self.linea, self.columna)