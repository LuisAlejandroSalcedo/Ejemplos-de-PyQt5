# PyChrome

__author__ = "Luis Salcedo"

# Importamos las librerias necesarias
import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QProgressBar
from PyQt5.QtCore import QUrl


class PyChrome(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(640, 320)
        self.setWindowTitle('PyQt-5 WebEngine')

        page = "https://www.google.com"

        self.url = QLineEdit(page)
        self.url.setPlaceholderText(page)

        self.go = QPushButton("Ir")
        self.go.clicked.connect(self.btnIrClicked)

        self.nav_bar = QHBoxLayout()
        self.nav_bar.addWidget(self.url)
        self.nav_bar.addWidget(self.go)

        self.progress = QProgressBar()
        self.progress.setValue(0)

        html = """
        <!DOCTYPE HTML>
            <html>
                <head>
                    <title>Example Local HTML</title>
                </head>
                <body>
                    <p>Este es un archivo <code>HTML</code> local.</p>
                    <p>Si deseas acceder página indica su <code>URL</code> y presiona <b>Ir</b></p>
                </body>
            </html>
        """

        self.web_view = QWebEngineView()
        self.web_view.loadProgress.connect(self.webLoading)
        self.web_view.setHtml(html)

        root = QVBoxLayout()
        root.addLayout(self.nav_bar)
        root.addWidget(self.web_view)
        root.addWidget(self.progress)

        self.setLayout(root)

    def btnIrClicked(self, event):
        url = QUrl(self.url.text())
        self.web_view.page().load(url)

    def webLoading(self, event):
        self.progress.setValue(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = PyChrome()
    win.show()
    sys.exit(app.exec_())