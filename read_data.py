from stock_data import StockData

def get_stock_data(file_path):
    # Read file
    f = open(file_path, 'r')
    lines = f.readlines()
    f.close()

    # Parse file
    stock_data = []

    # Skip the first line (header)
    for line in lines[1:]:
        parts = line.split(',')

        date = parts[0]
        close_price = float(parts[1][1:])  # Remove the dollar sign and convert to float
        volume = int(parts[2])
        open_price = float(parts[3][1:])
        high = float(parts[4][1:])
        low = float(parts[5][1:])

        # Convert american date to european date (MM/DD/YYYY -> DD/MM/YYYY)
        date_parts = date.split('/')
        date = f'{date_parts[1]}/{date_parts[0]}/{date_parts[2]}'

        # Create and append to list a StockData object
        stock_data.append(StockData(date, close_price, volume, open_price, high, low))

    # Reverse list to have the oldest data first
    stock_data.reverse()

    return stock_data