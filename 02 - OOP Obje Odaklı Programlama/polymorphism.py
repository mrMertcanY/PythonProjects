class Apple:
    def __init__(self, name):
        self.name = name

    def giveInfo(self):
        return self.name + " 100 kaloridir"

class Banana:
    def __init__(self, name):
        self.name = name

    def giveInfo(self):
        return self.name + " 150 kaloridir"


def takeInfo(fruit):
    print(fruit.giveInfo())



apple = Apple("elma")
banana = Banana("muz")


fruitList = [apple,banana]

takeInfo(banana)

for fruit in fruitList:
    print(fruit.giveInfo())
