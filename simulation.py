from transaction import Transaction
from simulation_utils import SimulationUtils as SimUtils
import matplotlib.pyplot as plt

# Represents simulation logic for MACD and Buy and Hold strategies
class Simulation:
    CAPITAL_MULTIPLIER = 1000

    def __init__(self, product, output_dir):
        self.product = product
        self.output_dir = output_dir

    # Run simulation for MACD and Buy and Hold strategies
    def run_simulation(self):
        self.__simulation_macd()
        self.__simulation_buy_and_hold()

    # Run simulation for MACD strategy
    def __simulation_macd(self):
        cash_capital = self.CAPITAL_MULTIPLIER * self.product.stock_data[0].close_price
        capital_history = [cash_capital for _ in range(36)] # 36th day is the first valid day for MACD
        shares_count = 0
        transactions = []
        buy_transactions_indexes = []
        sell_transactions_indexes = []

        transactions_log_file_path = f'{self.output_dir}/{self.product.product_name.replace("/", "")}-simulation-macd_transaction_log.txt'
        summary_file_path = f'{self.output_dir}/{self.product.product_name.replace("/", "")}-simulation-macd_summary.txt'

        transactions_log_file = open(transactions_log_file_path, 'w')
        summary_file = open(summary_file_path, 'w')

        for i in range(36, len(self.product.stock_data)):
            if i in self.product.buy_signals:
                shares_amount_to_buy = capital_history[-1] // self.product.stock_data[i].close_price
                # We can't buy shares if we don't have enough capital
                if shares_amount_to_buy == 0:
                    capital_history.append(cash_capital + shares_count * self.product.stock_data[i].close_price)
                    continue

                # Buy as many shares as possible
                transaction = Transaction('BUY', shares_amount_to_buy, self.product.stock_data[i].close_price)
                transactions.append(transaction)
                cash_capital -= shares_amount_to_buy * self.product.stock_data[i].close_price
                shares_count += shares_amount_to_buy
                buy_transactions_indexes.append(i)

                # Log transaction to file
                SimUtils.log_transaction(transactions_log_file, 'BUY', shares_amount_to_buy, self.product.stock_data[i].close_price)
            elif i in self.product.sell_signals:
                # We can't sell shares if we don't have any
                if shares_count == 0:
                    capital_history.append(cash_capital + shares_count * self.product.stock_data[i].close_price)
                    continue

                # Sell all shares
                transaction = Transaction('SELL', shares_count, self.product.stock_data[i].close_price)
                transactions.append(transaction)
                cash_capital += shares_count * self.product.stock_data[i].close_price
                shares_count = 0
                sell_transactions_indexes.append(i)

                # Log transaction to file
                SimUtils.log_transaction(transactions_log_file, 'SELL', transaction.amount, transaction.unit_price)

            # Update capital history
            capital_history.append(cash_capital + shares_count * self.product.stock_data[i].close_price)

        # Log summary
        start_capital = capital_history[0]
        end_capital = capital_history[-1]
        SimUtils.log_capital_summary(summary_file, start_capital, end_capital)
        SimUtils.log_transactions_summary(summary_file, transactions)

        transactions_log_file.close()
        summary_file.close()

        self.__generate_macd_simulation_chart(capital_history, buy_transactions_indexes, sell_transactions_indexes)

    # Run simulation for Buy and Hold strategy
    def __simulation_buy_and_hold(self):
        cash_capital = self.CAPITAL_MULTIPLIER * self.product.stock_data[0].close_price
        capital_history = []
        shares_count = 0
        transactions = []

        summary_file_path = f'{self.output_dir}/{self.product.product_name.replace("/", "")}-simulation-buy-and-hold_summary.txt'
        summary_file = open(summary_file_path, 'w')

        # Buy transaction on the first day
        shares_amount = cash_capital // self.product.stock_data[0].close_price
        buy_transaction = Transaction('BUY', shares_amount, self.product.stock_data[0].close_price)
        transactions.append(buy_transaction)
        cash_capital -= shares_amount * self.product.stock_data[0].close_price
        shares_count += shares_amount
        capital_history.append(round(cash_capital + shares_count * self.product.stock_data[0].close_price, 2))

        for i in range(1, len(self.product.stock_data) - 1):
            capital_history.append(round(cash_capital + shares_count * self.product.stock_data[i].close_price, 2))

        # Sell transaction on the last day
        sell_transaction = Transaction('SELL', shares_count, self.product.stock_data[-1].close_price)
        transactions.append(sell_transaction)
        cash_capital += shares_count * self.product.stock_data[-1].close_price
        capital_history.append(round(cash_capital, 2))
        shares_count = 0

        # Log summary
        start_capital = round(self.CAPITAL_MULTIPLIER * self.product.stock_data[0].close_price, 2)
        end_capital = round(cash_capital, 2)
        SimUtils.log_capital_summary(summary_file, start_capital, end_capital)
        SimUtils.log_transactions_summary(summary_file, transactions)

        summary_file.close()

        self.__generate_buy_and_hold_simulation_chart(capital_history)

    # Generate chart for MACD simulation
    def __generate_macd_simulation_chart(self, capital_history, buy_transactions_indexes, sell_transactions_indexes, x_ticks = 251):
        date_data = [data.date for data in self.product.stock_data]

        plt.figure(figsize=(15, 6))
        plt.plot(date_data, [capital_history[0] for _ in range(len(date_data))], label='Kapitał początkowy',
                 linewidth=1,
                 linestyle='--')
        plt.plot(date_data, capital_history, label='Kapitał', linewidth=1, linestyle='-')
        plt.xlabel('Data')
        plt.xticks(ticks=date_data[::x_ticks], labels=date_data[::x_ticks])
        plt.title(f'Symulacja transakcji ({self.product.product_name}) - strategia MACD')
        plt.ylabel('Kapitał (USD)')

        plt.scatter([date_data[i] for i in buy_transactions_indexes],
                    [capital_history[i] for i in buy_transactions_indexes], marker='^', color='green',
                    label='Sygnał zakupu', zorder=2)
        plt.scatter([date_data[i] for i in sell_transactions_indexes],
                    [capital_history[i] for i in sell_transactions_indexes], marker='v', color='red',
                    label='Sygnał sprzedaży', zorder=2)

        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(f'{self.output_dir}/{self.product.product_name.replace("/", "")}-simulation-macd.png', bbox_inches='tight')

    # Generate chart for Buy and Hold simulation
    def __generate_buy_and_hold_simulation_chart(self, capital_history, x_ticks = 251):
        date_data = [data.date for data in self.product.stock_data]

        plt.figure(figsize=(15, 6))
        plt.plot(date_data, capital_history, label='Kapitał', linewidth=1, linestyle='-')
        plt.plot(date_data, [capital_history[0] for _ in range(len(date_data))], label='Kapitał początkowy',
                 linewidth=1,
                 linestyle='--')
        plt.xlabel('Data')
        plt.xticks(ticks=date_data[::x_ticks], labels=date_data[::x_ticks])
        plt.title(f'Symulacja transakcji ({self.product.product_name}) - strategia Buy and Hold')
        plt.ylabel('Kapitał (USD)')

        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.savefig(f'{self.output_dir}/{self.product.product_name.replace("/", "")}-simulation-buy-and-hold.png', bbox_inches='tight')