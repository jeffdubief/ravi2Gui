import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp


class Gui(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        fichierMenu = menubar.addMenu("Fichier")

        openAct = QAction("Ouvrir",self)
        openAct.triggered.connect(self.open)
        openAct.setShortcut('ctrl+O')
        openAct.setStatusTip('Ouvrir un fichier')

        recAct = QAction("Enregistrer",self)
        recAct.triggered.connect(self.rec)
        recAct.setShortcut('ctrl+S')
        recAct.setStatusTip('Enregistrer un fichier')


        quitAct = QAction("Quitter",self)
        quitAct.triggered.connect(self.exit)
        quitAct.setShortcut('ctrl+Q')
        quitAct.setStatusTip('Quitter')



        fichierMenu.addAction(openAct)
        fichierMenu.addAction(recAct)
        fichierMenu.addAction(quitAct)

        self.setMinimumSize(1280, 720)

        self.setWindowTitle('Ravi Example')
        self.show()

    def open(self):
        print("open")

    def rec(self):
        print("rec")

    def exit(self):
        print("exit")
        self.quit

