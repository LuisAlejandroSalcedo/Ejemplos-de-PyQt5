import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QApplication, QMessageBox, QWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.resize(150, 40)
        btn1.move(400 / 2 - 150 / 2, 200 / 2 - 40)
        btn1.clicked.connect(self.buttonClicked)

        btn2 = QPushButton("Button 2", self)
        btn2.resize(150, 40)
        btn2.move(400 / 2 - 150 / 2, 200 / 2)
        btn2.clicked.connect(self.buttonClicked)

        self.resize(400, 200)
        self.setMaximumSize(400, 200)
        self.setWindowTitle('Event PyQT5')
        self.show()

    def buttonClicked(self, e):
        btn_txt = self.sender().text()
        QMessageBox.information(self, 'Events - Slot', 'click en: ' + btn_txt)

    def closeEvent(self, event):
        reply = QMessageBox.question(self,
                                     'Events - Slot',
                                     "Realmente desea cerrar la aplicacion",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    sys.exit(app.exec_())


