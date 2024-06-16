import pandas as pd
import yfinance as yf

from exchange_supported_coins import GMX_Exchange


def get_volatility(ticker_list, period="1mo", market="USD"):
    market = market.upper()
    ticker_data = {}
    for t in ticker_list:
        ticker = f"{t}-{market}"
        df = yf.download(ticker, period=period)
        start_price = df["Close"].iloc[0]
        end_price = df["Close"].iloc[-1]
        change = ((end_price - start_price) / start_price) * 100

        # Calculate daily returns
        daily_returns = df["Close"].pct_change().dropna()
        volatility = daily_returns.std()
        ticker_data[t] = {
            "Volatility": volatility,
            "Start": start_price,
            "End": end_price,
            "Change": change,
        }
    # Convert dict to dataframe.
    vol_df = pd.DataFrame.from_dict(
        ticker_data, orient="index", columns=["Volatility", "Start", "End", "Change"]
    )
    # Sort dataframe by most volatile.
    vol_df = vol_df.sort_values(by="Volatility", ascending=False)
    return vol_df


if __name__ == "__main__":

    ticker_list = GMX_Exchange

    df = get_volatility(ticker_list)

    print(f"{df}")
