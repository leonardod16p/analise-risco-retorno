import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np


#nome da acao
ticker = "IBM"

empresas = ["IBM", "MSFT"]
dados_fechamento = yf.download(empresas, period="1y")["Close"]
dados_fechamento = dados_fechamento.dropna()

dados_fechamento["IBM_MM50"] = dados_fechamento["IBM"].rolling(window=50).mean()
print(dados_fechamento[["IBM", "IBM_MM50"]].head(55))

# #criando o objeto da acao no yfinance

# acao = yf.Ticker(ticker)

# dados = acao.history(period="1y")


# #criando uma nova coluna em dados a partir da variacao do preco de fechamento por dia
#dados["Retorno_Diario"] = dados["Close"].pct_change()
retornos_diarios = dados_fechamento[["IBM", "MSFT"]].pct_change()
#precisamos limpar a primeira coluna ja que ela tera valor nulo (porque n temos fechamento anterior)

# dados = dados.dropna()

#volatilidade = dados["Retorno_Diario"].std()
volatilidade_diaria = retornos_diarios.std()

# #calculando o retorno acumulado
# #
#dados["Retorno_Acumulado"] = (1 + dados["Retorno_Diario"]).cumprod()
volatilidade_anual = volatilidade_diaria * np.sqrt(252)

# print(dados[["Close", "Retorno_Diario", "Retorno_Acumulado"]].tail())
volatilidade_anual_pct = volatilidade_anual * 100

print("volatilidade anualizada")
print(volatilidade_anual_pct.round(3)) 


#taxa livre de risco
#quanto de retorno teriamos na aplicacao mais segura do mundo?
#(o interessante aqui seria usar a taxa de juros do tesouro direto dos EUA)
#vamos de valor hipotetico
taxa_livre_risco = 0.04

retorno_anualizado = retornos_diarios.mean() * 252

#nossa indice sharpe
#retorno acao - taxa livre / risco
indice_sharpe = (retorno_anualizado - taxa_livre_risco ) / volatilidade_anual

print("Indice Sharpe: ")
print(indice_sharpe.round(3))

precos = dados_fechamento[["IBM", "MSFT"]]

#retorna o maior preco ate cada dia
picos = precos.cummax()


#porcentagem de queda em relacao ao pico anterior
drawdowns = (precos - picos) / picos

max_drawdown = drawdowns.min() * 100

print("Maior drawdown: ")
print(max_drawdown.round(3))



plt.figure(figsize=(10,6))

# plt.plot(dados.index, dados["Retorno_Acumulado"], label="IBM",color="blue", linewidth=2)
plt.plot(dados_fechamento.index, dados_fechamento["IBM"], label="Preço IBM",color="blue", alpha=0.5)
plt.plot(dados_fechamento.index, dados_fechamento["IBM_MM50"], label="Média Móvel 50 Dias",color="red", linewidth=2)

plt.title("IBM: Preço Vs Média Móvel", fontsize=12)
plt.xlabel("Data", fontsize=10)
plt.ylabel("Preço (USD)", fontsize=10)

plt.grid(True, linestyle="--", alpha=0.5)

plt.legend()

plt.show()
