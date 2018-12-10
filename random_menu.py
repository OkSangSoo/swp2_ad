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
                tupList = []
                for i in range(0,len(ls),3):
                    tup = (ls[i],ls[i+1],ls[i+2])
                    tupList.append(tup)
                kv[1] = tupList
                record[kv[0]] = kv[1]
                self.rdMenuDB +=[record]

        self.save_restaurant = ''

    def dictKeys(self):
        self.keys = []
        for i in self.rdMenuDB:
            self.keys.append(list(i.keys())[0])

    def findIdx(self, restaurant):
        for i in self.keys:
            if i == restaurant:
                self.Idx = self.keys.index(restaurant)

    def Finder(self,restaurant):
        self.dictKeys()
        self.findIdx(restaurant)
        return self.Idx

    def randomMenu(self, restaurant):
        randNum = random.randrange(len(self.rdMenuDB[self.Finder(restaurant)][restaurant]))
        self.randomMenu = self.rdMenuDB[self.Finder(restaurant)][restaurant][randNum]


    def menu_GUI(self,restaurant):
        str_menu = ''
        str_price = ''
        str_etc = ''
        self.str_list = [[str_menu,0],[str_price,1],[str_etc,2]]
        print(self.rdMenuDB)
        for i in self.str_list:
            for j in range (len(self.rdMenuDB[self.Finder(restaurant)][restaurant])):
                i[0] += self.rdMenuDB[self.Finder(restaurant)][restaurant][j][i[1]] +'\n'

    def selectMenu(self,restaurant,menu):
        restaurant = list(self.rdMenuDB[self.Finder(restaurant)].keys())[0]
        for i in self.getMenus(restaurant):
            if i[0]==menu:
                self.chosenMenu = i
        self.cart.append((restaurant,self.chosenMenu[0],self.chosenMenu[1]))

    def cart_GUI(self):
        str_cartrestaurant = ''
        str_cartmenu = ''
        str_cartprice = ''
        self.cart_list = [[str_cartrestaurant,0],[str_cartmenu,1],[str_cartprice,2]]
        for i in self.cart_list:
            for j in range(len(self.cart)):
                i[0] += self.cart[j][i[1]]

    def getMenus(self,restaurant):
        return self.rdMenuDB[self.Finder(restaurant)][restaurant]

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

    def getStrCRes(self):
        return self.cart_list[0][0]

    def getStrCMenu(self):
        return self.cart_list[1][0]

    def getStrCPrice(self):
        return self.cart_list[2][0]

if __name__ == '__main__':
    rm = randomMenu()
    print(rm.getRdmenuDB())
    restaurant = '송강루'
    rm.randomMenu(restaurant)
    print(rm.getRandomMenu())
    rm.menu_GUI(restaurant)
    print(rm.getMenus(restaurant))

    print(rm.getStrMenu())
    print(rm.getStrPrice())
    print(rm.getStrEtc())
    rm.selectMenu(restaurant,'등심탕수육')
    print(rm.getChosenMenu())
