def bolme(num):
    return num / 2


print(bolme(20))

mylist = list(range(1, 11))


# for item in mylist:
#     newlist.append(bolme(item))

# print(newlist)


newlist = list(map(bolme, mylist))

print(newlist)


stringList = ["mertcan", "felen", "deneme", "ahmet", "gibi"]


def strControl(s):
    return "a" in s



print(list(map(strControl, stringList)))


print("=====================")



print(list(filter(strControl, stringList)))


print("==================")



carpma = lambda numara : numara * 3


print(carpma(10))

print(list(map(lambda num : num * 3, mylist)))