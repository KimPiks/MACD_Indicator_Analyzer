from macd import calculate_macd, calculate_signal
from transaction import Transaction
import matplotlib.pyplot as plt

# X-axis of the chart
date_data = []

# Y-axis of the chart
price_data = []

# Buy and sell signals
buy_signals = []
sell_signals = []

def set_x_y_axis_data(stock_data):
    # Extracting the data from the stock_data
    for data in stock_data:
        date_data.append(data.date)
        price_data.append(data.close_price)

def define_buy_sell_signals(macd, signal):
    for i in range(1, len(macd)):
        if macd[i] > signal[i] and macd[i - 1] < signal[i - 1]:
            buy_signals.append(i)
        if macd[i] < signal[i] and macd[i - 1] > signal[i - 1]:
            sell_signals.append(i)

def log_capital(file, capital, shares, shares_value):
    file.write("-------------------------\n")
    file.write(f"Kapitał: ${round(capital, 2)}\n")
    file.write(f"Liczba akcji: {shares}\n")
    file.write(f"Wartość akcji: ${round(shares_value, 2)}\n")
    file.write("-------------------------\n")

def log_transaction(file, type, shares, price):
    file.write(f"{type} {shares} akcji po cenie {price}\n")

def create_simulation_chart(product_name, capital_history, buy_transactions_indexes, sell_transactions_indexes):
    plt.figure(figsize=(12, 6))
    plt.plot(date_data, [capital_history[0] for _ in range(len(date_data))], label='Kapitał początkowy', linewidth=1,
             linestyle='--')
    plt.plot(date_data, capital_history, label='Kapitał', linewidth=1, linestyle='-')
    plt.xlabel('Data')
    plt.xticks(ticks=date_data[::251], labels=date_data[::251])
    plt.title(f'Symulacja transakcji ({product_name})')
    plt.ylabel('Kapitał (USD)')

    plt.scatter([date_data[i] for i in buy_transactions_indexes],
                [capital_history[i] for i in buy_transactions_indexes], marker='^', color='green',
                label='Sygnał zakupu', zorder=2)
    plt.scatter([date_data[i] for i in sell_transactions_indexes],
                [capital_history[i] for i in sell_transactions_indexes], marker='v', color='red',
                label='Sygnał sprzedaży', zorder=2)

    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(f'{product_name}/simulation.png')


def simulation(stock_data, product_name):
    # Initial capital (1000 units * the price of the first stock)
    capital_multiplier = 1000
    capital = capital_multiplier * stock_data[0].close_price
    capital_history = [capital for _ in range(26)]
    shares_count = 0
    transactions = []
    buy_transactions_indexes = []
    sell_transactions_indexes = []

    set_x_y_axis_data(stock_data)

    macd = calculate_macd(stock_data)
    signal = calculate_signal(stock_data)
    define_buy_sell_signals(macd, signal)

    # Simulation log file
    f = open(f'{product_name}/simulation_log.txt', 'w')
    f.write(f"Kapitał początkowy: {round(capital, 2)}\n")

    for i in range(26, len(stock_data)):
        if i in buy_signals:
            amount = capital // stock_data[i].close_price
            if amount == 0:
                continue

            transactions.append(Transaction('BUY', amount, stock_data[i].close_price))
            shares_count += amount
            capital -= amount * stock_data[i].close_price
            capital_history.append(capital + shares_count * stock_data[i].close_price)
            buy_transactions_indexes.append(i)

            log_transaction(f, 'BUY', amount, stock_data[i].close_price)
            log_capital(f, capital, shares_count, shares_count * stock_data[i].close_price)
        elif i in sell_signals and len(transactions) > 0 and shares_count > 0:
            transactions.append(Transaction('SELL', shares_count, stock_data[i].close_price))
            capital += shares_count * stock_data[i].close_price
            shares_count = 0
            capital_history.append(capital)
            sell_transactions_indexes.append(i)

            log_transaction(f, 'SELL', transactions[-1].amount, stock_data[i].close_price)
            log_capital(f, capital, shares_count, shares_count * stock_data[i].close_price)
        else:
            capital_history.append(capital + shares_count * stock_data[i].close_price)

    f.write("===========================\n")
    f.write(f"Kapitał początkowy: ${round(capital_multiplier * stock_data[0].close_price, 2)}\n")
    f.write(f"Kapitał końcowy: ${round((capital + shares_count * stock_data[-1].close_price), 2)}\n")
    f.write(f"Zysk: ${round((capital + shares_count * stock_data[-1].close_price) - (capital_multiplier * stock_data[0].close_price), 2)}\n")
    f.write("===========================\n")
    f.close()

    create_simulation_chart(product_name, capital_history, buy_transactions_indexes, sell_transactions_indexes)