f_dti = open("myfile02.txt","r",encoding='utf-8')
try:    
    data = f_dti.readline()
    print(data, end="")
    data = f_dti.readline()
    print(data, end="")
    data = f_dti.readline()
    print(data, end="")
    
except Exception:
    print("context us 02-1234567")
finally:
    f_dti.close()