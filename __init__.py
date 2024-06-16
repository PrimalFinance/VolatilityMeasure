from volatility import get_volatility

from exchange_supported_coins import GMX_Exchange


if __name__ == "__main__":

    ticker_list = GMX_Exchange

    df = get_volatility(ticker_list)

    print(f"{df}")
