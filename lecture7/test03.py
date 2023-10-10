# list Method
var1 = [10,20,"hello",True,[111,"wow"],"สมชาย"]

# append เพิ่มข้อมูลเป็นชุด
print(var1.append(["HI","Hey",999]))

# extend เพิ่มข้อมูลเป็นอันๆ
print(var1.extend([10,20,30]))

# remove เอาออก 1 ตัว (เจอตัวไหนก่อนก็เอาออกก่อน)
var1.remove("hello")
var1.remove(10)
print(var1)

var2 = [10,20,"Hello"]
#insert แทรกข้อมูลลงในตำแหน่งที่ต้องการ
print(var2.insert(2,"Hi"))

#pop เอาข้อมูลตัวสุดท้ายออก *ถ้าใส่ index จะเอาตัวนั้นออกแทน
print(var2.pop())
print(var2.pop(1))

#index แสดง index ของข้อมูล
print(var2.index("Hi"))

var3 = [10,10,10,"Hi",10,"Hi"]
#count นับจำนวนข้อมูลนั้นๆที่อยู่ใน list
print(f"ใน var3 มี 10 ทั้งหมด {var3.count(10)} ตัว")
print(f"ใน var3 มี Hi ทั้งหมด {var3.count('Hi')} ตัว")

var4 = [10,10,10,"Hi",10,"Hi"]
var5 = [2,67,13,64,3,35,]
#sort เรียงลำดับจากน้อยไปหามาก ใช้ได้แค่ข้อมูลประเภทเดียวกันเท่านั้นฃ
print(var5)
var5.sort()
print(var5)
var5.sort(reverse=True)
print(var5) 