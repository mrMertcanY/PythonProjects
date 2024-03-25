from random import randint
from random import shuffle

myList = list(range(0,15))

print(myList[randint(0,len(myList)-1)])

print("====================")


myNewList = list(range(0, 15))

shuffle(myNewList)
print(myNewList)
