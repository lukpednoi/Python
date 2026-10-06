def change():
 while True:
  menu = input("คำนวนระยะทาง หรือ ออกจากโปรแกรม: ")
  if menu == "คำนวนระยะทาง":
      ask = input("mile or kilometer: ")
      if ask == "mile":
         mile = float(input("ใส่ระยะทาง: "))
         kilometer = mile * 1.60934
         print(f"คิดเป็นระยะทางเป็น: {kilometer} กิโลเมตร")
      elif ask == "kilometer":
         kilometer = float(input("ใส่ระยะทาง: "))
         mile = kilometer * 0.621371
         print(f"คิดระยะทางเป็น: {mile} ไมล์")
  elif menu == "ออกจากโปรแกรม":
     print("ออกแล้ว")
     break
change()

