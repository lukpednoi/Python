from Checking import Borrow_money
from Savings import Withdraw_money

withdraw_money = Withdraw_money()
withdraw_money.Account_money()
borrow_money = Borrow_money()
borrow_money.Account_money()

while True:
    print("==========================================")
    print("")
    print("    --------------------------")
    print("    🏦 Welcome to the K-bank🏦")
    print("    --------------------------")
    print("")
    print("      User: Mr.Rick Sanchez")
    print("")
    print("==========================================")
    print("\n หากท่านต้องการเข้าใช้งานบัญชีประเภทออมทรัพย์ให้กดหมายเลข 1")
    print("\nหากท่านต้องการเข้าใช้งานบัญชีประเภทกระแสรายวันให้กดหมายเลข 2")

    menu = input("\n เลือกประเภทบัญชีที่ต้องการใช้งานของท่าน:")


    match menu:
        case "1":
            print("==========================================")
            print("")
            print("    --------------------------")
            print("    💸 บัญชีประเภทออมทรัพย์ 💸")
            print("    --------------------------")
            print("")
            print("==========================================")
            print("")
            print("        เลือกเมนูที่ต้องการทำรายการ")
            print("        1.ฝากเงิน 2. ถอนเงิน")
            Savings_menu = input("กรุณาเลือกหมายเลข: ")
            match Savings_menu:
                case "1":
                    withdraw_money.Deposit_Money()
                case "2":
                    withdraw_money.Deduct_money()       
        case "2":
            print("==========================================")
            print("")
            print("    --------------------------")
            print("    💳 บัญชีประเภทกระแสรายวัน 💳")
            print("    --------------------------")
            print("")
            print("==========================================")
            print("")
            print("        เลือกเมนูที่ต้องการทำรายการ")
            print("        1.ฝากเงิน 2. ถอนเงิน")
            Checking_menu = input("กรุณาเลือกหมายเลขเลข: ")
            match Checking_menu:
                case "1":
                    borrow_money.Deposit_Money()
                case "2":
                    borrow_money.Deduct_money()