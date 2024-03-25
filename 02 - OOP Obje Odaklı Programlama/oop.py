class SuperKahraman:

    ozelGuc = "Görünmezlik"

    def __init__(self, name, age, job):
        print("init çağırıldı")
        self.name = name
        self.age = age
        self.job = job

    def ornekMethod(self):
        print(f"ben süperkahramanım ve mesleğim: {self.job}")


superman = SuperKahraman("Superman", 30, "Gazeteci")

superman.ozelGuc = "Uçabiliyor"
print(superman.ozelGuc)

superman.ornekMethod()