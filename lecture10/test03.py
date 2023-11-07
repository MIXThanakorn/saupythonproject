f_dti = open("myfile02.txt","x",encoding='utf-8') #โหมด x จะสร้างไฟล์ให้ใหม่ต่อให้ไม่มีแต่หากมีอยู่แล้วจะขึ้น Exception
f_dti.write("SAU....\n")
f_dti.write("DTI.....\n")
f_dti.write("สวัสดี.....\n")

f_dti.close()

print("บันทึกไฟล์เรียบร้อยแล้ว")