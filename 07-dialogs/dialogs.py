import sys

from PyQt5.QtCore import Qt, QDir
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog, QVBoxLayout, QPushButton, QFileDialog, QColorDialog, \
    QFontDialog, QMessageBox


class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)

        btn0 = QPushButton('Mostrar QInputDialog')
        btn0.clicked.connect(self.showIntDialog)

        btn1 = QPushButton('Mostrar QFileDialog')
        btn1.clicked.connect(self.buscarArchivo)

        btn2 = QPushButton('Mostrar QColorDialog')
        btn2.clicked.connect(self.buscarColor)

        btn3 = QPushButton('Mostrar QFontDialog')
        btn3.clicked.connect(self.cambiarFuente)

        btn4 = QPushButton('Mostrar QMessageBox')
        btn4.clicked.connect(self.showDialog)

        vbox = QVBoxLayout()
        vbox.addWidget(btn0)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addStretch(0)

        self.setLayout(vbox)
        self.setWindowTitle("Cuadros de Dialogo")
        self.resize(250, 320)

    def buscarArchivo(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Buscar Archivo')#, QDir.homePath(), "All Files (*);;Text Files (*.txt)")
        if file:
            print("Archivo seleccionado: ", file)

    def showIntDialog(self):
        value, ok = QInputDialog.getText(self, "getText()", "Como te llamas:")
        if ok and value != '' : print('Nombre:', value)

        value, ok = QInputDialog.getInt(self, "getInt()", "Dime Tu Edad:", 18, 1, 150)
        if ok : print('Edad:', value)

        value, ok = QInputDialog.getDouble(self, "getDouble()", "Cuanto Pesas:")
        if ok : print('Peso:', value)

        items = ("Perro", "Gato", "Aves", "Serpientes", "Otros")
        value, ok = QInputDialog.getItem(self, "getItem()", "Mascota favorita:", items, 2)
        if ok : print('Mascota:', value)

    def buscarColor(self):
        color = QColorDialog.getColor(Qt.red, self)
        if color.isValid():
            self.setPalette(QPalette(color))

    def cambiarFuente(self):
        font, ok = QFontDialog.getFont(self)
        if ok:
            self.setFont(font)

    def showDialog(self):
        # QMessageBox.warning(self, "Warning Dialog", "Peligro Alto Voltage")
        reply = QMessageBox.critical(self, "QMessageBox.critical()",
                "Error irrecuperable en la aplicacion \n que desea hacer para proceder.",
                QMessageBox.Abort | QMessageBox.Retry | QMessageBox.Ignore)
        if reply == QMessageBox.Abort:
            print("Abortar la mision")
        elif reply == QMessageBox.Retry:
            print("Intentar nuevamente")
        else:
            print("Nada por ahora")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Example()
    dialog.show()
    sys.exit(app.exec_())