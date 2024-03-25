myList = [10, 20, 30, 40]

print(myList[0])

myList.append(50) ## diziye 50 sayısını ekler

print(myList)


myList.pop() ## son indexi atar. 

print(myList)

myList.remove(40) ## içindeki değeri çıkartır

print(myList)


print(myList.count(20)) ## içine verdiğimiz değerden listenin içinde kaç tane olduğunu sayar

myStrList = ["Mertcan", "Deneme", "Falan"]
myOtherStrList = ["Diğer", "Olur", "Olmaz"]

print(myStrList + myOtherStrList) ## İki listeyi toplar - eğer bir listenin yanıa * 5 yazarsak => 5 kere yazdırır

myStrList.reverse()
print(myStrList) ## Tersten yazdırır

karisikListe = [1,2,3.5,"mertcan",9]

nestedList = [1,5,"mertcan",4,[6,"z"]]

nestedListValue = nestedList[4][1]
print(nestedListValue)
