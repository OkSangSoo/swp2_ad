import pickle

list = [{'menu':"",'price':2000,'special':""},{'menu':"",'price':266,'special':""},{'menu':"",'price':266,'special':""},{'menu':"",'price':2666,'special':""},{'menu':"",'price':3464,'special':""}]

with open('menu2.dat','wb') as f:
    pickle.dump(list,f)