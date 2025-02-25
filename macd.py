# Calculate EMAs
alfa_12 = 2 / (12 + 1)
alfa_26 = 2 / (26 + 1)

def calculate_ema12(stock_data):
    ema_12 = []

    for i in range(len(stock_data)):
        if i == 0:
            ema_12.append(stock_data[i].close_price)
        else:
            e1 = 0
            e2 = 0
            for j in range(0, 12):
                if i-j < 0:
                    break

                alfa_param = (1-alfa_12)**j
                e1 += alfa_param * stock_data[i-j].close_price
                e2 += alfa_param

            ema_12.append(e1/e2)

    return ema_12

def calculate_ema26(stock_data):
    ema_26 = []

    for i in range(len(stock_data)):
        if i == 0:
            ema_26.append(stock_data[i].close_price)
        else:
            e1 = 0
            e2 = 0
            for j in range(0, 26):
                if i - j < 0:
                    break

                alfa_param = (1 - alfa_26) ** j
                e1 += alfa_param * stock_data[i - j].close_price
                e2 += alfa_param

            ema_26.append(e1 / e2)

    return ema_26

def calculate_macd(stock_data):
    macd = []
    ema_12 = calculate_ema12(stock_data)
    ema_26 = calculate_ema26(stock_data)

    calculate_ema12(stock_data)
    calculate_ema26(stock_data)
    for i in range(len(stock_data)):
        macd.append(ema_12[i] - ema_26[i])

    return macd

def calculate_signal(stock_data):
    signal = []
    macd = calculate_macd(stock_data)
    alfa_9 = 2 / (9 + 1)
    for i in range(len(stock_data)):
        if i == 0:
            signal.append(macd[i])
        else:
            e1 = 0
            e2 = 0
            for j in range(0, 9):
                if i - j < 0:
                    break

                alfa_param = (1 - alfa_9) ** j
                e1 += alfa_param * macd[i - j]
                e2 += alfa_param

            signal.append(e1 / e2)

    return signal