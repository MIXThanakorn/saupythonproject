#function แบบที่ 2 - Have parameters/no return
#parameter คือตัวแปรประเภทฆนึ่ง เอาไว้รับค่ามาใช้เฉพาะในฟังก์ชั่นนั่นๆ เท่านั้น

def funcA(x,y):
    print(f"x is {x}")
    print(f"y is {y}")
    print(f"Sum {x} + {y} = {x+y} ")

funcA(5,6) #call function ข้อมูลที่ส่งให้ parameter เรียกว่า argument
funcA(10,90)
print("DTI....")
funcA(50,12)
