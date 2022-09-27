from graphviz import Graph

i = 0
dot= Graph('Ast', 'png')
dot.format = 'png'
dot.attr(splines='false')
dot.node_attr.update(shape='circle')
dot.edge_attr.update(color = 'blue')

def inc():
	global i
	i += 1
	return i 

def getNumNodo():
	global i
	return i

class ExpresionIdentificador() :
    def __init__(self, id) :
        self.id = id

    def getValor(self, entorno):
        return entorno.get(self.id)

    def getNodos(self):
        global dot
        idnodo = str(inc())
        dot.node(idnodo , "expresion")

        idid = str(inc())
        dot.node(idid , "identificador")

        idexp = str(inc())
        dot.node(idexp , self.id)

        dot.edge(idid, idexp)
        dot.edge(idnodo, idid)

        return idnodo

class ExpresionLiteral() :
    def __init__(self, tipo, valor) :
        self.tipo = tipo
        self.valor = valor

    def getValor(self, entorno):
        return self.valor

    def getNodos(self):
        global dot
        idnodo = str(inc())
        dot.node(idnodo , "expresion")
        idlit = str(inc())
        dot.node(idlit , "literal")
        idexp = str(inc())
        dot.node(idexp , self.valor)
        dot.edge(idlit, idexp)
        dot.edge(idnodo, idlit)
        return idnodo