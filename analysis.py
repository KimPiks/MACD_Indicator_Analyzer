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
print("Stock data loaded successfully")
print("1/4 | Generating price chart...")
stock.generate_price_chart()
print("2/4 | Generating MACD chart...")
stock.generate_macd_chart()
print("3/4 | Simulating strategies...")
stock.simulate_strategies()
print("4/4 | Generating transaction charts...")
stock.generate_transaction_charts()
print("Analysis completed successfully")