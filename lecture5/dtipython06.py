#คำสั่ง return ที่ไม่มีอะไรต่อท้าย หมายถึง บ่งบอกว่าการทำงานนั้นเสร็จแล้ว
def example1():
    print(111)
    print(222)
    return
    print(333)
    print(444)
    return

#Default parameters มีการกำหนดค่าเริ่มต้นให้กับ parameters
def dtitest(x = 99, y = 0 ,z = 20, a = 10):
    print(f"{x} + {y} + {z} + {a} = {x+y+z+a}")

dtitest(5, 10)

dtitest(5, 10, 20)