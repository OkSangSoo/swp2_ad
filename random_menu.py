import random

class randomMenu:

    def __init__(self):
        fH = open("menu.dat")
        self.rdMenuDB = []
        self.cart = []
        for line in fH:
            dat = line.strip()
            menu = dat.split("\n")
            record={}
            for attr in menu:
                kv = attr.split(':')
                ls = kv[1].replace(',',' ').split()
                count = 0
                tupList = []
                print(ls)
                for i in range(0,len(ls),3):
                    tup = (ls[i],ls[i+1],ls[i+2])
                    tupList.append(tup)
                kv[1] = tupList
                record[kv[0]] = kv[1]
                self.rdMenuDB +=[record]


    def randomMenu(self, restaurant):
        randNum = random.randrange(len(self.rdMenuDB[0][restaurant]))
        self.randomMenu = self.rdMenuDB[0][restaurant][randNum]

    def menu_GUI(self,restaurant):
        str_menu = ''
        str_price = ''
        str_etc = ''
        self.str_list = [[str_menu,0],[str_price,1],[str_etc,2]]
        for i in self.str_list:
            for j in range (len(self.rdMenuDB[0][restaurant])):
                i[0] += self.rdMenuDB[0][restaurant][j][i[1]] +'\n'

    def selectMenu(self,menu):
        restaurant = list(self.rdMenuDB[0].keys())[0]
        for i in self.getMenus(restaurant):
            if i[0]==menu:
                self.chosenMenu = i
        self.cart.append((restaurant,self.chosenMenu[0],self.chosenMenu[1]))

    def getMenus(self,restaurant):
        return self.rdMenuDB[0][restaurant]

    def getRdmenuDB(self):
        return self.rdMenuDB

    def getRandomMenu(self):
        return self.randomMenu

    def getChosenMenu(self):
        return self.cart

    def getMenuGUI(self):
        return self.str_list

    def getStrMenu(self):
        return self.str_list[0][0]

    def getStrPrice(self):
        return self.str_list[1][0]

    def getStrEtc(self):
        return self.str_list[2][0]

if __name__ == '__main__':
    rm = randomMenu()
    print(rm.getRdmenuDB())
    restaurant = '홍콩반점'
    rm.randomMenu(restaurant)
    print(rm.getRandomMenu())
    rm.menu_GUI(restaurant)

    print(rm.getStrMenu())
    print(rm.getStrPrice())
    print(rm.getStrEtc())
    rm.selectMenu('자장면')
    print(rm.getChosenMenu())