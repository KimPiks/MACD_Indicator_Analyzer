# MACD Indicator Analyzer

<div align="center">
  <img src="https://raw.githubusercontent.com/KimPiks/MACD_Indicator_Analyzer/refs/heads/main/simulation-readme.png?token=GHSAT0AAAAAAC4TYR45KSK3SZW3DGEN2CLAZ6QRTNA" alt="Example simulation chart" width="75%" />
</div>


The script allows you to generate price charts of a given financial instrument, MACD chart, run simulations for MACD and Buy&Hold strategies. 
It generates a summary showing the profit and list of transactions for both strategies, and approximate charts for each individual transaction.

## Installation and Usage
1. Clone the repository
```bash
git clone https://github.com/KimPiks/MACD_Indicator_Analyzer.git
```

2. Go to the project directory.
```bash
cd MACD_Indicator_Analyzer
```

3. Install the required packages
```bash
pip install -r requirements.txt
```

4. Create `for_analysis.txt` file in the script folder and add the financial instruments you want to analyze. 
Each instrument should be in a separate line. The first column should be the path to the data file, and the second column should be the name of the instrument.

Example:
```
stock_data/gold.csv Gold
```

5. Run the script

Windows:
```bash
./run_analysis.cmd
```

Linux:
```bash
./run_analysis.sh
```

## Result of the analysis
The script generates a folder `output` in the script folder. 
Each instrument has its own folder with the following files:
- `X-price-chart.png` - price chart of the instrument
- `X-macd-chart.png` - MACD chart of the instrument
- `X-simulation-macd.png` - simulation chart for MACD strategy
- `X-simulation-buy-and-hold.png` - simulation chart for Buy&Hold strategy
- `X-simulation-macd_summmary.txt` - summary of the MACD strategy
- `X-simulation-buy-and-hold_summary.txt` - summary of the Buy&Hold strategy
- `X-simulation-macd_transaction_log.txt` - list of transactions for the MACD strategy

Also for each transaction, the script generates a folder `transactions` with the following files:
- `X-transaction-Y.png` - approximate chart of the transaction
- `X-transaction-macd-Y.txt` - summary of the transaction

## .csv file structure
```
Date,Close/Last,Volume,Open,High,Low
02/24/2025,$2952.76,0,$2934.13,$2956.18,$2921.55
02/21/2025,$2934.92,0,$2938.78,$2949.79,$2917.07
02/20/2025,$2939.675,0,$2933.46,$2954.88,$2924.63
02/19/2025,$2932.94,0,$2935.52,$2946.91,$2918.95
...
```
