# nested list
b = [1, 2, 3, 4, 5]
a = [6, 7, 8, b]
print(a)  # [6, 7, 8, [1, 2, 3, 4, 5]]

# one method
c = [6, 7, 8, [1, 2, 3, 4, 5]]
print(c[-1][2])  # list vitra ko number=3


# Python Dictionaries
a = {
    "name": "hari",
    "address": "Nepal",
    "age": 12,
    "phone": [123, 456],
    "address": "Bhaktapur",
}
print(type(a))  # <class 'dict'>
print(a)  # {'name': 'hari', 'address': 'Bhaktapur', 'age': 12, 'phone': [123, 456]}
print(a["address"], a["age"]) # Bhaktapur 12
print(len(a))  # 4
print(a.keys())  # dict_keys(['name', 'address', 'age', 'phone'])
print(a.values())  # dict_values(['hari', 'Bhaktapur', 12, [123, 456]])

ok = "nmkfnofejwnlsnglknbg"
print(len(ok))  # 20
print(a["phone"][-1]) # 456

user_info= {
    "name":"Sudan" ,
    "age":22

}

# user_info["name"]="Hari" #update garcha
# user_info["phone"]=123
# print(user_info) # {'name': 'Hari', 'age': 22, 'phone': 123} #value change garne



user_info.update({
    "name":"Hari",
    "age":123,
    "phone":2470,
    "role":"teacher"
})

print(user_info) #{'name': 'Hari', 'age': 123, 'phone': 2470, 'role': 'teacher'} # update garne tarika

#data delete garne
# del
# pop
# popitem
# clear

data = {
    'name': 'Hari', 
    'age': 123, 
    'phone': 2470,
    'role': 'teacher'

}

# del data['age']
# print(data) #{'name': 'Hari', 'phone': 2470, 'role': 'teacher'}

data.pop("role")
print(data) #{'name': 'Hari', 'age': 123, 'phone': 2470}


data.popitem()
print(data) #{'name': 'Hari', 'age': 123}  removes last value

data.clear()
print(data) # The clear() method empties the dictionary


user_infor = {
    "name": "Hari",
    "age": 21,
    "phone": [
        {
            "type":"NTC",
            "num": 9845
        },
        {
            "type": "Ncell",
            "num" : 980
        },
    ],
    "role": "teacher"
}


#Hari NTC number is 9845
print(f"{user_infor['name']} {user_infor['phone'][0]['type']} number is {user_infor['phone'][0]['num']}")

#Hari Ncell number is 980
print(f"{user_infor['name']} {user_infor['phone'][1]['type']} number is {user_infor['phone'][1]['num']}")


user_info = {
    "name":"sudan",
    "address":{
        "temp":"dang",
        "per":"Imadol"
    }
}

print(user_info['address']['temp'])