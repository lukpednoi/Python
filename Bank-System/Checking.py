from BE_account import user

class Borrow_money(user):
    def Deduct_money(self): #ถอนเงิน
                    Withdraw = int(input("จำนวนเงินที่ต้องการถอน: "))
                    F_money = self.money - Withdraw
                    if F_money < -5000:
                        print("========================================")
                        print("⚠️ คุณไม่สามารถถอนเงินได้เนื่องจากวงเงินของคุณเต็ม")
                        print("========================================")
                    if F_money >=0:
                        self.money = F_money
                        print("========================================")
                        print(f"ยอดเงินคงเหลือ: {self.money} บาท")
                        print("========================================")   
                    if -5000 <= F_money <0:
                        self.money = F_money
                        dept = abs(self.money)
                        self.money = 0
                        print("========================================")
                        print(f"ยอดเงินคงเหลือ: {self.money} บาท")     
                        print(f"มีหนี้ทีต้องชำระ {dept} บาท")
                        print("========================================")

    def Deposit_Money(self): #ฝากเงิน
            Withdraw = int(input("จำนวนเงินที่ต้องการฝาก: "))
            self.money = self.money + Withdraw
            print("========================================")
            print(f"ยอดเงินคงเหลือ: {self.money} บาท")
            print("========================================")   
                    