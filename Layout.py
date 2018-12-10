from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QLabel , QTextEdit
from PyQt5.QtWidgets import QPushButton,QVBoxLayout,QHBoxLayout
import random_category
import random_menu

class Layout_save(QWidget):
    def __init__(self, parent=None):

        ##위젯의 사이즈 조절
        super().__init__()
        self.setGeometry(500,300,600,400)
        self.initUI()




    def initUI(self):

        ##모든 버튼과 라벨을 생성합니다.
        vbox=QVBoxLayout()
        hbox_1=QHBoxLayout()
        hbox_2=QHBoxLayout()
        vbox_1_1=QVBoxLayout()
        vbox_1_2=QVBoxLayout()
        vbox_1_3=QVBoxLayout()
        vbox_1_4=QVBoxLayout()
        restaurantLabel=QLabel("식당")
        menuLabel=QLabel("메뉴")
        priceLabel=QLabel("가격")
        backButton=QPushButton("뒤로")
        backButton.clicked.connect(self.backButtonClicked)

        restaurantText=QTextEdit()
        restaurantText.setReadOnly(True)
        menuText=QTextEdit()
        menuText.setReadOnly(True)
        priceText=QTextEdit()
        priceText.setReadOnly(True)
        totalPriceLabel=QLabel("총금액 : ")
        randomButton=QPushButton("무작위선택")

        ##hbox_1에 집어넣기
        hbox_1.addLayout(vbox_1_1)
        vbox_1_1.addWidget(restaurantLabel)
        vbox_1_1.addWidget(restaurantText)
        hbox_1.addLayout(vbox_1_2)
        vbox_1_2.addWidget(menuLabel)
        vbox_1_2.addWidget(menuText)
        hbox_1.addLayout(vbox_1_3)
        vbox_1_3.addWidget(priceLabel)
        vbox_1_3.addWidget(priceText)
        hbox_1.addLayout(vbox_1_4)
        vbox_1_4.addWidget(backButton)
        vbox_1_4.addStretch(1)

        ##hbox_2에 집어넣기
        hbox_2.addWidget(totalPriceLabel)
        hbox_2.addStretch(1)
        hbox_2.addWidget(randomButton)
        ##vbox에 레이아웃 집어넣기
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)

        ##설정하기
        self.setLayout(vbox)

        ##버튼이벤트

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def backButtonClicked(self):
        self.hide()
        self.Layout_first=Layout_first()
        self.Layout_first.show()







class Layout_first(QWidget):
    def __init__(self, parent=None):

        ##위젯의 사이즈 조절
        super().__init__()
        self.setGeometry(500,300,600,400)
        self.initUI()
        self.Layout_menu = Layout_menu()
        self.Layout_save = Layout_save()
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
        self.restaurantText= QTextEdit()
        self.restaurantText.setReadOnly(True)
        self.phoneNumText=QTextEdit()
        self.phoneNumText.setReadOnly(True)
        self.specialText=QTextEdit()
        self.specialText.setReadOnly(True)
        decideButton.clicked.connect(self.backButtonClicked)
        saveMenu.clicked.connect(self.saveButtonClicked)
        koreaFoodButton.clicked.connect(self.kBC)
        chineseFoodButton.clicked.connect(self.cBC)
        japaneseFoodButton.clicked.connect(self.jBC)
        meatFoodButton.clicked.connect(self.mBC)
        schoolFoodButton.clicked.connect(self.sFC)
        randomButton.clicked.connect(self.randomButtonClicked)

        ##LayoutBox 들을 생성 합니다.

        vbox_1=QVBoxLayout()
        hbox_2=QHBoxLayout()
        hbox_1_1=QHBoxLayout()
        hbox_1_2=QHBoxLayout()
        hbox_1_3=QHBoxLayout()
        vbox_2_1=QVBoxLayout()
        vbox_2_2=QVBoxLayout()
        vbox_2_3=QVBoxLayout()


        ##hbox_1과 hbox_2에 레이아웃을 집어 넣습니다.

        vbox_1.addLayout(hbox_1_1)
        vbox_1.addLayout(hbox_1_2)
        vbox_1.addLayout(hbox_1_3)
        hbox_2.addLayout(vbox_2_1)
        hbox_2.addLayout(vbox_2_2)
        hbox_2.addLayout(vbox_2_3)


        ##hbox_1안의 레이아웃에 위젯을 넣습니다.

        hbox_1_1.addStretch(1)
        hbox_1_1.addWidget(textMessage)
        hbox_1_1.addStretch(1)
        hbox_1_1.addWidget(saveMenu)
        hbox_1_2.addWidget(koreaFoodButton)
        hbox_1_2.addStretch(1)
        hbox_1_2.addWidget(chineseFoodButton)
        hbox_1_2.addStretch(1)
        hbox_1_2.addWidget(japaneseFoodButton)
        hbox_1_2.addStretch(1)
        hbox_1_2.addWidget(meatFoodButton)
        hbox_1_2.addStretch(1)
        hbox_1_2.addWidget(schoolFoodButton)
        hbox_1_2.addStretch(8)
        hbox_1_2.addWidget(randomButton)
        hbox_1_3.addStretch(1)
        hbox_1_3.addWidget(decideButton)

        ##hbox_2안의 레이아웃에 위젯을 넣습니다.

        vbox_2_1.addWidget(restaurantLabel)
        vbox_2_1.addWidget(self.restaurantText)
        vbox_2_2.addWidget(phoneNumberLabel)
        vbox_2_2.addWidget(self.phoneNumText)
        vbox_2_3.addWidget(specialLabel)
        vbox_2_3.addWidget(self.specialText)



        ##보여줄 레이아웃
        vbox=QVBoxLayout()
        vbox.addLayout(vbox_1)
        vbox.addLayout(hbox_2)
        self.setLayout(vbox)
        self.cate=""



    def backButtonClicked(self):
        self.hide()
        self.Layout_menu.show()

    def randomButtonClicked(self):
        self.category=random_category.randomCategory()
        self.category.randomAll()
        ##self.cate=
        self.restaurantText.setText(self.category.getrCg)

    def kBC(self):
        self.category=random_category.randomCategory()
        self.category.category_GUI("한식")
        self.cate="한식"
        self.restaurantText.setText(self.category.category_str)

    def cBC(self):
        self.category=random_category.randomCategory()
        self.category.category_GUI("중식")
        self.cate="중식"
        self.restaurantText.setText(self.category.category_str)

    def jBC(self):
        self.category=random_category.randomCategory()
        self.cate="일식"
        self.category.category_GUI("일식")
        self.restaurantText.setText(self.category.category_str)

    def mBC(self):
        self.cate="양식"
        self.category=random_category.randomCategory()
        self.category.category_GUI("양식")
        self.restaurantText.setText(self.category.category_str)

    def sFC(self):
        self.cate="학식"
        self.category=random_category.randomCategory()
        self.category.category_GUI("학식")
        self.restaurantText.setText(self.category.category_str)

    def keyPressEvent(self,e):
        if e.key()==Qt.Key_Escape:
            self.close()

    def saveButtonClicked(self):
        self.hide()
        self.Layout_save.show()
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
        self.menuText.setReadOnly(True)
        self.priceText=QTextEdit("")
        self.priceText.setReadOnly(True)
        self.specialText=QTextEdit("")
        self.specialText.setReadOnly(True)
        decideButton.clicked.connect(self.decideButtonClicked)
        backButton.clicked.connect(self.backButtonClicked)


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

    def backButtonClicked(self):
        self.hide()
        self.Layout_first=Layout_first()
        self.Layout_first.show()

    def decideButtonClicked(self):
        self.hide()
        self.Layout_save=Layout_save()
        self.Layout_save.show()


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    choiceMenu = Layout_first()
    choiceMenu.show()


    sys.exit(app.exec_())