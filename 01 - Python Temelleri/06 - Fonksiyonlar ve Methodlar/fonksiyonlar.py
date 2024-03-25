myName = "Mertcan Eligüzel"


def firstFunction():
    print("first function")


firstFunction()

print("=====================")


def hello(name = "Ziyaretçi"):
    print(f"Merhaba {name}")


hello(input("Bir isim girin: "))


print("=====================")


def returnSum(num1, num2):
    return num1+num2


print(returnSum(3,4))