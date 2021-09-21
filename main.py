class Atm(object):
    def __init__(self, bankName, pinNumber, atmCardNumber):
        self.bankName = bankName
        self.pinNumber = pinNumber
        self.atmCardNumber = atmCardNumber

    def bank(self):
        print("bankName")

    def pin(self):
        print("pinNumber")    

    def atm(self):
        print("AtmCardNumebr")

Atm1 = Atm("HDFC", 7777, 9999)
print(Atm1.bankName)        