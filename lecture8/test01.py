# list
my_list = ["nick",1,1,1,True,["hello",1]]
print(my_list)
print(len(my_list))

# tuple
my_tuple = ("nick",1,1,1,True,("hello",1))
print(my_tuple)
print(len(my_tuple))

# Set ไม่มึลำดับ ข้อมูลไม่ซ้ำกันแต่เขียนให้ซ้ำกันได้
my_set = {True,"nick",10,10,20,30}
print(my_set)
print(len(my_set))

for i in my_set :
    print(i, end = "/")
print("..................................")

listformset = list(my_set)
print(listformset)
listformset[0] ="DTI"
my_set = set(listformset)
print(my_set)

#set method
my_set.clear()
print(my_set)

my_set1 = {10,20,30,"Hi"}
my_set2 = {10,"Hello","Hi",True}

my_set1.add(999) 
print(my_set1)
my_set1.remove(999)
print(my_set1)

print(my_set1.intersection(my_set2))
print(my_set1.union(my_set2))

#set Function len,min,max
