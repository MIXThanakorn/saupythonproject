Product_name = input("กรอกชื่อสินค้า: ")
Product_cost = float(input("กรอกราคาต้นทุน: "))
Product_price = (Product_cost + (Product_cost)*0.1)

print(f"{Product_name}มีต้นทุน {Product_cost} บาทจะขายที่ราคา {Product_price} บาท")