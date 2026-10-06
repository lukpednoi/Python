data_student = []

def student_id(data_student):
    name = input("กรุณาเขียนชื่อ-นามสกุลของคุณ: ")
    while True:
       brith_day =  input("กรุณาใส่ปีเกิดของคุณ(เช่น 2550): ")
       try:
          age = 2569 - int(brith_day)
          break
       except ValueError:
          print("กรุณาใส่ตัวเลขเท่านั้น")
    classroom = input("กรุณาเขขียนห้องที่คุณเรียน: ")
    scoreM = check_score("กรุณาใส่คะแนนสอบคณิตศาสตร์ของนักเรียน: ")
    scoreE = check_score("กรุณาใส่คะแนนสอบภาษาอังกฤษของนักเรียน: ")
    scoreS = check_score("กรุณาใส่คะแนนสอบวิทยาศาสตร์ของนักเรียน: ")
    student = {
        "ชื่อ:": name,
        "อายุ:": age,
        "ห้องเรียน:": classroom,
        "คะแนนสอบคณิตศาสตร์:": scoreM,
        "คะแนนสอบภาษาอังกฤษ:": scoreE,
        "คะแนนสอบวิทยาศาสตร์:": scoreS
    }
    data_student.append(student)
    print("\n!ข้อมูลของนักเรียนถูกบันทึกแล้ว!")
    print("================================")

    
def show_data_student(data_student):
    number = 1
    sorted_student = sorted(
        data_student,
        key = lambda s: (int(s["คะแนนสอบคณิตศาสตร์:"]) + int(s["คะแนนสอบภาษาอังกฤษ:"]) + int(s["คะแนนสอบวิทยาศาสตร์:"])) / 3,
        reverse = True
    )
    print("============ข้อมูลนักเรียนทั้งหมด===========")
    for Item in sorted_student:
       print(f"นักเรียนคนที่ {number}.")
       print(f"ชื่อ-นามสกุล: {Item['ชื่อ:']}")
       print(f"อายุ: {Item['อายุ:']} ปี")
       print(f"ห้องเรียน: {Item['ห้องเรียน:']}")
       print(f"คะแนนสอบคณิตศาสตร์: {Item['คะแนนสอบคณิตศาสตร์:']} คะแนน")
       print(f"คะแนนสอบภาษาอังกฤษ: {Item['คะแนนสอบภาษาอังกฤษ:']} คะแนน")
       print(f"คะแนนสอบวิทยาศาสตร์: {Item['คะแนนสอบวิทยาศาสตร์:']} คะแนน")
       print("----------------------------------------------")
       number = number + 1

def show_info_student(info, data_student):
 print("--------------------------------")
 print(f"นักเรียน: {data_student[info]['ชื่อ:']}")
 print ("--------------------------------")
 print(f"คะแนนสอบคณิตศาสตร์: {data_student[info]['คะแนนสอบคณิตศาสตร์:']} คะแนน")
 print(f"คะแนนสอบภาษาอังกฤษ: {data_student[info]['คะแนนสอบภาษาอังกฤษ:']} คะแนน")
 print(f"คะแนนสอบวิทยาศาสตร์: {data_student[info]['คะแนนสอบวิทยาศาสตร์:']} คะแนน")
 total_score = int(data_student[info]["คะแนนสอบคณิตศาสตร์:"]) + int(data_student[info]["คะแนนสอบภาษาอังกฤษ:"]) + int(data_student[info]["คะแนนสอบวิทยาศาสตร์:"])
 average_score = total_score / 3
 print(f"คะแนนเฉลี่ย:{average_score} คะแนน")
 
def check_score(subject_name):
   while True:
      score = input(f"กรุณาใส่่คะแนน {subject_name} ของนักเรียน")
      if score == "":
         return 0
      try:
         return int(score)
      except ValueError:
         print("ใส่แค่ตัวเลขเท่านั้น")