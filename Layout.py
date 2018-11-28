from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QLabel
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtWidgets import QToolButton, QSizePolicy
from random import random
from PyQt5.QtWidgets import QMainWindow

class Layout(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setGeometry(500,100,800,800)
        self.initUI()

    def initUI(self):
        koreaFoodButton=QPushButton("한식")
        chineseFoodButton=QPushButton("중식")
        japaneseFoodButton=QPushButton("일식")
        meatFoodButton=QPushButton("양식")
        randomButton=QPushButton("무작위")
        decideButton=QPushButton("확인")

        hbox=QHBoxLayout()
        hbox.addWidget(koreaFoodButton)
        hbox.addWidget(chineseFoodButton)
        hbox.addWidget(japaneseFoodButton)
        hbox.addWidget(meatFoodButton)
        hbox.addStretch(1)
        hbox.addWidget(randomButton)



        hbox2=QHBoxLayout()
        randomButton2=QPushButton("무작위")
        restaurantLabel=QLabel("식당")
        phoneNumberLabel=QLabel("전화 번호 ")
        specialLabel=QLabel("비고")
        hbox2.addWidget(restaurantLabel)
        hbox2.addWidget(phoneNumberLabel)
        hbox2.addWidget(specialLabel)
        hbox2.addStretch(1)
        hbox2.addWidget(randomButton2)

        vbox=QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)






if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    choiceMenu = Layout()
    choiceMenu.show()
    sys.exit(app.exec_())