#การลบไฟล์
import os


if os.path.exists("myfile03.txt"):
    os.remove("myfile03.txt")
    print("ลบไฟล์เรียบร้อยแล้ว")
else:
    print("No flie to delete")