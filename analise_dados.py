import pandas as pd
import yfinance as yf

#nome da acao
ticker = "IBM"

#criando o objeto da acao no yfinance

acao = yf.Ticker(ticker)


dados = acao.history(period="1y")

print(dados.head())