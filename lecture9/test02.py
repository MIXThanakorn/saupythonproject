#constructer
#สร้าง object ที่มาจาก class เดียวกันแต่ไม่เหมือนกันบ้าง
class DTITest():
    infoA = 10
    #constructor คือตัวที่ทำให้ Object ที่สร้างจากแม่พิมพ์เดียวกันไม่จำเป็นต้องเหมือนกัน
    #constructor จะทำงานทุกครั้งที่มีการสร้าง Object
    def __init__(self,infoB,infoC):
        self.infoB = infoB
        self.infoC = infoC
        print("wow wow wow")

    #method
    def showinfo(self,mix):
        print(self.infoA + self.infoB + self.infoC + mix)

#สร้าง Object
sau1 = DTITest(20,30)
sau2 = DTITest(10,100)
sau3 = DTITest(20,30)

        