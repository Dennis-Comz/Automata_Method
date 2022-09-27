import os

def text_inicial(titulo, inicial):
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,900;1,900&display=swap" rel="stylesheet">
    <title>''' + titulo + '''</title>
</head>
<body>
    <nav style="text-align: center;">
        <h1>'''+ inicial + '''</h1>
    </nav>
    <div>
        <table class="table table-bordered">
            <thead class="thead-dark">
              <tr>'''
    return html

class Reporte_Funcion:
    def __init__(self):
        pass

    def generar_reporte(self, titulo, cabecera, datos):
        html = text_inicial(titulo, "Reporte de Registros")
        
        for dato in cabecera:
            html += "\n\t\t\t<th scope=\"col\">" + dato + "</th>\n"

        html += '''
              </tr>
            </thead>
            <tbody>\n'''

        for dt in datos:
            html += "\t\t\t<tr>\n"
            for i in range(len(dt)):
                html += '\t\t\t\t<td>' + str(dt[i]) + "</td>\n"
        
        html += '\n\t\t</tbody>\n\t</table>\n</div>\n\n</body>\n</html>'
        file = open(titulo + ".html", 'w')
        file.write(html)
        file.close()
        os.startfile(titulo + '.html')

class Reporte_Tokens:
    def __init__(self) -> None:
        pass
    
    def generar_tokens(self, tokens):
        html = text_inicial("Reporte de Tokens", "Reporte de Tokens Validos")
        html += '''
                <th scope="col">#</th>
                <th scope="col">Token</th>
                <th scope="col">Lexema</th>
                <th scope="col">Fila</th>
                <th scope="col">Columna</th>
              </tr>
            </thead>
            <tbody>\n'''

        i = 1
        for token in tokens:
            html += "\t\t\t<tr>\n"
            html += '\t\t\t\t<th scope=\"row\">' + str(i) + "</th>\n"
            html += '\t\t\t\t<td>' + str(token.getTipo()) + "</td>\n"
            html += '\t\t\t\t<td>' + str(token.getLexema()) + "</td>\n"
            html += '\t\t\t\t<td>' + str(token.getFila()) + "</td>\n"
            html += '\t\t\t\t<td>' + str(token.getColumna()) + "</td>\n"
            html += "\t\t\t</tr>\n"
            i += 1
        html += '\n\t\t</tbody>\n\t</table>\n</div>\n</body>\n</html>'
        
        file = open("Reporte Tokens.html", 'w')
        file.write(html)
        file.close
        os.startfile('Reporte Tokens.html')

class Reporte_Errores:
    def __init__(self) -> None:
        pass

    def generar_errores(self, lexicos, sintacticos):
        html = text_inicial("Reporte Errores", "Reporte Errores Lexicos")
        html += '''
                <th scope="col">#</th>
                <th scope="col">Token</th>
                <th scope="col">Lexema</th>
                <th scope="col">Fila</th>
                <th scope="col">Columna</th>
              </tr>
            </thead>
            <tbody>\n'''

        i = 1
        for token in lexicos:
            html += "\t\t\t<tr>\n"
            html += '\t\t\t\t<th scope=\"row\">' + str(i) + "</th>\n"
            html += '\t\t\t\t<td>' + str(token.getTipo()) + "</td>\n"
            html += '\t\t\t\t<td>' + str(token.getLexema()) + "</td>\n"
            html += '\t\t\t\t<td>' + str(token.getFila()) + "</td>\n"
            html += '\t\t\t\t<td>' + str(token.getColumna()) + "</td>\n"
            html += "\t\t\t</tr>\n"
            i += 1
        html += '\n\t\t</tbody>\n\t</table>\n</div>\n'
        html += '''<div>
        <h1 style="text-align: center;">Reporte de Errores Sintacticos</h1>
        <table class="table table-bordered">
            <thead class="thead-dark">
              <tr>
                <th scope="col">#</th>
                <th scope="col">Token</th>
                <th scope="col">Lexema</th>
                <th scope="col">Fila</th>
                <th scope="col">Columna</th>
                <th scope="col">Esperado</th>
              </tr>
            </thead>
            <tbody>\n'''

        i = 1
        html += "\t\t\t<tr>\n"
        html += '\t\t\t\t<th scope=\"row\">' + str(1) + "</th>\n"
        for i in range(len(sintacticos)):
            html += '\t\t\t\t<td>' + str(sintacticos[i]) + "</td>\n"
        html += "\t\t\t</tr>\n"
        html += '\n\t\t</tbody>\n\t</table>\n</div>\n</body>\n</html>'

        file = open("Reporte Errores.html", 'w')
        file.write(html)
        file.close
        os.startfile('Reporte Errores.html')