import requests


def get_price(pair: str) -> str:
    try:
        pair = pair.upper()
        url = f'https://api.binance.com/api/v3/ticker/price?symbol={pair}'
        response = requests.get(url)
        data = response.json()
        return f"💰Курс {data['symbol']} = {float((data['price']))}$"
    except KeyError:
        return 'Пара не найдена!'


def get_24h_statistic(pair: str) -> str:
    try:
        pair = pair.upper()
        url = f'https://api.binance.com/api/v3/ticker/24hr?symbol={pair}'
        response = requests.get(url)
        data = response.json()
        msg = (
            f'📈Статистка за 24 часа:\n'
            f'Пара: {data["symbol"]}\n'
            f'Изменение в %: {data["priceChangePercent"]}\n'
            f'Последняя цена: {float(data["lastPrice"])}\n'
            f'Объём торгов 1: {round(float(data["volume"]), 1)}\n'
            f'Объём торгов 2: {round(float(data["quoteVolume"]), 1)}\n'
            f'Мин. за 24ч.: {float(data["lowPrice"])}\n'
            f'Макс. за 24ч.: {float(data["highPrice"])}\n'
            f'BID: {float(data["bidPrice"])}\n'
            f'ASK: {float(data["askPrice"])}\n'
        )
        return msg
    except KeyError:
        return 'Пара не найдена!' 
