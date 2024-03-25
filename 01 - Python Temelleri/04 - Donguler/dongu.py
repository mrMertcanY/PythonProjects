# myList = [10,20,30,40,50]


# for number in myList:
#     print(number)


myList = [1, 2, 3, 4, 5, 6]

for num in myList:
    if num % 2 == 0:
        print(num)

print("===========")
coordinateList = [(10.2, 15.2), (32.4, 16.2), (40.2, 20.2)]

for x, y in coordinateList:
    print(x)

print("===========")
myDictionary = {"muz": 150, "portakal": 250, "elma": 400}
for (key,value) in myDictionary.items():
    print(value)
