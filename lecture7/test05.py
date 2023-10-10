#list function/tuple function
var1 = [10,20,"hello",True,[111,"wow"],"สมชาย"]
var2 = (10,20,"hello",True,(111,"wow"),"สมชาย")
#len() นับจำนวนโดยไม่สนว่าจะเป็นข้อมูลชนิดเดียวกันไหม 
print(f"ใน var1 มีข้อมูลทั้งหมด {len(var1)} ตัว")
print(f"ใน var2 มีข้อมูลทั้งหมด {len(var2)} ตัว")

var3 = [10,20,30,True,10,20] #True = 1 false = 0
var4 = (10,20,30,True,10,20)
#min() ข้อมูลที่มีค่าน้อยทีุ่สด ใช้ได้กับข้อมูลประเภทเดียวกันเท่านั้น
print(min(var3))
print(min(var4))

#max() ข้อมูลที่มีค่ามากทีุ่สด ใช้ได้กับข้อมูลประเภทเดียวกันเท่านั้น
print(max(var3))
print(max(var4))