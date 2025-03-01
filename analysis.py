import sys
from stock import Stock

# USAGE: py analysis.py <input_file_path> <product_name>

# Input file path and product name from the command line arguments
input_file_path = sys.argv[1]
product_name = sys.argv[2]

# Remove all invisible and problematic characters from the product name
product_name = product_name.replace("\r", "")
product_name = product_name.replace("\n", "")
product_name = product_name.replace("\t", "")
product_name = product_name.replace(" ", "")
product_name = product_name.replace("/", "")
product_name = product_name.replace("\\", "")

print(f"> Analyzing {product_name} stock data from {input_file_path}")

stock = Stock(input_file_path, product_name)
stock.generate_price_chart()
stock.generate_macd_chart()
stock.simulate_strategies()