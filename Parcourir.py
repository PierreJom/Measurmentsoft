from PyQt5.QtWidgets import QWidget, QFileDialog


class App(QWidget):
    global fileName

    def __init__(self):
        super().__init__()
        self.title = 'Ouvrir'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        global fileName
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "Ouvrir", 'C:\\Users\Pierre.J\Desktop', "All Files (*);;Text Files (*.txt);;CSV Files (*.csv)", 'Desktop', options=options)
        self.show()
