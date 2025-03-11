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
print("1/5 | Generating price chart...")
stock.generate_price_chart()
print("2/5 | Generating MACD chart...")
stock.generate_macd_chart()
print("3/5 | Simulating strategies...")
stock.simulate_strategies()
print("4/5 | Generating transaction charts...")
stock.generate_transaction_charts()
print("5/5 | Generating MACD transaction charts...")
stock.generate_macd_transaction_charts()
print("Analysis completed successfully")