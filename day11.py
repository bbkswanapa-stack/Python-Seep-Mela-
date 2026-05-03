def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))


class Person:
    a = 10
    b = 1000


data = Person()
print(data.a)
print(data.b)
data.door = "main door"
print(data.door)

data2 = Person()
print(data2.a)
print(data2.b)
# print(data2.door)

del data2


class Test:
    a = 200
    b = 150

    def add(self):              #method 1
        return self.a + self.b
    
    def sub(self):              #method 2
        return self.a - self.b
    
    def result(self):           #method 3
        return self.add(), self.sub()



obj1 = Test()
print(obj1.a)
print(obj1.add())
print(obj1.sub())
print(obj1.result())


class Student:
    name = "ram"
    marks = [20,60,50,90,60]

    def result(self):
        avg = sum(self.marks) / len(self.marks)

        if avg >= 80:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 40:
            return "C"
        else:
            return "Fail"

grade = Student()
print(grade.result())
