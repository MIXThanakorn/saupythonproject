# โปรแกรมตรวจสอบน้ำหนักรถบรรทุก หากหนักเกิน 1000 kg  ให้แสดงข้อความ "น้ำหนักรถไม่ผ่านเกณฑ์"
# หากหนักตั้งแต่ 1000kg ลงมาให้แสดงข้อความ "น้ำหนักรถผ่านเกณฑ์"
# โดยให้กรอกทะเบียนรถและน้ำหนักของรถ

# วิเคราะห์
# มองหา feeture การทำงานว่ามีอะไรบ้าง เพื่อจะไปทำเป็น function
# 1.รับค่าทะเบียนรถและน้ำหนัก inputcardetail
# 2.ตรวจสอบน้ำหนัก processandshow

print(".........................")
print("Truck Checker")
print(".........................")

def inputcardetail():
    carregistration = input("กรอกทะเบียนรถ: ")
    weight = float(input("กรอกน้ำหนักรถ: "))
    return weight, carregistration

def processandshow(carregistration,weight):
    if weight > 1000:
        print(f"รถทะเบียน {carregistration} น้ำหนักรถไม่ผ่านเกณฑ์")
    else:
        print(f"รถทะเบียน {carregistration} น้ำหนักรถผ่านเกณฑ์")


carregistration,weight = inputcardetail()
processandshow(weight,carregistration)
print(".........................")