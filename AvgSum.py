import random

def avg():
    MyArray = []
    for i in range(10):
        i += 1
        MyArray.append(random.randint(1, 100))
    print(MyArray)

avg()