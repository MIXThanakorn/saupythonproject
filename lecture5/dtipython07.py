import math
#คำนวนหาพทวงกลม เส้นรอบวง และปริมาตรทรงกลม
#จากรัศมีที่ผู้ใช้กรอกแล้วแสดงผล

#กรอกข้อมูล
def radians():
    return float(input('รัศมีของวงกลม: '))
    

#คำนวนพื้นที่
def circlearea(r):
    return math.pi*math.pow(r,2)

#คำนวนเส้นรอบวง
def circleround(r):
    return 2*math.pi*r

#คำนวนปริมาตร
def circlevalue(r):
    return 4/3 * math.pi * r **3

#แสดงผล
def show(r):
    print(f"วงกลมมีรัศมี {r} ซม. มีพื้นที่ {circlearea(r):.2f} ตรซม. มีเส้นรอบวง {circleround(r):.2f} ซม. มีปริมาตร {circlevalue(r):.2f} ลบซม.")



r = radians()
show(r)