# file handling
# เขียนข้อมูลลงไฟล์
f_dti = open("myfile01.txt","w",encoding='utf-8')  #เปิดไฟล์เพิ่อเขียนข้อมูลลงไป #โหมด w จะสร้างไฟล์ให้ใหม่ต่อให้ไม่มีและจะสร้างทับไฟล์เดิม
f_dti.write("Hello....\n")
f_dti.write("Hi.....\n")
f_dti.write("สวัสดี.....\n")

f_dti.close()

print("บันทึกไฟล์เรียบร้อยแล้ว")