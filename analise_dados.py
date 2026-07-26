import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

#nome da acao
ticker = "IBM"

#criando o objeto da acao no yfinance

acao = yf.Ticker(ticker)

dados = acao.history(period="1y")


#criando uma nova coluna em dados a partir da variacao do preco de fechamento por dia
dados["Retorno_Diario"] = dados["Close"].pct_change()

#precisamos limpar a primeira coluna ja que ela tera valor nulo (porque n temos fechamento anterior)

dados = dados.dropna()

volatilidade = dados["Retorno_Diario"].std()


#calculando o retorno acumulado
#
dados["Retorno_Acumulado"] = (1 + dados["Retorno_Diario"]).cumprod()


print(dados[["Close", "Retorno_Diario", "Retorno_Acumulado"]].tail())


print(volatilidade)