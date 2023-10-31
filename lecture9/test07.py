#เรียกใช้ Module 
import test06 #User-defined module
import math #Build-in module
#import test08 
from test08 import (calCircleArea , calSquareArea , calTriangleArea)

print(f"ผลรวมของ 10 + 20 = {test06.sumNUMBER(10,20)}")

test06.showhi()

print(f"ราคาสินค้า 2000 เลืยภาษี {2000 * test06.Vat}")

print(f"7 ยกกำลัง 15 มีค่า {math.pow(7,15)}")

print(f"พื้นที่วงกลม มีรัศมี 3 มีค่า {math.pi * math.pow(3 ,2)}")

print(f"หาพื้นที่วงกลมรัศมี 8 มีค่า {calCircleArea(8)}")

print(f"หาพื้นที่สี่เหลี่ยมกว้าง 5 ยาว 10 มีค่า {calSquareArea(10,5)}")

print(f"หาพื้นที่สามเหลี่ยมฐาน {calCircleArea(8)}")