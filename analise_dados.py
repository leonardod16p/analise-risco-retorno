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


plt.figure(figsize=(10,6))

plt.plot(dados.index, dados["Retorno_Acumulado"], label="IBM",color="blue", linewidth=2)

plt.title("Evolucao do patrimonio - IBM (1 ano)", fontsize=12)
plt.xlabel("Data", fontsize=10)
plt.ylabel("Retorno Acumulado", fontsize=10)

plt.grid(True, linestyle="--", alpha=0.5)

plt.legend()

plt.show()
