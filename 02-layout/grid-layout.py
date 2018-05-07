import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('Layout PyQT-5')
    w.resize(250, 120)

    lblName = QLabel("Nombre:")
    txtName = QLineEdit()
    txtName.setPlaceholderText("Nombre de usuario")

    lblPass = QLabel("Contraseña:")
    txtPass = QLineEdit(w)
    txtPass.setPlaceholderText("Contraseña de usuario")

    grid = QGridLayout()
    grid.addWidget(lblName, 0, 0)
    grid.addWidget(txtName, 0, 1)
    grid.addWidget(lblPass, 1, 0)
    grid.addWidget(txtPass, 1, 1)

    btnLogin = QPushButton("Login", w)
    grid.addWidget(btnLogin, 2, 0, 1, 2)

    w.setLayout(grid)
    w.show()

    sys.exit(app.exec_())
