def calculate(operation, num1, num2):
    if operation == "+":
        return f"{num1} + {num2} = {num1+num2}"
    elif operation == "-":
        return f"{num1} - {num2} = {num1-num2}"
    elif operation == "/":
        return f"{num1} / {num2} = {num1/num2}"
    elif operation == "*":
        return f"{num1} * {num2} = {num1*num2}"


while True:
    try:
        n1 = input("1. Sayıyı Giriniz: ")
        o =  input("İşlem: ")
        n2 = input("2. Sayıyı Giriniz: ")

        if o in "+-/*":
            print(calculate(o, int(n1), int(n2)))

    except:
        print("Lütfen sayıları düzgün giriniz.")
