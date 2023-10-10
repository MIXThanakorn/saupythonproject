#list ***แก้ไขข้อมูลด้านในได้
#        0  1    2      3       4        5
var1 = [10,20,"hello",True,[111,"wow"],"สมชาย"]
#       -6 -5    -4     -3     -2       -1 
print(var1[0] + var1[1])
print(var1[-6] + var1[-5])
#list in list ใช้ [] เพิ่ม
print(var1[0] + var1[4][0])
print(var1[-6] + var1[-2][-2])
print(f"{var1[2]}...{var1[5]} {var1[4][1]}...")


#tuple ***แก้ไขข้อมูลด้านในไม่ได้
var2 = (10,20,"hello",True,(111,"wow"),"สมชาย")
print(var2[0] + var2[1])
print(var2[-6] + var2[-5])
print(var2[0] + var2[4][0])
print(var2[-6] + var2[-2][-2])
print(f"{var2[2]}...{var2[5]} {var2[4][1]}...")