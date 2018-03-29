dic1= {1:'a', 2:'b'}
dic2= {3: 'c', 4:'d'}
dic3= {5:'e', 6:'f'}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

#OR:
dic1= {1:'a', 2:'b'}
dic2= {3: 'c', 4:'d'}
dic3= {5:'e', 6:'f'}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
