class Atm:
    def __init__(self,card_number,pin_number,cash_withdrawl,balance_statement):
        self.card_number = card_number
        self.pin_number = pin_number
        self.cash_withdrawl = cash_withdrawl
        self.balance_statement = balance_statement
        
    def print_card(self):
        print(self.card_number)
    def print_pin(self):
        print(self.pin_number)
    def print_cash(self):
        print(self.cash_withdrawl)
    def print_balance(self):
        print(self.balance_statement)
        
Values = Atm("1111 2222 3333 4444" , "1234" , "$3068" , "Money left = $1038967")
Values.print_card()
Values.print_pin()
Values.print_cash()
Values.print_balance()

        
        
    