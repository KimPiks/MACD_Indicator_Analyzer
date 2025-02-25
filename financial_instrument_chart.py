import matplotlib.pyplot as plt

# Y-axis of the chart
price_data = []
# X-axis of the chart
date_data = []

def set_x_y_axis_data(stock_data):
    # Extracting the data from the stock_data
    for data in stock_data:
        price_data.append(data.close_price)
        date_data.append(data.date)

def plot_full_chart(product_name):
    plt.figure(figsize=(12, 6))
    plt.plot(date_data, price_data, linewidth=1)
    plt.xlabel('Data')
    plt.ylabel('Cena (USD)')
    plt.xticks(ticks=date_data[::251], labels=date_data[::251])
    plt.title(f'Wycena ({product_name})')
    plt.grid(True, alpha=0.3)
    plt.savefig(f'{product_name}/full_chart.png')

def plot_first_half_chart(product_name):
    plt.figure(figsize=(12, 6))
    plt.plot(date_data[:len(date_data)//2], price_data[:len(price_data)//2], linewidth=1)
    plt.xlabel('Data')
    plt.ylabel('Cena (USD)')
    plt.xticks(ticks=date_data[:len(date_data)//2:200], labels=date_data[:len(date_data)//2:200])
    plt.title(f'Wycena ({product_name})')
    plt.grid(True, alpha=0.3)
    plt.savefig(f'{product_name}/first_half_chart.png')

def plot_second_half_chart(product_name):
    plt.figure(figsize=(12, 6))
    plt.plot(date_data[len(date_data)//2:], price_data[len(price_data)//2:], linewidth=1)
    plt.xlabel('Data')
    plt.ylabel('Cena (USD)')
    plt.xticks(ticks=date_data[len(date_data)//2::200], labels=date_data[len(date_data)//2::200])
    plt.title(f'Wycena ({product_name})')
    plt.grid(True, alpha=0.3)
    plt.savefig(f'{product_name}/second_half_chart.png')

def create_product_chart(stock_data, product_name):
    set_x_y_axis_data(stock_data)
    plot_full_chart(product_name)
    plot_first_half_chart(product_name)
    plot_second_half_chart(product_name)