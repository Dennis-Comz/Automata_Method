import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QFrame, QLabel, QMainWindow, QPlainTextEdit, QPushButton, QVBoxLayout, QHBoxLayout
from Lexico import Analizador
from Reportes import Reporte_Tokens, Reporte_Errores
import sys

class Gui:
    def __init__(self):
        self.lexico = Analizador()
        self.reporte = Reporte_Tokens()
        self.errores = Reporte_Errores()
        self.text = ''
        self.window()

    def window(self):
        # Inicio de la app y conexion a stylesheet
        self.app = QApplication(sys.argv)

        with open("Gui/style.qss", "r") as f:
            _style = f.read()
            self.app.setStyleSheet(_style)

        # Ventana principal desplegada
        self.mainW = QMainWindow()
        self.mainW.setGeometry(350, 150, 1300, 800)
        self.mainW.setWindowTitle("Proyecto 2")

        # Frame de los botones y division
        self.btnFrame = QFrame(self.mainW)
        self.btnFrame.setGeometry(0,0,1300,100)
        
        self.dvLabel = QLabel('Label', self.mainW)
        self.dvLabel.setGeometry(0,100, 1300, 2)
        self.dvLabel.setStyleSheet('background-color: black;')
        
        # ------------- Botones --------------- #
        # Widget para ordenar los botones
        self.vbox = QVBoxLayout(self.btnFrame)
        self.hbox = QHBoxLayout()
        self.hbox.setContentsMargins(0,0,0,0)
        self.hbox.addStretch()

        self.btnCargar = QPushButton()
        self.btnCargar.setText("Cargar Archivo")
        self.btnCargar.clicked.connect(self.cargarArchivo)
        self.hbox.addWidget(self.btnCargar)
        self.hbox.addStretch()

        self.btnAnalizar = QPushButton("Analizar")
        self.btnAnalizar.clicked.connect(self.analizar_texto)
        self.hbox.addWidget(self.btnAnalizar)
        self.hbox.addStretch()
        
        self.btnReportes = QPushButton("Reportes")
        self.btnReportes.clicked.connect(self.generar_reportes)
        self.hbox.addWidget(self.btnReportes)
        self.hbox.addStretch()
        
        self.btnArbol = QPushButton("Arbol")
        self.btnArbol.clicked.connect(self.lexico.generar_arbol)
        self.hbox.addWidget(self.btnArbol)
        self.hbox.addStretch()

        self.vbox.addLayout(self.hbox)
        #  ----------- Fin Botones ----------- #

        # text displayers
        # Editable
        self.textEditor = QPlainTextEdit(self.mainW)
        self.textEditor.setGeometry(50, 150, 550, 600)

        # No editable
        self.displayText = QPlainTextEdit(self.mainW)
        self.displayText.setReadOnly(True)
        self.displayText.setGeometry(650, 150, 600, 600)

        self.lexico.setTextEditor(self.displayText)
        
        self.mainW.show()
        sys.exit(self.app.exec_())

    def getWindow(self):
        return self.mainW

    def getTextEditor(self):
        return self.textEditor

    def getdisplayText(self):
        return self.displayText

    def cargarArchivo(self):
        self.filename = QFileDialog.getOpenFileName(None, None, None, 'lfp files (*.lfp)')
        if os.path.exists(self.filename[0]) == True:
            self.text = open(self.filename[0], 'r')
            self.text = self.text.read()
            self.textEditor.setPlainText(self.text)
            text = self.textEditor.toPlainText()

    def analizar_texto(self):
        if self.textEditor.toPlainText() != '':
            self.text = self.textEditor.toPlainText()
        self.lexico.reader(self.text)

    def generar_reportes(self):
        tokens = self.lexico.getTokens()
        erroresL = self.lexico.getErrores()
        erroresS = self.lexico.getErroresSint()
        self.reporte.generar_tokens(tokens)
        self.errores.generar_errores(erroresL, erroresS)
        

    def getText(self):
        return self.text