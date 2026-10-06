tasks = ["เก็บที่นอน", "อาบน้ำ", "กินข้าวเช้า"]

def show_tasks(tasks):
   number = 1
   for i in tasks:
        print(str(number) + "." + i)
        number = number + 1

def add_task(tasks, new_task):
    tasks.append(new_task)

def delete_task(tasks, task_name):
    tasks.remove(task_name)        

while True:
    choice = input("เลือกเมนู โดยมี add, view, exit, remove: ")
    if choice == "add":
       new_task = input("เพิ่มรายการ: ")
       add_task(tasks, new_task)
    elif choice == "view":
       show_tasks(tasks)
    elif choice == "exit":
       print("ออกจากโปรแกรม")
       break
    elif choice == "remove":
       task_name = input("อยากลบอะไร?: ")
       delete_task(tasks, task_name)
    else:
       print("พิมพ์คำสั่งที่อยู่ในตัวเลือก")