f_dti = open("myfile03.txt","a",encoding='utf-8') #โหมด a จะสร้างไฟล์ให้ใหม่ต่อให้ไม่มีแต่หากมีอยู่แล้วจะเพิ่มข้อมูลเข้าไป
f_dti.write("ccc\n")
f_dti.write("ddd\n")

f_dti.close()

print("บันทึกไฟล์เรียบร้อยแล้ว")