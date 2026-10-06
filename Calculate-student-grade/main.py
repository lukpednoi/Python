from backend import show_data_student
from backend import student_id
from backend import show_info_student

data_student = []
while True:    
 print("================================")
 print("1.ข้อมูลส่วนตัวของนักเรียน")
 print("2.คะแนนสอบของนักเรียน")
 print("3.ออกจากโปรแกรม")
 print("================================")
 menu = input("\nเลือกเมนูที่ต้องการ:")

 match menu: 
            case "1":
                print("===============================")
                print("1.ดูข้อมูลนักเรียน")
                print("2.เพิ่มข้อมูลนักเรียน")
                print("===============================")
                menu2 = input("\n เลือกเมนู: ")
                match menu2: 
                    case "1":
                     show_data_student(data_student)
                    case "2":
                     student_id(data_student)
            case "2":
                info = int(input("เลือกนักเรียนที่ต้องการดูคะแนน เริ่มจา่ก 0): "))
                show_info_student(info, data_student)
            case "3":
                print("ออกจากโปรแกรม")
                break
            case _:
                print("เมนูที่เลือกไม่ถูกต้อง")