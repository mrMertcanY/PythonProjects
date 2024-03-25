class Fruit:
    def __init__(self, isim, kalori):
        self.isim = isim
        self.kalori = kalori

    def __str__(self):
        return f"{self.isim} şu kadar kaloriye sahiptir: {self.kalori}"
    
    def __len__(self):
        return self.kalori


banana = Fruit("muz", 150)

print(banana)
print(len(banana))
