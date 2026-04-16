list1 = [1,2,2,4,5,6,6]
print(list1)

print(list1[-5])
# print(type(list1))
# print(list1[-80])
print(len(list1))


list5 = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]

print(isinstance(list5[-1], float)) #True
print(isinstance(list5[1], int)) #True
print(isinstance(list5[0], str)) #True

#Slicing
print(list5[0:4]) #['apple', 54, 71.3, False]
print(list5[3:]) #[False, 'Orange', True, 21, 13.8]
print(list5[-3:]) #[True, 21, 13.8]

#Data Adding Method

#append
#insert
#extends
#concat
#index

#append
data= [2,3,4,5,6]
data.append(1)
print(data) #[2, 3, 4, 5, 6, 1]


#insert
data2 = ["apple", 54, 71.3, False, "Orange", True, 21, 13.8]
data2.insert(5,"iphone")
print(data2) #['apple', 54, 71.3, False, 'Orange', 'iphone', True, 21, 13.8]

#extends
a = [1,2,3,4,5]
b = [6,7]
b.extend(a)
print(b) #[6, 7, 1, 2, 3, 4, 5]

a.extend(b)
print(a) #[1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5]


#concat
d = [1,2]
e = [4,5]

f = d+e
print(f) #[1, 2, 4, 5]
print(d, e) #[1, 2] [4, 5]

#index
data6 = ["hello", 2, 2.5 , "old"]
data6[1]= "new"
print(data6) #['hello', 'new', 2.5, 'old']

#Data remove garne tarika
# del
# remove
# pop
# clear

#del
data2 = ["apple", 54, 71.3, False, "Orange", True, 21, 71.3, 13.8]
del data2[0]
print(data2) #[54, 71.3, False, 'Orange', True, 21, 13.8]
#entire varaible udauna milxa

#remove
data2.remove(71.3) #[54, False, 'Orange', True, 21, 71.3, 13.8]
data2.remove(71.3) #[54, False, 'Orange', True, 21, 13.8] duitai remove garna lai
print(data2)

#pop
data2.pop()
print(data2) #[54, False, 'Orange', True, 21] #kei index rakhena vane last ko udauxa 
#data recover garnu milxa 


#clear
# The clear() method remove all the elements from the list
teachers = ['Nasir', 'Irfan', 'Haris', 'Sheraz', 'Farhan', 'Khalil','Haris', 'Ihsan']
teachers.clear()
print(teachers) #[]





