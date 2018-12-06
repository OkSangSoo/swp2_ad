import random

class randomMenu:

    def __init__(self):
        fH = open("menu.dat")
        self.mndb = []
        for line in fH:
            dat = line.strip()
            menu = dat.split("\n")
            record={}
            for attr in menu:
                kv = attr.split(':')
                ls = kv[1].split(',')
                kv[1] = ls
                record[kv[0]] = kv[1]
                self.mndb +=[record]

    def getCgdb(self):
        return self.mndb

if __name__ == '__main__':
    cg = randomMenu()
    print(cg.getCgdb())
    print(cg.getCgdb()[0])