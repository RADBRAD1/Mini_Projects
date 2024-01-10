import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow #only need these 2 methods, not all of QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon 


class my_window(QMainWindow):
    def __init__(self):
        super(my_window, self).__init__()
        self.setGeometry(1200,300,700,700)
        self.setWindowTitle("Bugatti")
        self.setToolTip("Just Drive Me")
        self.setWindowIcon(QIcon("Bugattichiron1.jpg"))
        self.initUI() #define function we created in the initUI function
    
    def initUI(self): # add label, button, text box function
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Enter your name:")
        self.lbl_name.move(50,50)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Enter your surname:")
        self.lbl_surname.move(50,90)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(200,50)
        self.txt_name.resize(200,32)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(200,90)
        self.txt_surname.resize(200,32)

        self.btn_save = QtWidgets.QPushButton(self) #display the user inputted f/l name
        self.btn_save.setText("Save")
        self.btn_save.clicked.connect(self.clicked) # use clicked and connect method to run the "def clicked " function
        #when clicked. 
        self.btn_save.move(200,130)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("RESULT")
        self.lbl_result.move(200,170)
        self.lbl_result.resize(200,200)

    def clicked(self):
        self.lbl_result.setText("Name\t: " + self.txt_name.text() + "\nSurname : " + self.txt_surname.text())



def window(): #create desktop application, main instance, outside class
    app = QApplication(sys.argv)
    win = my_window()
    win.show()
    sys.exit(app.exec_())

window()


