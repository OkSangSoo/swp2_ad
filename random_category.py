import random

class randomCategory:

    def __init__(self):
        fH = open("category.dat")
        self.cgdb = []
        for line in fH:
            dat = line.strip()
            category = dat.split("\n")
            record={}
            for attr in category:
                kv = attr.split(':')
                ls = kv[1].split(',')
                kv[1] = ls
                record[kv[0]] = kv[1]
                self.cgdb +=[record]

    def randomBigC(self):
        rdBC = random.randrange(len(self.cgdb))
        self.rCg = self.cgdb[rdBC]

    def randomShop(self):
        rdidx = list(self.rCg.keys())[0]
        rdlist = self.rCg[rdidx]
        rdS = random.randrange(len(rdlist))
        self.rdShop = rdlist[rdS]

    def randomAll(self):
        self.randomBigC()
        self.randomShop()

    def chooseCategory(self,category):
        self.returns = []
        if category == '중식':
            self.returns = self.cgdb[0][category]
        if category == '일식':
            self.returns = self.cgdb[1][category]
        if category == '학식':
            self.returns = self.cgdb[2][category]
        if category == '양식':
            self.returns = self.cgdb[3][category]
        if category == '한식':
            self.returns = self.cgdb[4][category]

    def category_GUI(self, category):
        self.category_str = ''
        self.chooseCategory(category)
        restaurants = self.getChosen()
        for i in range(len(restaurants)):
            self.category_str += restaurants[i] +'\n'

    def random_GUI(self):
        self.randomBigC()
        Cate = self.getrCg()
        Cate_key = list(Cate.keys())[0]
        rdCate = Cate[Cate_key]
        rdidx = random.randrange(len(rdCate))
        self.randomRestaurant = rdCate[rdidx]
        self.rdCategory_str = ''
        for i in rdCate:
            self.rdCategory_str += i +'\n'

    def getCgdb(self):
        return self.cgdb

    def getrCg(self):
        return self.rCg

    def getrdShop(self):
        return self.rdShop

    def getChosen(self):
        return self.returns

    def categoryGUI(self):
        return self.category_str

    def randomGUI(self):
        return self.rdCategory_str

    def randomGUI_getRandomRestaurant(self):
        return self.randomRestaurant

if __name__ == '__main__':
    cg = randomCategory()
    print(cg.getCgdb())
    print(cg.getCgdb()[0]['중식'][1])
    s=cg.randomAll()
    print(cg.getrCg())
    print(cg.getrdShop())
    category = '한식'
    cg.category_GUI(category)
    print(cg.categoryGUI())
    cg.random_GUI()
    print(cg.randomGUI())