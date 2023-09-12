# break/continue
# คำสั่ง break กับ คำสั่ง continue **ไม่ใช่ Control flow แต่ใช้ร่วมกับ Control flow โดยเฉพาะ loop**

for x in range(5):
    if x == 3:
        break ; # break ทำงานเมื่อไหร่จะจบ loop ทันที
    print(f"SAU...{x}")

print("................................")

for y in range(5):
    if y == 3:
        continue ; # continue ทำงานเมื่อไหร่จะจบรอบนั้น แล้วขึ้นรอบใหม่ทันที
    print(f"DTI...{y}")