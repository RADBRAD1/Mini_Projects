import sys
from PyQt5.QtWidgets import QApplication, QMainWindow #only need these 2 methods, not all of QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon 

def window():
    app = QApplication(sys.argv)
    win = QMainWindow() #create a window, win is the mainapps name
    win.setGeometry(1200,500,500,500) #starting position
    win.setWindowTitle("Bugatti") #title
    win.setWindowIcon(QIcon("Bugattichiron1.jpg"))# photo icon added
    win.setToolTip("Just drive me")

    lbl_name = QtWidgets.QLabel(win) 
    lbl_name.setText("Enter your name :")
    lbl_name.move(50,50) #change label position

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Enter your surname:")
    lbl_surname.move(50,90)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(200,50)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(200,90)

    def clicked(self):
        print("button clicked")
        print("name :" + txt_name.text()) 
        print("surname :" + txt_surname.text())

    btn_save = QtWidgets.QPushButton(win) #create a button
    btn_save.setText("Save") #given button text displaying "save"
    btn_save.clicked.connect(clicked) #when we click the botton, we perform the task of the function also named
    btn_save.move(200,130)

    win.show() #show created desktop window
    sys.exit(app.exec_()) #send argument to close app when close button clicked

    

window() #call function 


