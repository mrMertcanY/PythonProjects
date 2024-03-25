myName = "Mertcan"
# Global

def MyFunc():
    myName = "Deneme"
    # Enclosing
    def InnerMyFunc():
        myName = "Denedik"
        #Local
        print(myName)
    InnerMyFunc()

MyFunc()


