from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QLabel , QTextEdit
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtWidgets import QToolButton, QSizePolicy
from random import random
from PyQt5.QtWidgets import QMainWindow

class Layout_save(QWidget):
    def __init__(self, parent=None):

        ##위젯의 사이즈 조절
        super().__init__()
        self.setGeometry(500,300,600,400)
        self.initUI()

    def initUI(self):

        ##모든 버튼과 라벨을 생성합니다.
        vbox=QVBoxLayout()
        hbox=QHBoxLayout()
        vbox_1_1_1=QVBoxLayout()
        vbox_1_1_2=QVBoxLayout()
        hbox_1=QHBoxLayout()
        vbox_1_1=QVBoxLayout()
        vbox_1_2=QVBoxLayout()
        vbox_1_3=QVBoxLayout()
        backButton=QPushButton("뒤로")

        vbox.addLayout(hbox)
        hbox.addLayout(vbox_1_1_1)
        hbox.addLayout(vbox_1_1_2)

        vbox_1_1_1.addLayout(vbox_1_1)
        vbox_1_1_1.addLayout(vbox_1_2)
        vbox_1_1_1.addLayout(vbox_1_3)
        vbox_1_1_2.addWidget(backButton)
        vbox_1_1_2.addStretch(1)

        self.setLayout(vbox)



class Layout_first(QWidget):
    def __init__(self, parent=None):

        ##위젯의 사이즈 조절
        super().__init__()
        self.setGeometry(500,300,600,400)
        self.initUI()

    def initUI(self):
        ##모든버튼과 라벨을 생성합니다.
        saveMenu=QPushButton("장바구니")
        koreaFoodButton=QPushButton("한식")
        chineseFoodButton=QPushButton("중식")
        japaneseFoodButton=QPushButton("일식")
        meatFoodButton=QPushButton("양식")
        schoolFoodButton=QPushButton("학식")
        randomButton=QPushButton("무작위")
        decideButton=QPushButton("확인")
        restaurantLabel = QLabel("식당")
        phoneNumberLabel = QLabel("전화 번호 ")
        specialLabel = QLabel("비고")
        textMessage = QLabel("어떤 음식이 좋을까요 ?")
        defaultMessage = QLabel("")
        self.restaurantText= QTextEdit()
        self.phoneNumText=QTextEdit()
        self.specialText=QTextEdit()

        ##LayoutBox 들을 생성 합니다.
        vbox_1L = QVBoxLayout()
        vbox_1R = QVBoxLayout()
        vbox_2L = QVBoxLayout()
        vbox_2M = QVBoxLayout()
        vbox_2R = QVBoxLayout()
        hbox_1Main = QHBoxLayout()
        hbox_1L_1 = QHBoxLayout()
        hbox_1L_2 = QHBoxLayout()
        hbox_1L_3 = QHBoxLayout()
        hbox_2Main = QHBoxLayout()

        ##hbox_1과 hbox_2에 레이아웃을 집어 넣습니다.
        vbox_1L.addLayout(hbox_1L_1)
        vbox_1L.addLayout(hbox_1L_2)
        vbox_1L.addLayout(hbox_1L_3)
        hbox_1Main.addLayout(vbox_1L)
        hbox_1Main.addLayout(vbox_1R)
        hbox_2Main.addLayout(vbox_2L)
        hbox_2Main.addLayout(vbox_2M)
        hbox_2Main.addLayout(vbox_2R)

        ##hbox_1안의 레이아웃에 위젯을 넣습니다.


        hbox_1L_1.addStretch(1)
        hbox_1L_1.addWidget(textMessage)
        hbox_1L_1.addStretch(1)

        hbox_1L_2.addWidget(koreaFoodButton)
        hbox_1L_2.addStretch(1)
        hbox_1L_2.addWidget(chineseFoodButton)
        hbox_1L_2.addStretch(1)
        hbox_1L_2.addWidget(japaneseFoodButton)
        hbox_1L_2.addStretch(1)
        hbox_1L_2.addWidget(meatFoodButton)
        hbox_1L_2.addStretch(1)
        hbox_1L_2.addWidget(schoolFoodButton)

        hbox_1L_3.addWidget(defaultMessage)

        vbox_1R.addWidget(saveMenu)
        vbox_1R.addWidget(randomButton)
        vbox_1R.addWidget(decideButton)

        ##hbox_2안의 레이아웃에 위젯을 넣습니다.


        vbox_2R.addWidget(restaurantLabel)
        vbox_2R.addWidget(self.restaurantText)
        vbox_2M.addWidget(phoneNumberLabel)
        vbox_2M.addWidget(self.phoneNumText)
        vbox_2L.addWidget(specialLabel)
        vbox_2L.addWidget(self.specialText)



        ##보여줄 레이아웃
        vbox_main=QVBoxLayout()
        vbox_main.addLayout(hbox_1Main)
        vbox_main.addLayout(hbox_2Main)
        self.setLayout(vbox_main)

    def keyPressEvent(self,e):
        if e.key()==Qt.Key_Escape:
            self.close()

class Layout_menu(QWidget):
    def __init__(self, parent=None):

        ##위젯의 사이즈 조절
        super().__init__()
        self.setGeometry(300,300,500,300)
        self.initUI()

    def initUI(self):

        ##모든 버튼과 라벨을 생성 합니다.
        vbox=QVBoxLayout()
        hbox_1=QHBoxLayout()

        hbox_2=QHBoxLayout()
        restaurantLabel=QLabel("메뉴를 입력해 주세요 : ")
        restaurantText=QLineEdit()
        priceLabel=QLabel("")
        backButton=QPushButton("뒤로")
        vbox_2_1=QVBoxLayout()
        vbox_2_2=QVBoxLayout()
        vbox_2_3=QVBoxLayout()
        vbox_2_4=QVBoxLayout()
        randombutton=QPushButton("무작위")
        decideButton=QPushButton("결정")
        menu_Label=QLabel("메뉴")
        price_Label=QLabel("가격")
        special_Label=QLabel("비고")
        self.menuText=QTextEdit("")
        self.priceText=QTextEdit("")
        self.specialText=QTextEdit("")


        ##vbox에 vbox_1과 hbox_2 넣기
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)

        ##hbox_1 채워넣기

        hbox_1.addWidget(restaurantLabel)
        hbox_1.addWidget(restaurantText)
        hbox_1.addWidget(priceLabel)
        hbox_1.addStretch(1)
        hbox_1.addWidget(backButton)

        ##vbox_2 채워넣기

        hbox_2.addLayout(vbox_2_1)
        vbox_2_1.addWidget(menu_Label)
        vbox_2_1.addWidget(self.menuText)
        hbox_2.addLayout(vbox_2_2)
        vbox_2_2.addWidget(price_Label)
        vbox_2_2.addWidget(self.priceText)
        hbox_2.addLayout(vbox_2_3)
        vbox_2_3.addWidget(special_Label)
        vbox_2_3.addWidget(self.specialText)
        hbox_2.addLayout(vbox_2_4)
        vbox_2_4.addWidget(randombutton)
        vbox_2_4.addStretch(1)
        vbox_2_4.addWidget(decideButton)

        self.setLayout(vbox)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    choiceMenu = Layout_menu()
    choiceMenu.show()
    sys.exit(app.exec_())
