
#  1-Abstraction
#  2- Polymorphism
#  3- Encapsulation
#  4- Inheritance

# class c_name:
#     def __init__(self,f,m,l):
#         self.f=f
#         self.m=m
#         self.l=l
# name=c_name("zeel", "rajiv", "gandhi")
# print (name)


class parent: #base class
    def name(self):
        print ("I am your mother")

class children(parent): #inherit
    def c_name(self):
        print ("I am your daughter")

d=children()
d.c_name()
d.name()
