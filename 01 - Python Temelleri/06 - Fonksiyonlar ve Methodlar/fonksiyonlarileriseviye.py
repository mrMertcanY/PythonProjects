## args & kwargs


def summarize(*args):
    return sum(args)


print(summarize(10, 20, 30, 40, 50, 60, 70, 90))


print("=======")


def exampleFunc(**kwargs):
    print(kwargs)


exampleFunc(muz = 100, elma = 200, ananas = 300)
