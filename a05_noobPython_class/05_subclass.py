
class Parent(object):
    parentAttr = 100

    def __init__(self):
        print('use Parent init')

    def parentMethod(self):
        print('use Parent funciton')

    def setAttr(self,attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print('Parent attr: ',Parent.parentAttr)

    def myMethod(self):
        print('use Parent function')

class Child(Parent):
    def __init__(self):
        print('use child init')

    def childMethod(self):
        print('use child funtion')

    def myMethod(self):
        print('use child funtion')

c = Child()

c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()
c.myMethod()