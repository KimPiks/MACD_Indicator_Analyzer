import sys
import os
from read_data import get_stock_data
from financial_instrument_chart import create_product_chart
from macd_chart import create_macd_chart
from simulation import simulation

# USAGE: py analysis.py <input_file_path> <product_name>

input_file_path = sys.argv[1]
product_name = sys.argv[2]

# Create directory for the output files with the product name
os.makedirs(product_name, exist_ok=True)

# Get stock data from the input file
data = get_stock_data(input_file_path)

# Create product chart and MACD chart
create_product_chart(data, product_name)
create_macd_chart(data, product_name)
simulation(data, product_name)