import yfinance as yf
import numpy as np

def get_stock_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

def calculate_returns(data):
    returns = data.pct_change()
    return returns

def build_portfolio(data, num_stocks):
    tickers = data.columns
    selected_tickers = np.random.choice(tickers, size=num_stocks, replace=False)
    portfolio = data[selected_tickers]
    return portfolio

def main():
    # Parameters
    tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'FB']  # Example list of stock tickers
    start_date = '2023-01-01'
    end_date = '2024-01-01'
    num_stocks = 3  # Number of stocks in the portfolio

    # Get stock data
    data = get_stock_data(tickers, start_date, end_date)

    # Calculate returns
    returns = calculate_returns(data)

    # Build portfolio
    portfolio = build_portfolio(data, num_stocks)

    print("Selected Stocks for Portfolio:")
    print(portfolio.head())

if __name__ == "__main__":
    main()