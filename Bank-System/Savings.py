from BE_account import user

class Withdraw_money(user):
    def Deduct_money(self):
     Withdraw = int(input("จำนวนเงินที่ต้องการถอน: "))
     F_money = self.money - Withdraw
     if F_money < 500:
        print("ไม่สามารถถอนเงินได้เนื่องจากยอดจะเหลือน้อยกว่า 500 บาท")
     else:
        self.money = F_money
        print(f"ยอดเงินคงเหลือ: {self.money} บาท")

    def Deposit_Money(self): #ฝากเงิน
            Withdraw = int(input("จำนวนเงินที่ต้องการฝาก: "))
            self.money = self.money + Withdraw
            print("========================================")
            print(f"ยอดเงินคงเหลือ: {self.money} บาท")
            print("========================================")
           