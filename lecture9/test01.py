class DTITest01:
    pass

class DTITest02:
    #data/attribute
    infoA = " "
    infoB = 20

    #method คือ Function ประเภทนึง
    def ShowHi(self):
        print("Hi...")

    def ShowInfo(self):
        print(self.infoA)
        print(self.infoB)
        
#สรัาง Object
objA = DTITest02()
objB = DTITest02()
Sombut = DTITest02()

#ใช้งาน Object
objA.infoA = "xxx"
objB.infoB = 100
print(objA.infoB + objB.infoB)
Sombut.ShowInfo()