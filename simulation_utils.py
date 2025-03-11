# Represents utility functions for simulation logic
class SimulationUtils:
    @staticmethod
    def log_transaction(file, date, transaction_type, shares_amount, share_price):
        file.write(f"[{date}] {transaction_type} - {shares_amount} shares at price ${round(share_price, 2)}\n")

    @staticmethod
    def log_capital_summary(file, start_capital, end_capital):
        file.write("===========================\n")
        file.write(f"Initial capital: ${start_capital}\n")
        file.write(f"Final capital: ${end_capital}\n")
        file.write(f"Profit: ${end_capital - start_capital}\n")
        file.write(f"Percentage profit: {round(((end_capital - start_capital) / start_capital) * 100, 2)}%\n")
        file.write("===========================\n")

    @staticmethod
    def log_transactions_summary(file, transactions):
        transactions_count = len(transactions)
        last_buy_price = None
        profit_transactions = 0
        loss_transactions = 0

        for i in range(transactions_count):
            if transactions[i].transaction_type == "BUY":
                last_buy_price = transactions[i].unit_price
            elif transactions[i].unit_price > last_buy_price:
                profit_transactions += 1
            else:
                loss_transactions += 1


        file.write("===========================\n")
        file.write(f"Number of transactions: {transactions_count}\n")
        file.write(f"Number of profitable transactions: {profit_transactions}\n")
        file.write(f"Number of losing transactions: {loss_transactions}\n")
        file.write("===========================\n")