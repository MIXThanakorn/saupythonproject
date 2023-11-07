f_dti = open("myfile02.txt","r",encoding='utf-8')# r ใช้สำหรับการอ่านข้อมูล
try:    
    
    data = f_dti.read()

    for databyline in data:
        print (databyline,end="")



except Exception:
    print("context us 02-1234567")
finally:
    f_dti.close()