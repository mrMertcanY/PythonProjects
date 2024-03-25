## key - value pairing (anahtar kelime - değer eşleşmesi)

myDictionary = {
    "elma": 100,
    "karpuz": 200,
    "muz": 300
}


print(myDictionary["elma"])

newDictionary = {
    "anahtar1" : 100,
    "anahtar2": [10,20,30,40,4.5,"mertcan"],
    "anahtar3": {
        "anahtar9": 4,
        "anahtar10": {"anahtar4":3}
    }
}


print(newDictionary.keys())

print(newDictionary.values())

print(newDictionary["anahtar3"]["anahtar9"])
