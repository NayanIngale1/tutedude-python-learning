'''

# Object oriented programing

# class - blue print
# objects - instance of class, created as many times as you want
# attributes - characteristics associated to a type / object
# methods - functions associated to a type / object

# syntax

# class (name):
#      statements and attributes
#      ...

# call the class
# statememts

class car:
    color = 'black'
    type = 'SUV'

    def name(self):
        return f'This car is {self.type} with {self.color}'


car_1 = car()

print(car_1.color)
print(car_1.name())


class const_dest:
    x = 0

    def __init__(self, color, type):
        self.color = color
        self.type = type
        print('constructed')

    def __del__(self):
        print('destructed')


cd = const_dest('Red', 'SUV')
print(cd.color)
print(cd.type)


# base class
class name:
    points = 0
    name = ''

    def __init__(self, z):
        self.name = z
        print(f'Hi {self.name}')

# sub class or derived class


class football_fans(name):

    def pts(self):
        print(self.name, 'score')


player = football_fans('Jim')
player.pts()


# TYPES OF INHERITACE

# single type inheritance
# multi-level inheritance
# multiple inheritance


# 1. Single level inheritance
class A:

    def state_1(self):
        print('State 1 present')

    def state_2(self):
        print('State 2 present')

    def state_3(self):
        print('State 3 present')


class B(A):

    def state_4(self):
        print('State 4 present')

    def state_5(self):
        print('State 5 present')


# a = A()
# a.state_1()
# a.state_2()

# b = B()
# b.state_4()
# b.state_3()

# multi-level inheritace
class C(B):
    
    def state_6(self):
        print('State 6 present')

# c = C()
# c.state_1()
# c.state_6()


# multiple inheritance


class D:

    def state_7(self):
        print('State 7 present')
        
class E(D,A):
    def state_8(self):
        print('State 8 present')
    
# e = E()
# e.state_3()
# e.state_7()

'''
