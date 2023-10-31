#คุณสมบัติ Inheritance สืบทอด คือ การที่ class นึง สือบทอดอีกคลาสนึง reuse
#สืบทอด มีแม่ (super class) มีลูก (sub class)

#คุณสมบัติ polymorphism (พ้องรูป,พฤติกรรมเดียวกันแต่วิธีการต่างกัน)  คือการที่ class ลูกเอา method ของ class แม่มาเขียนใหม่
class Sau1:
    infoA = 10

    def showhi():
        print("Hi...")

class Sau2(Sau1):
    infoB = 20

    def showhey():
        print("Hey...")

    #overiding method : polymorphism
    def showhi():
        print("Hi Hi Hi ...")

ob1 = Sau1()
ob2 = Sau2()
ob2.showhi()