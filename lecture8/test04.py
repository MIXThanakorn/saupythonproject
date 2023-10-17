class Test04:
    #data
    data1 = 10
    #constructor
    def __init__(self,data2,data3):
        print("Hi")
        self.data2 = data2
        self.data3 = data3
    #method     
    def show(self):
        print(self.data1 + self.data2 + self.data3 )  
        self.show2()
    def show2(self):
        print("wow wow wow")

objA = Test04(10,20) 
objB = Test04(0,10) 
objC = Test04(100,122) 
objD = Test04(10,20)