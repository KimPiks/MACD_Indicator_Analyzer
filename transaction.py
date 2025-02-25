class Transaction:
    def __init__(self, transaction_type, amount, unit_price):
        self.transaction_type = transaction_type
        self.amount = amount
        self.unit_price = unit_price

    def __str__(self):
        return f'{self.transaction_type} - {self.amount} x ${self.unit_price}'