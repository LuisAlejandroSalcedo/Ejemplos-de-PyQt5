import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('Layout PyQT-5')
    w.resize(250, 120)

    lblName = QLabel("Nombre:", w)
    lblName.move(20, 20)

    lblPass = QLabel("Contraseña:", w)
    lblPass.move(20, 50)

    txtName = QLineEdit(w)
    txtName.setPlaceholderText("Nombre de usuario")
    txtName.move(100, 15)

    txtPass = QLineEdit(w)
    txtPass.setPlaceholderText("Contraseña de usuario")
    txtPass.move(100, 45)

    btnLogin = QPushButton("Login", w)
    btnLogin.move(20, 80)
    btnLogin.resize(218, 30)

    w.show()

    sys.exit(app.exec_())
