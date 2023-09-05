#function แบบที่ 1 - no parameter/no return

def FuncA():
    print("AAA")
    print("BBB")
    #ไม่มีคำสั่ง return
def FuncB():
    print("111")
    FuncA()

FuncA()
FuncB()