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
        randomButton_2=QPushButton("무작위")
        decideButton=QPushButton("확인")
        restaurantLabel = QLabel("식당")
        phoneNumberLabel = QLabel("전화 번호 ")
        specialLabel = QLabel("비고")
        textMessage = QLabel("어떤 음식이 좋을까요 ?")
        NoneMessage=QLabel("")
        self.restaurantText= QTextEdit()
        self.phoneNumText=QTextEdit()
        self.specialText=QTextEdit()

        ##LayoutBox 들을 생성 합니다.

        hbox_1=QHBoxLayout()
        hbox_2=QHBoxLayout()
        hbox_1_1=QHBoxLayout()
        hbox_1_2=QHBoxLayout()
        vbox_2_1=QVBoxLayout()
        vbox_2_2=QVBoxLayout()
        vbox_2_3=QVBoxLayout()
        vbox_2_4=QVBoxLayout()

        ##hbox_1과 hbox_2에 레이아웃을 집어 넣습니다.

        hbox_1.addLayout(hbox_1_1)
        hbox_1.addLayout(hbox_1_2)
        hbox_2.addLayout(vbox_2_1)
        hbox_2.addLayout(vbox_2_2)
        hbox_2.addLayout(vbox_2_3)
        hbox_2.addLayout(vbox_2_4)

        ##hbox_1안의 레이아웃에 위젯을 넣습니다.

        hbox_1_1.addWidget(textMessage)
        hbox_1_2.addWidget(koreaFoodButton)
        hbox_1_2.addWidget(chineseFoodButton)
        hbox_1_2.addWidget(japaneseFoodButton)
        hbox_1_2.addWidget(meatFoodButton)
        hbox_1_2.addStretch(1)
        hbox_1_2.addWidget(randomButton)

        ##hbox_2안의 레이아웃에 위젯을 넣습니다.

        vbox_2_1.addWidget(restaurantLabel)
        vbox_2_1.addWidget(self.restaurantText)
        vbox_2_2.addWidget(phoneNumberLabel)
        vbox_2_2.addWidget(self.phoneNumText)
        vbox_2_3.addWidget(specialLabel)
        vbox_2_3.addWidget(self.specialText)
        vbox_2_4.addWidget(NoneMessage)
        vbox_2_4.addWidget(randomButton_2)
        vbox_2_4.addStretch(1)
        vbox_2_4.addWidget(decideButton)

        ##보여줄 레이아웃
        vbox=QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
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