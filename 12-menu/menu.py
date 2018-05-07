import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        statusbar = self.statusBar()
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        copyAction = QAction(QIcon('copy.png'), 'Copy', self)
        pasteAction = QAction(QIcon('paste.png'), 'Paste', self)
        cutAction = QAction(QIcon('cut.png'), 'Cut', self)

        editMenu = menubar.addMenu('Ed&it')
        editMenu.addAction(copyAction)
        editMenu.addAction(pasteAction)
        editMenu.addAction(cutAction)

        findMenu = editMenu.addMenu(QIcon('image/find_disabled.png'), 'Find')

        findAction = QAction('Find', self)
        findAction.setShortcut('Ctrl+F')
        findAction.setStatusTip('Buscar texto indicado')

        replaceAction = QAction('Replace', self)
        replaceAction.setShortcut('Ctrl+R')
        replaceAction.setStatusTip('Reemplazar texto seleccionado')

        findMenu.addAction(findAction)
        findMenu.addAction(replaceAction)

        aboutAction = QAction('&About', self)
        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(aboutAction)

        self.resize(420, 280)
        self.setWindowTitle('Menubar And Statusbar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())