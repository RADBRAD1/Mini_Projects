import sys
from PyQt5.QtWidgets import QApplication, QMainWindow #only need these 2 methods, not all of QtWidgets
from PyQt5.QtGui import QIcon 
"""
from PyQt5 import QtWidgets """

def window():
    app = QApplication(sys.argv)
   # no need for QtWidgets.qapp, b/c we imported from submodule. -->  app = QtWidgets.QApplication(sys.argv)
    win = QMainWindow() #create a window
   # win = QtWidgets.QMainWindow() #create a window
    win.setGeometry(1200,500,500,500)
    win.setWindowTitle("Bugatti")
    win.setWindowIcon(QIcon("Bugattichiron1.jpg"))
    win.setToolTip("Just drive me")
    win.show() #show created desktop window
    sys.exit(app.exec_()) #send argument to close app when close button clicked

window() #call function 


