class Dog():
   
    multiplier = 7

    def __init__(self, age=0):
        self.age = age
        self.HumanAgeAttribute = age * 7

    def humanAgeCalc(self):
        return self.age * Dog.multiplier



myDog = Dog(3)

print(myDog.humanAgeCalc())
print(myDog.HumanAgeAttribute)