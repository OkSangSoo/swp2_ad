from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QLabel , QTextEdit
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtWidgets import QToolButton, QSizePolicy
from random import random
from PyQt5.QtWidgets import QMainWindow

class Layout(QWidget):
    def __init__(self, parent=None):

        ##위젯의 사이즈 조절
        super().__init__()
        self.setGeometry(300,300,500,300)
        self.initUI()

    def initUI(self):
        ##모든버튼과 라벨을 생성합니다.
        koreaFoodButton=QPushButton("한식")
        chineseFoodButton=QPushButton("중식")
        japaneseFoodButton=QPushButton("일식")
        meatFoodButton=QPushButton("양식")
        randomButton=QPushButton("무작위")
        decideButton=QPushButton("확인")
        restaurantLabel = QLabel("식당")
        phoneNumberLabel = QLabel("전화 번호 ")
        specialLabel = QLabel("비고")

        #두번째 줄은 hbox 입니다.
        hbox=QHBoxLayout()
        hbox.addWidget(koreaFoodButton)
        hbox.addWidget(chineseFoodButton)
        hbox.addWidget(japaneseFoodButton)
        hbox.addWidget(meatFoodButton)
        hbox.addStretch(1)
        hbox.addWidget(randomButton)

        hbox4=QHBoxLayout()





        vbox=QVBoxLayout()

        ##hbox3은 두번째 레이아웃 입니다.
        hbox3=QHBoxLayout()
        textMessage1 = QLabel("어떤 음식이 좋을까요 ?")
        textMessage2 = QLabel("")
        textMessage=QLabel("")
        hbox3.addWidget(textMessage)
        hbox3.addWidget(textMessage1)
        hbox3.addWidget(textMessage2)

        hbox3.addWidget(decideButton)
        vbox.addLayout(hbox3)

        vbox.addLayout(hbox)


        vbox.addStretch(1)
        self.menuText1=QTextEdit()
        vbox1_1=QVBoxLayout()
        vbox1_1.addWidget(restaurantLabel)
        vbox1_1.addWidget(self.menuText1)
        self.menuText2 = QTextEdit()
        vbox1_2 = QVBoxLayout()
        vbox1_2.addWidget(phoneNumberLabel)
        vbox1_2.addWidget(self.menuText2)
        self.menuText3 = QTextEdit()
        vbox1_3 = QVBoxLayout()
        vbox1_3.addWidget(specialLabel)
        vbox1_3.addWidget(self.menuText3)

        hbox4.addLayout(vbox1_1)
        hbox4.addLayout(vbox1_2)
        hbox4.addLayout(vbox1_3)

        vbox.addLayout(hbox4)


        self.setLayout(vbox)

    def keyPressEvent(self,e):
        if e.key()==Qt.Key_Escape:
            self.close()

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    choiceMenu = Layout()
    choiceMenu.show()
    sys.exit(app.exec_())