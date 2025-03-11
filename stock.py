from stock_data import StockData
from financial_instrument import FinancialInstrument
from simulation import Simulation
import os

class Stock:
    OUTPUT_DIR = 'output'

    def __init__(self, input_file_path, product_name):
        self.stock_data = self.__read_data_file(input_file_path)
        self.product_name = product_name
        self.product = FinancialInstrument(self.stock_data, self.product_name)

    # Read data from a file and store it in a list of StockData objects
    @staticmethod
    def __read_data_file(file_path):
        # Read file
        f = open(file_path, 'r')
        lines = f.readlines()
        f.close()

        data = []

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
            data.append(StockData(date, close_price, volume, open_price, high, low))

        # Reverse list to have the oldest data first
        data.reverse()
        return data

    # Ensure that the output directory exists
    def __ensure_output_dir_exists(self):
        if not os.path.exists(self.OUTPUT_DIR):
            os.makedirs(self.OUTPUT_DIR)

        if not os.path.exists(f'{self.OUTPUT_DIR}/{self.product_name.replace("/", "")}'):
            os.makedirs(f'{self.OUTPUT_DIR}/{self.product_name.replace("/", "")}')

        if not os.path.exists(f'{self.OUTPUT_DIR}/{self.product_name.replace("/", "")}/transactions'):
            os.makedirs(f'{self.OUTPUT_DIR}/{self.product_name.replace("/", "")}/transactions')

    # Generate a price chart for the stock product
    def generate_price_chart(self):
        self.__ensure_output_dir_exists()
        self.product.generate_price_chart(self.OUTPUT_DIR)

    # Generate a MACD chart for the stock product
    def generate_macd_chart(self):
        self.__ensure_output_dir_exists()
        self.product.generate_macd_chart(self.OUTPUT_DIR)

    # Generate approximate charts for each transaction
    def generate_transaction_charts(self):
        self.__ensure_output_dir_exists()
        self.product.generate_transaction_charts(self.OUTPUT_DIR)

    # Generate approximate charts for each transaction (MACD)
    def generate_macd_transaction_charts(self):
        self.__ensure_output_dir_exists()
        self.product.generate_macd_transaction_charts(self.OUTPUT_DIR)

    # Simulate a MACD and Buy & Hold strategy for the stock product
    def simulate_strategies(self):
        sim = Simulation(self.product, self.OUTPUT_DIR)
        sim.run_simulation()