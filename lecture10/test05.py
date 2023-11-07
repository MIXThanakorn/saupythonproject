#อ่านข้อมูลจากไฟล์

f_dti = open("myfile01.txt","r",encoding='utf-8')
try:
    
    data = f_dti.read()
    print(data)
except Exception:
    print("context us 02-1234567")
finally:
    f_dti.close()

