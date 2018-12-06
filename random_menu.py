import random

class randomMenu:

    def __init__(self):
        fH = open("menu.dat")
        self.rdMenuDB = []
        for line in fH:
            dat = line.strip()
            menu = dat.split("\n")
            record={}
            for attr in menu:
                kv = attr.split(':')
                ls = kv[1].replace(',',' ').split()
                count = 0
                tupList = []
                for i in range(0,len(ls),3):
                    tup = (ls[i],ls[i+1],ls[i+2])
                    tupList.append(tup)
                kv[1] = tupList
                record[kv[0]] = kv[1]
                self.rdMenuDB +=[record]


    def randomMenu(self):
        randNum = random.randrange(len(self.rdMenuDB[0]['홍콩반점']))
        self.randomMenu = self.rdMenuDB[0]['홍콩반점'][randNum]

    def getRdmenuDB(self):
        return self.rdMenuDB

    def getRandomMenu(self):
        return self.randomMenu

if __name__ == '__main__':
    cg = randomMenu()
    print(cg.getRdmenuDB())
    cg.randomMenu()
    print(cg.getRandomMenu())