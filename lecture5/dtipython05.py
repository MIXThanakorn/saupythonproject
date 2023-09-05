#จำนวนเงินที่จะแชร์กัน ป้อนเงิน ป้อนเงิน แล้วคำนวนและแสดงเงินที่ใช้ได้ทางหน้าจอ
#โดยเขียนเป็นฟังค์ชั่น 2 ฟังค์ชั่น

#รับค่า
def InputMoneyPerson():
    money = float(input("ป้อนจำนวนเงิน: "))
    person = int(input("ป้อนคน: "))
    return money, person

#คำนวน
def calculate(money,person):
    #เงินทศนิยม 2 ตำแหน่ง แชร์กันปัดขึ้น
    print(f"จำนวนเงิน {float(money):.2f} บาท คน {person} คน แชร์กันคนละ {round(float(money/person))} บาท")
    print("จำนวนเงิน" , format(float(money),'.2f') ,"บาท","คน",person,"คน","แชร์กันคนละ",round(money/person),"บาท") #ใช้ ,
    print("จำนวนเงิน"+" "+ str(format(float(money),".2f"))+" "+"บาท"+" "+"คน"+" "+str(person)+" "+"คน"+" "+"แชร์กันคนละ"+" "+str(round(money/person))+" "+"บาท") #ใช้ +
    print("จำนวนเงิน {} บาท คน {} คน แชร์กันคนละ {} บาท".format((format(float(money),'.2f')),person,round(money/person))) #ใช้ format 
    print("จำนวนเงิน %s บาท คน %d คน แชร์กันคนละ %a บาท" % ((format(float(money),'.2f')),person,round(money/person))) #ใช้ %

money, person = InputMoneyPerson()

calculate(money,person)