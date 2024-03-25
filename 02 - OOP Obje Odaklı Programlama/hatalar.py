# ERROR HANDLING


while True:
    try:
        myInt = int(input("Numaranızı giriniz:"))
    except:
        print("Lütfen gerçekten numara giriniz")
        continue
    else:
        print("Teşekkürler") 
        break
    finally:
        print("finally çağırıldı")