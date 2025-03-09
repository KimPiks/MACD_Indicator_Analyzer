# TradingCalculator class if a class that performs calculations to determine the MACD and signal values for a given stock data.
class TradingCalculator:
    def __init__(self, stock_data):
        self.data = stock_data

        # Dictionary to store EMA values for each day
        self.ema = {
            12: self.__calculate_ema(12, [data.close_price for data in self.data]),
            26: self.__calculate_ema(26, [data.close_price for data in self.data])
        }

        # List of MACD values for each day
        self.macd = self.__calculate_macd(self.ema[12], self.ema[26])

        # List of signal values for each day
        self.signal = self.__calculate_ema(9, self.macd)

        # Lists of buy and sell signals
        self.buy_signals = self.__calculate_buy_signals(self.macd, self.signal)
        self.sell_signals = self.__calculate_sell_signals(self.macd, self.signal)

        # Validate signals
        self.sell_signals, self.buy_signals = self.__validate_signals(self.sell_signals, self.buy_signals)

    # Calculate EMA for a given period and data
    @staticmethod
    def __calculate_ema(period, data):
        alfa = 2 / (period + 1)
        ema = len(data) * [None]

        # Calculate EMA for all valid data points
        for i in range(len(data)):
            if i < period:
                continue
            if data[i - period] is None:
                continue

            ema_val = 0
            div = 0

            for j in range (0, period+1):
                ema_val += (1 - alfa) ** j * data[i - j]
                div += (1 - alfa) ** j

            ema_val /= div
            ema[i] = ema_val

        return ema

    # Calculate MACD for a given EMA12 and EMA26
    @staticmethod
    def __calculate_macd(ema12, ema26):
        macd = len(ema12) * [None]

        # Calculate MACD for all valid data points
        for i in range(len(ema12)):
            if i < 26: # 26 intervals for EMA26
                continue

            macd[i] = ema12[i] - ema26[i]

        return macd

    # Calculate buy signals for a given MACD and signal
    @staticmethod
    def __calculate_buy_signals(macd, signal):
        buy_signals = []
        for i in range(36, len(macd)): # 26 intervals for EMA26 + 9 intervals for signal + 1 to compare with previous value
            if macd[i] > signal[i] and macd[i - 1] < signal[i - 1]:
                buy_signals.append(i)
        return buy_signals

    # Calculate sell signals for a given MACD and signal
    @staticmethod
    def __calculate_sell_signals(macd, signal):
        sell_signals = []
        for i in range(36, len(macd)): # 26 intervals for EMA26 + 9 intervals for signal + 1 to compare with previous value
            if macd[i] < signal[i] and macd[i - 1] > signal[i - 1]:
                sell_signals.append(i)
        return sell_signals

    # Ensure that the sell signal is not generated before the buy signal
    @staticmethod
    def __validate_signals(sell_signals, buy_signals):
        if sell_signals[0] < buy_signals[0]:
            sell_signals.pop(0)
        return sell_signals, buy_signals