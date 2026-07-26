import pandas as pd
import yfinance as yf

#nome da acao
ticker = "IBM"

#criando o objeto da acao no yfinance

acao = yf.Ticker(ticker)

dados = acao.history(period="1y")


#criando uma nova coluna em dados a partir da variacao do preco de fechamento por dia
dados["Retorno_Diario"] = dados["Close"].pct_change()

#precisamos limpar a primeira coluna ja que ela tera valor nulo (porque n temos fechamento anterior)

dados = dados.dropna()

print(dados[["Close", "Retorno_Diario"]].head())