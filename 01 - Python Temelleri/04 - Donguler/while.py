x = 0

while x < 10:
    print(x)
    x += 1


myList = [1,2,3,4,5]

print("==============")

while 3 in myList:
    myList.pop()
    print(myList)


print("=============")


newVariable = 0

while newVariable < 15:
    #print("Yeni değişkenin güncel değeri: "+str(newVariable))
    print(f"Yeni değişken'in güncel değeri: {newVariable}")
    newVariable += 1