import pandas as pd
import numpy as np
import yfinance as yf

# 투자할 주식 종목의 티커를 정의합니다
stock_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

# 주식 가격 데이터를 다운로드합니다
def download_stock_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

# 일일 수익률을 계산합니다
def calculate_daily_returns(data):
    return data.pct_change().dropna()

# 동일 가중 포트폴리오를 생성합니다
def create_equal_weighted_portfolio(data):
    num_assets = len(data.columns)
    weights = np.ones(num_assets) / num_assets
    portfolio_returns = data.dot(weights)
    return portfolio_returns

def main():
    start_date = '2022-01-01'
    end_date = '2022-12-31'

    # 주식 데이터 다운로드
    stock_data = download_stock_data(stock_tickers, start_date, end_date)

    # 일일 수익률 계산
    daily_returns = calculate_daily_returns(stock_data)

    # 동일 가중 포트폴리오 생성
    portfolio_returns = create_equal_weighted_portfolio(daily_returns)

    # 누적 수익률 계산
    cumulative_returns = (1 + portfolio_returns).cumprod()

    # 결과 출력
    print("포트폴리오 수익률:")
    print(portfolio_returns.tail())
    print("\n누적 수익률:")
    print(cumulative_returns.tail())

if __name__ == "__main__":
    main()