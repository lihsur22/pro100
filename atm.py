class Atm:
    def __init__(self,card_num,pin_num):
        self.card_num = str(card_num)
        self.pin_num = str(pin_num)
        self.bal = 10000
    def cashW(self):
        cardN = str(input('ENTER CARD NUMBER : '))
        pinN = str(input('ENTER PIN NUMBER : '))
        if(cardN == self.card_num) and (pinN == self.pin_num):
            print('\nYOUR BALANCE : ' + str(self.bal))
            amnt = int(input('\n\nENTER WITHDRAWAL AMOUNT : '))
            if(amnt <= 5000) and (amnt < self.bal):
                self.bal = self.bal - amnt
                print('TRANSACTION SUCCESSFUL')
            elif(amnt > self.bal):
                print('YOU DON\'T HAVE ENOUGH BALANCE')
            else:
                print('YOU CAN ONLY MAKE A TRANSACTION OF 5000 OR LESS')
        else:
            print('WRONG PIN OR CARD NUMBER')
    def cashD(self):
        cardN = str(input('ENTER CARD NUMBER : '))
        pinN = str(input('ENTER PIN NUMBER : '))
        if(cardN == self.card_num) and (pinN == self.pin_num):
            print('\nYOUR BALANCE : ' + str(self.bal))
            amnt = int(input('\n\nENTER WITHDRAWAL AMOUNT : '))
            if(amnt <= 5000):
                self.bal = self.bal + amnt
                print('DEPOSITION SUCCESSFUL')
            else:
                print('YOU CAN ONLY MAKE A TRANSACTION OF 5000 OR LESS')
        else:
            print('WRONG PIN OR CARD NUMBER')
    def getBal(self):
        cardN = str(input('ENTER CARD NUMBER : '))
        pinN = str(input('ENTER PIN NUMBER : '))
        if(cardN == self.card_num) and (pinN == self.pin_num):
            print('\nYOUR BALANCE : ' + str(self.bal))
        else:
            print('WRONG PIN OR CARD NUMBER')
    def help(self):
        print('THIS IS YOUR ATM!\nGET YOUR BALANCE BY USING .getBal()\nWITHDRAW COINS BY USING .cashW()\nDEPOSIT COINS BY USING .cashD()')