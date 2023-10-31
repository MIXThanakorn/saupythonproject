#Destructor
class DTITest04():
    data1 = 10

    def __init__(self,data2) :
        self.data2 = data2
        print('Hi...')
    def task1(self):
        print("^_^")
    def task2(self,value):
        print(value)
    #Destructor ทำงานทุกครั้งที่ Object ทำงานเสร็จทุกครั้ง
    def __del__(self):
        print("Bye bye....")
#..........................................

sauA = DTITest04(20)
sauB = DTITest04(20)
sauC = DTITest04(20)

sauC.task2("T_T")
sauC.task1()
print(sauA.data1 + sauB.data1)