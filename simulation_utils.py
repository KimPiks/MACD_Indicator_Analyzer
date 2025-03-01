# Represents utility functions for simulation logic
class SimulationUtils:
    @staticmethod
    def log_transaction(file, transaction_type, shares_amount, share_price):
        file.write(f"{transaction_type} - {shares_amount} akcji po cenie ${round(share_price, 2)}\n")

    @staticmethod
    def log_capital_summary(file, start_capital, end_capital):
        file.write("===========================\n")
        file.write(f"Kapitał początkowy: ${start_capital}\n")
        file.write(f"Kapitał końcowy: ${end_capital}\n")
        file.write(f"Zysk: ${end_capital - start_capital}\n")
        file.write(f"Zysk procentowy: {round(((end_capital - start_capital) / start_capital) * 100, 2)}%\n")
        file.write("===========================\n")

    @staticmethod
    def log_transactions_summary(file, transactions):
        transactions_count = len(transactions)
        last_buy_price = None
        profit_transactions = 0

        for i in range(transactions_count):
            if transactions[i].transaction_type == "BUY":
                last_buy_price = transactions[i].unit_price
            elif transactions[i].unit_price > last_buy_price:
                profit_transactions += 1

        file.write("===========================\n")
        file.write(f"Liczba transakcji: {transactions_count}\n")
        file.write(f"Liczba zyskownych transakcji: {profit_transactions}\n")
        file.write(f"Liczba niezyskowych transakcji: {transactions_count - profit_transactions}\n")
        file.write("===========================\n")