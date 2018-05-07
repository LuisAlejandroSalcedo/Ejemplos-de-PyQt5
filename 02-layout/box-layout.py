import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('Layout PyQT-5')
    w.resize(250, 120)

    vbox = QVBoxLayout()
    vbox.setSpacing(20)

    for n in range(5):
        if n == 2:
            hbox = QHBoxLayout()
            for m in range(3):
                hbox.addWidget(QPushButton("Button #" + str(m)))
            vbox.addLayout(hbox)
        else:
            vbox.addWidget(QPushButton("Button #" + str(n)))

    w.setLayout(vbox)
    w.show()

    sys.exit(app.exec_())
