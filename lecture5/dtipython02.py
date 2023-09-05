#function แบบที่ 2 - Have parameters/no return
#parameter คือตัวแปรประเภทฆนึ่ง เอาไว้รับค่ามาใช้เฉพาะในฟังก์ชั่นนั่นๆ เท่านั้น
#ข้อมูลที่ส่งให้ parameter เรียกว่า argument
def FuncA(x,y):
    print("AAA")
    z = x + y
    print(z)

def FuncD(x,y,z):
   print("{:.2f} {:.4f} {:.5f}".format(x,y,z))

FuncA(5,10)
FuncD(10,20,30)

