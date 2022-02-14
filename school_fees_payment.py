#Payment of fees
print("School fees payment")
name =input("Type your name : ")
arrears =int(input("Arrears is GHS : "))
payments = int(input("Payments of GHS : "))
def subtraction(arrears,payments):
    sub=arrears-payments
    return sub
print("Your ballance is GHS :",subtraction(arrears,payments))
