#คุณสมบัติ Encapsulation (ห่อหุ้ม data)
class DTITest05 :
    infoA = 10
    __infoB = 20 #Encap ดูจาก __ เป็นการกำหนด access modifier เป็น private

    def __init__(self, infoC , infoD):
        self.infoC = infoC
        self.__infoD = infoD

#เมื่อใดก็ตามที่ encap ต้องมี method 2 ตัวนี้เสมอ คือ get , set ของ data ตัวนั้นๆ
    def setinfoB(self,infoB): #set คือการกำหนดค่า
        self.__infoB = infoB

    def getinfoB(self,infoB):#get คือการนำค่าไปใช้
        return self.__infoB

    def setinfoD(self,infoD):
        self.__infoD = infoD

    def getinfoB(self,infoD):
        return self.__infoD

    def showinfo(self):
        print(self.infoA)
        print(self.__infoB)
        print(self.infoC)
        print(self.__infoD)
        print("..............")

ob1 = DTITest05(30,40)
ob2 = DTITest05(30,100)
ob1.showinfo()
ob1.__infoB = 999
ob1.showinfo()
ob1.infoA = 555
ob1.showinfo()