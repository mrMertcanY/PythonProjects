class Animal():


    def __init__(self):
        print("hayvan sınıfı init çağırıldı.")

    def method1(self):
        print("hayvan sınıfı method1")

    def method2(self):
        print("hayvan sınıfı method2 çağırıldı")

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("kedi sınıfı init çağırıldı")
        
    def sayMeow(self):
        print("Miyav")

    #override
    def method1(self):
        print("kedi sınıfındaki method1 çağırıldı")

myAnimal = Animal()

myAnimal.method1()
myAnimal.method2()

myCat = Cat()

myCat.method1()
myCat.sayMeow()