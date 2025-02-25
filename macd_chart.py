from macd import calculate_macd, calculate_signal
import matplotlib.pyplot as plt

# X-axis of the chart
date_data = []

# Buy and sell signals
buy_signals = []
sell_signals = []

def set_x_y_axis_data(stock_data):
    # Extracting the data from the stock_data
    for data in stock_data:
        date_data.append(data.date)

def define_buy_sell_signals(macd, signal):
    for i in range(1, len(macd)):
        if macd[i] > signal[i] and macd[i - 1] < signal[i - 1]:
            buy_signals.append(i)
        if macd[i] < signal[i] and macd[i - 1] > signal[i - 1]:
            sell_signals.append(i)

def create_full_chart(macd, signal, product_name):
    plt.figure(figsize=(12, 6))
    plt.plot(date_data, macd, label='MACD', linewidth=1)
    plt.plot(date_data, signal, label='SIGNAL', linewidth=1)
    plt.xlabel('Data')
    plt.xticks(ticks=date_data[::251], labels=date_data[::251])
    plt.title(f'Wskaźnik MACD ({product_name})')

    plt.scatter([date_data[i] for i in buy_signals], [macd[i] for i in buy_signals], marker='^', color='green',
                label='Sygnał zakupu', zorder=2)
    plt.scatter([date_data[i] for i in sell_signals], [macd[i] for i in sell_signals], marker='v', color='red',
                label='Sygnał sprzedaży', zorder=2)

    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(f'{product_name}/macd_chart.png')

def create_first_half_chart(macd, signal, product_name):
    plt.figure(figsize=(12, 6))
    plt.plot(date_data[:len(date_data)//2], macd[:len(macd)//2], label='MACD', linewidth=1)
    plt.plot(date_data[:len(date_data)//2], signal[:len(signal)//2], label='SIGNAL', linewidth=1)
    plt.xlabel('Data')
    plt.xticks(ticks=date_data[:len(date_data)//2:200], labels=date_data[:len(date_data)//2:200])
    plt.title(f'Wskaźnik MACD ({product_name})')

    plt.scatter([date_data[i] for i in buy_signals if i < len(date_data)//2], [macd[i] for i in buy_signals if i < len(date_data)//2], marker='^', color='green', label='Sygnał zakupu', zorder=2)
    plt.scatter([date_data[i] for i in sell_signals if i < len(date_data)//2], [macd[i] for i in sell_signals if i < len(date_data)//2], marker='v', color='red', label='Sygnał sprzedaży', zorder=2)

    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(f'{product_name}/macd_chart_first_half.png')

def create_second_half_chart(macd, signal, product_name):
    plt.figure(figsize=(12, 6))
    plt.plot(date_data[len(date_data)//2:], macd[len(macd)//2:], label='MACD', linewidth=1)
    plt.plot(date_data[len(date_data)//2:], signal[len(signal)//2:], label='SIGNAL', linewidth=1)
    plt.xlabel('Data')
    plt.xticks(ticks=date_data[len(date_data)//2::200], labels=date_data[len(date_data)//2::200])
    plt.title(f'Wskaźnik MACD ({product_name})')

    plt.scatter([date_data[i] for i in buy_signals if i >= len(date_data)//2], [macd[i] for i in buy_signals if i >= len(date_data)//2], marker='^', color='green', label='Sygnał zakupu', zorder=2)
    plt.scatter([date_data[i] for i in sell_signals if i >= len(date_data)//2], [macd[i] for i in sell_signals if i >= len(date_data)//2], marker='v', color='red', label='Sygnał sprzedaży', zorder=2)

    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(f'{product_name}/macd_chart_second_half.png')

def create_macd_chart(stock_data, product_name):
    set_x_y_axis_data(stock_data)

    macd = calculate_macd(stock_data)
    signal = calculate_signal(stock_data)

    define_buy_sell_signals(macd, signal)
    create_full_chart(macd, signal, product_name)
    create_first_half_chart(macd, signal, product_name)
    create_second_half_chart(macd, signal, product_name)