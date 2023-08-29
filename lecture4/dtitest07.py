Code = input("ป้อนรหัสพนักงาน: ")
Name = input("ป้อนชื่อพนักงาน: ")
Income = int(input("ป้อนเงินเดือนของพนักงาน: "))
Real_income = float(Income - ((Income)*0.07) - 500)

print(f"รหัสพนักงาน {Code} ชื่อ {Name} มีเงินเดือน {Income} บาท มีเงินเดือนสุทธิ {Real_income} บาท")