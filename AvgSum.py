import random


def AvgSum():
    MyArray = []
    for i in range(10):
        i += 1
        MyArray.append(random.randint(1, 100))
    SumArray = sum(MyArray)
    AvgArray = sum(MyArray) / len(MyArray)
    print(AvgArray)
    print(SumArray)

AvgSum()