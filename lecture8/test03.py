#Object-Oriented Programming OOP
class DtiSau:
    #data/properties members ค่าข้อมูล
    stuname = " "
    score = 0
    GPA = 0
    #method members คือค่าของการทำงาน (เขียนแบบ function)
    #self เปรียบเสมือนสิ่งที่ใช้ใยชน class ตัวเอง เพื่อสามารถเรียกใช้ member ใน class ตัวเอง
    def HiStudent(self):
        print(f"สวัสดี {self.stuname}")
    def showgrade(self):
        print(f"คะแนน {self.score} ได้เกรด {self.GPA}")

#สร้าง object จาก class
obj01 = DtiSau() #ชื่อ class ที่มีวงเล็บเป็นการสั่งให้ contructor ของ class ทำงาน
obj02 = DtiSau()

#การเรียกใช้ ชื่อ object "." ถ้าตามด้วย data จะแก้ไขได้ ถ้าตามด้วย method จะเรียกใช้งาน
obj01.stuname = "สมชาย"
obj01.HiStudent()
obj01.stuname = "สมหญิง"
obj01.score = 99
obj01.GPA = "A"
obj01.HiStudent()
obj01.showgrade()