# type func

# a = input("Enter the 1st value..")
# b = input("Enter the 2nd value..")
# print(a+b)

# print("the value of a is", a)

# a = "123"
# print("after type casting", type(a))


name = "Suman"
age = 14
address = "Dang"
""
# output
"My name is Suman and age is 14 and address is Dang"


# name = input ("enter your name")
# age = input ("enter your age")
# address = input ("enter your address")

# output = ("My name is ", name , "and age is", age , "and address is", address)


output = f"My name is {name} and age is {age} and address is {address}"
print(output)


# if  (1==2):
#     print("this is true condition")


# if ("test"!="hello"):
#     print("this is str condition")
# else:
#     print("this is else conditon")


percentage = float(input("Enter your percentage: "))

if (percentage <= 0) or (percentage > 100):
    print("invalid percentage")
elif percentage >= 80:
    print("Distinction")
elif percentage >= 70:
    print("First Division")
elif percentage >= 60:
    print("Second Division")
elif percentage >= 50:
    print("Third Division")
elif percentage >= 30:
    print("Fourth Division")
else:
    print("fail")


gender = "F"

if gender == "F":
    print("Female")
else:
    print("Male")

data = "Female" if gender == "F" else "Male"
