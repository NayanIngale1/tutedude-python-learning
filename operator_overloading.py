# operator overloading

# a = 1
# b = 2

# print(a+b)
# print(int.__add__(a, b), '<----by int class add method')


class vegetables:
    def __init__(self, carrot, beans):
        self.carrot = carrot
        self.beans = beans

    # ( + / addition ) operator overloading
    def __add__(self, other):
        carrot = self.carrot + other.carrot
        beans = self.beans + other.beans
        return vegetables(carrot, beans)


v1 = vegetables(5, 4)
v2 = vegetables(7, 3)
v3 = v1 + v2  # this operation handled by __add__ function in vegetables class
print(v3.carrot)
print(v3.beans)
