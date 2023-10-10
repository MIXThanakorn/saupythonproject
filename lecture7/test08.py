#วิธีเปลี่ยนค่าข้อมูลใน tuple
var2 = (10,20,"hello",True,(111,"wow"),"สมชาย")

#list() #tuple()
varTemp = list(var2)
varTemp[2] = "Hi"
var2 = tuple(varTemp)
print(var2)