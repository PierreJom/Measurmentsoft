import Fenetre
import sys


def Affichage():
    if __name__ == "__main__":
        app = Fenetre.QtWidgets.QApplication(sys.argv)
        MainWindow = Fenetre.QtWidgets.QMainWindow()
        ui = Fenetre.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())


Affichage()
