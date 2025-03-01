# Represents a single record of stock data
class StockData:
    def __init__(self, date, close_price, volume, open_price, high, low):
        self.date = date
        self.close_price = close_price
        self.volume = volume
        self.open_price = open_price
        self.high = high
        self.low = low

    def __str__(self):
        return f'Date: {self.date}, Close price: ${self.close_price}, Volume: {self.volume}, Open price: ${self.open_price}, High: ${self.high}, Low: ${self.low}'