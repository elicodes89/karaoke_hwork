class Guest:

    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def enough_money_to_pay_entry_fee(self, price):
        return self.wallet >= price.fee

    def not_enough_money_to_pay_entry_fee(self, price):
        return self.wallet <= price.fee


    
