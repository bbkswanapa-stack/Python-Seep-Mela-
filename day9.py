#keyword argument

# def user_info(fname, lname, age):
#     return f'my name is {fname} {lname} and age is {age}'

# print(user_info("sudan", 12, "bhandari"))

# print(user_info(fname="sudan",age=12, lname="bhandari")) #my name is sudan bhandari and age is 12




# def sum_number(*num):  
#     print(num)
#     print(type(num))

# sum_number(1)
# sum_number(1,2,3)
# sum_number()


# def sum_number(*num):   
#     print(len(num))
#     total = 0
#     if len(num)>1:
#         for i in num:
#             total += i
#         return f"Total sum = {total}"
#     else:
#         return "len must be  more than 1"
       
    

# print(sum_number(1))
# print(sum_number(1,2,3))
# print(sum_number())


# sum_number(1,"test",123,124512,"test")

# def sum_number(*num):
#     total = 0
#     for i in num:
#         if isinstance(i, int):
#          total += i
#     return f"total sum = {total}"

# print(sum_number(1,"test", 123 , 124512,"test"))




def per(**data):
    

    if "eng" not in data or "nep" not in data or "math" not in data:
        print("error")
        
    else:
        print("eng", data['eng'])
        print("nep", data['nep'])
        print("math", data['math'])
    
per(eng=100, nep=12, math=1)
per(eng=100, nep=13)


