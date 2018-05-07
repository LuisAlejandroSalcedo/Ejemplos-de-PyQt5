__author__ = 'Carmelo Marin Abrego'

import sys

from PyQt5.QtGui import QPainter, QFont, QColor, QPixmap, QPen, QBrush
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(1280, 720)
        self.setWindowTitle('PyQT5 Paint Event')

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawImage(event, qp, 'image/image.jpg')
        self.drawText(event, qp, 'Tutor de Programación\nPintar con PyQT5')
        self.drawPoint(event, qp)
        self.drawLine(event, qp)
        self.drawShape(event, qp)
        qp.end()

    def drawShape(self, event, qp):
        pen = QPen(Qt.yellow)
        pen.setWidth(3)
        # rellenar fondo con patron de imagen
        brush = QBrush()
        brush.setTexture(QPixmap('image/small_image.jpg'))
        # establecer el QBrush
        qp.setBrush(brush)
        qp.setPen(pen)
        qp.drawRoundedRect(QRect(50, 50, 200, 150), 15, 15)
        # utilizar un patron predefinido
        brush.setStyle(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawEllipse(350, 50, 150, 150)

    def drawPoint(self, event, qp):
        pen = QPen(Qt.red)
        pen.setWidth(10)

        qp.setPen(pen)
        qp.drawPoint(event.rect().width() / 2, event.rect().height() / 2)

    def drawLine(self, event, qp):
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(128, 250, 25, 255))
        pen.setStyle(Qt.DotLine)

        qp.setPen(pen)
        qp.drawLine(QPoint(10, 10), QPoint(1280 - 10, 10))

        color = QColor()
        color.setNamedColor('#c2h6b4')

        pen.setColor(color)
        pen.setStyle(Qt.DashLine)

        qp.setPen(pen)
        qp.drawLine(QPoint(10, 10 + 20), QPoint(1280 - 10, 10 + 20))


    def drawImage(self, event, qp, image):
        pixmap = QPixmap(image)
        qp.drawPixmap(event.rect(), pixmap)
        # qp.drawPixmap(QRect(0, 0, 1280, 720), pixmap)

    def drawText(self, event, qp, text):
        qp.setPen(QColor(0, 255, 255))
        qp.setFont(QFont('Consolas', 48))
        qp.drawText(event.rect(), Qt.AlignCenter, text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec_())


