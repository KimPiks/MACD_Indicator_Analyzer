import matplotlib.pyplot as plt
from trading_calculator import TradingCalculator

# Represents a single financial instrument
class FinancialInstrument:
    def __init__(self, stock_data, product_name):
        self.stock_data = stock_data
        self.product_name = product_name

        # Calculate MACD, signal, buy and sell signals
        tc = TradingCalculator(self.stock_data)
        self.macd = tc.macd
        self.signal = tc.signal
        self.buy_signals = tc.buy_signals
        self.sell_signals = tc.sell_signals


    # Generates a price chart and saves it to a file
    def generate_price_chart(self, output_path, x_ticks=251):
        # Y-axis data
        price_data = [data.close_price for data in self.stock_data]
        # X-axis data
        date_data = [data.date for data in self.stock_data]

        plt.figure(figsize=(15, 6))
        plt.plot(date_data, price_data, linewidth=1)
        plt.xlabel('Data')
        plt.ylabel('Cena (USD)')
        plt.xticks(ticks=date_data[::x_ticks], labels=date_data[::x_ticks])
        plt.title(f'Wycena ({self.product_name})')
        plt.grid(True, alpha=0.3)
        plt.savefig(output_path, bbox_inches='tight')

    # Generates a MACD chart and saves it to a file
    def generate_macd_chart(self, output_path, x_ticks=251):
        # X-axis data
        date_data = [data.date for data in self.stock_data]

        plt.figure(figsize=(12, 6))
        plt.plot(date_data, self.macd, label='MACD', linewidth=1)
        plt.plot(date_data, self.signal, label='SIGNAL', linewidth=1)
        plt.xlabel('Data')
        plt.xticks(ticks=date_data[::x_ticks], labels=date_data[::x_ticks])
        plt.title(f'Wskaźnik MACD ({self.product_name})')

        plt.scatter([date_data[i] for i in self.buy_signals], [self.macd[i] for i in self.buy_signals], marker='^', color='green',
                    label='Sygnał zakupu', zorder=2)
        plt.scatter([date_data[i] for i in self.sell_signals], [self.macd[i] for i in self.sell_signals], marker='v', color='red',
                    label='Sygnał sprzedaży', zorder=2)

        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(output_path, bbox_inches='tight')
