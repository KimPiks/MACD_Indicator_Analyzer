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
    def generate_price_chart(self, output_dir, x_ticks=251):
        output_path = f'{output_dir}/{self.product_name.replace("/", "")}/{self.product_name.replace("/", "")}-price-chart.png'

        # Y-axis data
        price_data = [data.close_price for data in self.stock_data]
        # X-axis data
        date_data = [data.date for data in self.stock_data]

        plt.figure(figsize=(12, 6))
        plt.plot(date_data, price_data, linewidth=1)
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.xticks(ticks=date_data[::x_ticks], labels=date_data[::x_ticks])
        plt.title(f'Price Chart ({self.product_name})')
        plt.grid(True, alpha=0.3)
        plt.savefig(output_path, bbox_inches='tight')
        plt.close()

    # Generates a MACD chart and saves it to a file
    def generate_macd_chart(self, output_dir, x_ticks=251):
        output_path = f'{output_dir}/{self.product_name.replace("/", "")}/{self.product_name.replace("/", "")}-macd-chart.png'

        # X-axis data
        date_data = [data.date for data in self.stock_data]

        plt.figure(figsize=(12, 6))
        plt.plot(date_data, self.macd, label='MACD', linewidth=1)
        plt.plot(date_data, self.signal, label='SIGNAL', linewidth=1)
        plt.xlabel('Date')
        plt.xticks(ticks=date_data[::x_ticks], labels=date_data[::x_ticks])
        plt.title(f'MACD Indicator ({self.product_name})')

        plt.scatter([date_data[i] for i in self.buy_signals], [self.macd[i] for i in self.buy_signals], marker='^', color='green',
                    label='Buy signal', zorder=2)
        plt.scatter([date_data[i] for i in self.sell_signals], [self.macd[i] for i in self.sell_signals], marker='v', color='red',
                    label='Sell signal', zorder=2)

        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(output_path, bbox_inches='tight')
        plt.close()

    # Generates approximate charts for each transaction
    def generate_transaction_charts(self, output_dir):
        for i in range(len(self.buy_signals)):
            if len(self.sell_signals) == i:
                break

            # X-axis data (10 days before buy signal to 10 days after sell signal)
            date_data = [data.date for data in self.stock_data[self.buy_signals[i] - 10:self.sell_signals[i] + 11]]
            # Y-axis data
            price_data = [data.close_price for data in self.stock_data[self.buy_signals[i] - 10:self.sell_signals[i] + 11]]

            buy_date = self.stock_data[self.buy_signals[i]].date
            sell_date = self.stock_data[self.sell_signals[i]].date

            plt.figure(figsize=(12, 6))
            plt.plot(date_data, price_data, linewidth=1)

            # Buy and sell signals
            plt.scatter([date_data[10]], [price_data[10]], marker='^', color='green', label='Buy signal', zorder=2)
            plt.scatter([date_data[-11]], [price_data[-11]], marker='v', color='red', label='Sell signal', zorder=2)

            # xticks on buy and sell signals and the first and last day
            plt.xticks(ticks=[date_data[0], date_data[10], date_data[-11], date_data[-1]], labels=[date_data[0], buy_date, sell_date, date_data[-1]])

            plt.xlabel('Date')
            plt.ylabel('Price (USD)')
            plt.title(f'Transaction {i+1}. ({self.product_name}) {buy_date} - {sell_date}')
            plt.grid(True, alpha=0.3)
            plt.legend()
            plt.savefig(f'{output_dir}/{self.product_name.replace("/", "")}/transactions/{self.product_name.replace("/", "")}-transaction-{i+1}.png', bbox_inches='tight')
            plt.close()

    # Generates MACD transaction charts
    def generate_macd_transaction_charts(self, output_dir):
        for i in range(len(self.buy_signals)):
            if len(self.sell_signals) == i:
                break

            # X-axis data (10 days before buy signal to 10 days after sell signal)
            date_data = [data.date for data in self.stock_data[self.buy_signals[i] - 10:self.sell_signals[i] + 11]]
            # Y-axis data
            macd = self.macd[self.buy_signals[i] - 10:self.sell_signals[i] + 11]
            signal = self.signal[self.buy_signals[i] - 10:self.sell_signals[i] + 11]

            buy_date = self.stock_data[self.buy_signals[i]].date
            sell_date = self.stock_data[self.sell_signals[i]].date

            plt.figure(figsize=(12, 6))
            plt.plot(date_data, macd, label='MACD', linewidth=1)
            plt.plot(date_data, signal, label='SIGNAL', linewidth=1)
            plt.xlabel('Date')
            plt.xticks(ticks=[date_data[0], date_data[10], date_data[-11], date_data[-1]], labels=[date_data[0], buy_date, sell_date, date_data[-1]])
            plt.title(f'Transaction {i+1}. ({self.product_name}) {buy_date} - {sell_date} (MACD)')
            plt.grid(True, alpha=0.3)
            plt.legend()
            plt.savefig(f'{output_dir}/{self.product_name.replace("/", "")}/transactions/{self.product_name.replace("/", "")}-transaction-macd-{i+1}.png', bbox_inches='tight')
            plt.close()