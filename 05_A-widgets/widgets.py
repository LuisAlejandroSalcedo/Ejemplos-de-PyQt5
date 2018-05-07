import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox, QLineEdit, QLabel, QSlider, QLCDNumber, QCalendarWidget, \
    QGroupBox, QRadioButton, QVBoxLayout
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.addCheckBox()
        self.addLineEdit()
        self.addSlider()
        self.addCalendar()
        self.addRadioBoton()

        self.resize(640, 320)
        self.setWindowTitle('Controles PyQT 5 by Tutor de Programacion')

    def addRadioBoton(self):
        gbx = QGroupBox('Tu Lenguaje Favorito', self)
        gbx.setGeometry(20, 150, 185, 120)
        # crear tres QRadioButton
        radio1 = QRadioButton("C/C++")
        radio2 = QRadioButton("Python")
        radio3 = QRadioButton("Java")
        # agregar los widgets al layout vertical
        vbox = QVBoxLayout(self)
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        # establecer el layout del QGroupBox
        gbx.setLayout(vbox)

        # radio1.setChecked(True)
        # print(radio1.isChecked())


    def addCalendar(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked.connect(self.timeSelected)
        cal.move(300, 20)

    def timeSelected(self, date):
        print('La Fecha es: ', date.toString())

    def addSlider(self):
        sld = QSlider(Qt.Horizontal, self)
        # establecer posicion (x,y) y dimenciones (ancho, alto)
        sld.setGeometry(20, 80, 150, 30)
        # indicar rango de valores validos
        sld.setRange(50, 250)
        # establecer valor inicial
        sld.setValue(120)
        # evento producido cada vez que cambia el valor
        sld.valueChanged.connect(self.valChange)

        num = QLCDNumber(self)
        num.setGeometry(180, 80, 50, 30)
        # mostrar valor inicial
        num.display(sld.value())
        # cambiar valor QLCDNumber cuando cambiar QSlider
        sld.valueChanged.connect(num.display)

    def valChange(self, value):
        print('QSlider value: ', value)

    def addLineEdit(self):
        # crea un texto no es editable
        lbl = QLabel('Nombre:', self)
        lbl.move(20, 52)

        # crea un widget que permite editar una linea de texto
        txt = QLineEdit(self)
        txt.move(72, 50)
        # establece un texto informativo
        txt.setPlaceholderText('Dime tu nombre')
        # evento producido cada vez que cambia el texto
        txt.textChanged.connect(self.textChange)
        # establece el foco en el widget
        txt.setFocus()
        # obtiene el texto escrito
        nombre = txt.text()

    def textChange(self, text):
        print('El nuevo texto es: ', text)


    def addCheckBox(self):
        # Crear el widget
        cbx = QCheckBox('Mostrar/Ocultar', self)
        # Cambiar estado del CheckBox puede ser: Qt.PartiallyChecked, Qt.Checked, Qt.Unchecked
        cbx.setCheckState(Qt.PartiallyChecked)
        # Responder al evento de cambio de estado
        cbx.stateChanged.connect(self.cbxChange)
        # Ubicar el control en la posicion (x, y)
        cbx.move(20, 20)

    def cbxChange(self, state):
        print('CheckBox State: ', state)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec_())
