q1 = {"Question": "สัตว์อะไรเอ่ย ร้องเหมียวๆและชอบกินปลา: ", "answer": "แมว"}
q2 = {"Question": "สัตว์อะไรเอ่ยร้องโฮ่งๆและชอบกินกระดูก: ", "answer": "หมา"}
q3 = {"Question": "สัตว์อะไรเอ่ยไม่มีแขนแต่มีปีก: ", "answer": 'นก'}
question = [q1, q2, q3]
score = 0

def ask_Question(q):
    ask = input(q["Question"])
    if ask == q["answer"]:
      print("คำตอบถูกต้อง")
      return 1
    else:
      print("คำตอบไม่ถูกต้อง")
      return 0

for q in question:
       score = score + ask_Question(q)
       print("Score:" + str(score))
print(("your score🎉:") + str(score) + str("/") + str(len(question))) 