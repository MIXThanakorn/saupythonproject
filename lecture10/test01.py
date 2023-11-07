# Exception handling
try :
    num1 = int(input("input number 1: "))
    num2 = int(input("input number 2: "))

    result1 = num1 * num2
    result2 = num1/num2

    print(f"{num1} x {num2} = {result1}")
    print(f"{num1} / {num2} = {result2}")
except ValueError :
    print("worng data type please try again")
except ZeroDivisionError:
    print("0 can't be used with Division") 
except Exception:
    print("please context us tel. 024261002 Thankyou")
finally:
    print("wow wow wow")