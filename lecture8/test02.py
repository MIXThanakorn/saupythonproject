my_list = ["nick",1,1,1,True,["hello",1]]
my_tuple = ("nick",1,1,1,True,("hello",1))
my_set = {True,"nick",10,10,20,30}

#dictionary >>> key:value/ key -> str/number / value -> everthing
my_dictionary = {"name":"nick", "age":20 , 555:999 , "flag":True}
print(my_dictionary["name"])
print(my_dictionary["age"] + my_dictionary["flag"])
my_dictionary["name"] = "kla"
print(my_dictionary["name"])

my_dictionary["major"] = "DTI"
print(my_dictionary)
#pop เอาข้อมูลออก
my_dictionary.pop("name")
my_dictionary.pop(555)
print(my_dictionary)
#popitem เอาข้อมูลตัวสุดท้ายออก
my_dictionary.popitem()
print(my_dictionary)



for data in my_dictionary:
    print(data,end = " ")
print(" ")
for data in my_dictionary.keys():
    print(data,end = " ")
print(" ")
for data in my_dictionary.values():
    print(data,end = " ")

my_dict = {"a":10 , "b":20 , "c":30}
my_dict1 = my_dict
my_dict2 = my_dict1.copy()

print()
print(my_dict1)
print(my_dict2)
my_dict["a"] = 999
my_dict2["a"] = 888
print("+++++++++++++++++")
print(my_dict)
print(my_dict1)
print(my_dict2)