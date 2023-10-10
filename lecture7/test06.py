#slicing data 
var1 = [10,20,"hello",True,[111,"wow"],"สมชาย"]
var2 = (10,20,"hello",True,(111,"wow"),"สมชาย")

#20 hello True
print(var1[1:4])

#True, (111, 'wow')
print(var2[3:5])

#10, 20, 'hello' 
print(var1[:3]) #ทำตั้งแต่ตัวแรกไม่ต้องใส่ตัวแรก

#'hello', True, [111, 'wow'], 'สมชาย'
print(var1[2:]) #ทำถึงตัวสุดท้ายไม่ต้องใส่ตัวสุดท้าย

