from PyQt5.QtWidgets import QApplication
from main_page import Main

app=QApplication([])
win=Main()
win.show()
app.exec_()
