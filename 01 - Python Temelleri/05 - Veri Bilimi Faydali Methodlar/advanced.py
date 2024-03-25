meals = ["muz", "ananas", "elma"]
calories = [100, 200, 300]
day = ["pazartesi", "salı", "çarşamba"]

print(list(zip(meals, calories, day)))


print("============")

# exampleList = []
# myList = "Mertcan Eligüzel"
# for char in myList:
#     exampleList.append(char)

myStr = "mertcan eligüzel"
newList = [item for item in myStr]


print(newList)

print("=========")


otherlist = [num ** 2 for num in list(range(0,10))]

print(otherlist)