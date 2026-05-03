class Parent1():
    a = 10
    b = 20

class Parent2():
    c = 30
    d = 40

class Child(Parent1, Parent2):
    a = 50

obj = Child()
print(obj.a)  # Output: 50 (Child's own attribute)
print(Child.__mro__)  # Output: (<class '__main__.Child'>, <class '__main__.Parent1'>, <class '__main__.Parent2'>, <class 'object'>)



#Lambda Function

data = lambda x,y : x+y
print (data(1,2))  # Output: 3

data = [1,2,3,4,5]
a= [i**2 for i in data]
print(a)  # Output: [1, 4, 9, 16, 25]


square = lambda *args : [i**2 for i in args]

print(square(1,2,3,4,5))  # Output: [1, 4, 9, 16, 25]
print(square(15,26))  # Output: [225, 676]