# โปรแกรมใช้คำนวนพื้นที่สามเหลี่ยม โดยรับค่าฐาน และสูงผ่านแป้นพิมพ์และแสดงผลผ่านทางหน้าจอ

# มองหา feeture การทำงานว่ามีอะไรบ้าง เพื่อจะไปทำเป็น function
# 1.รับค่าฐาน,สูง
# 2.คำนวนพื้นที่และแสดงผล

print(".........................")
print("calculate triangle Area")
print(".........................")


def Inputbasehigh():
    base = int(input("ป้อนฐาน: "))
    high = int(input("ป้อนสูง: "))
    return base, high

def CalAndShowTriangleArea(base, high):
    area = base * high/2
    print(f"รูปสามเหลี่ยมมีฐาน {base:.2f} ซม. สูง {high:.2f} ซม. มีพื้นที่ {area:.2f} ตรซม.")

base,high = Inputbasehigh()

CalAndShowTriangleArea(base,high)