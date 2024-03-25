x = 3
y = 4

if x > y:
    print("x > y")
elif y > x:
    print("y > x")
else:
    print("x == y")


## AND , OR , NOT gibi ifadeler kullanılabilir. In de kullanılır.


myString = "Mertcan Eligüzel"

if "M" in myString:
    print("vaaaar")

myNumList = [10, 20, 30, 40]

if 10 in myNumList:
    print("10 var")


myDictionary = {
    "muz": 100,
    "elma": 200,
    "armut": 300
}

if "muz" in myDictionary.keys():
    print("muz var mydict içinde keylerde")
