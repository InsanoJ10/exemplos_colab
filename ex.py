import pandas as pd # importa as funções do pandas
import numpy as np # importa as funções do numpy


dados = pd.read_excel("dados_exemplo.xlsx") # importa a dados anexada
# display(dados) #mostra todos os dados
# dados.head() #para mostrar somente as primeiras linhas
# dados.tail() # para mostrar as últimas linhas


# analise da estrutura da dados
# print("\nQuantidade de linhas e colunas: ", dados.shape)
# print("\nNome das colunas: ", dados.columns)
# print("\nTipos de dados: ", dados.dtypes)
# print("\nInformações Gerais: ")
# dados.info()


# Esse código remove espaços e transforma os nomes em letras minusculas
# dados.columns = (
#     dados.columns
#     .str.strip()
#     .str.lower()
# )
# display(dados)


#Para limpar o nome dos alunos
#dados["aluno"] = (
#    dados["aluno"]
#    .astype("string")
#    .str.strip()
#    .str.title()
#)


# localizar dados ausentes
# print("Valores ausentes por coluna:")
# print(dados.isna().sum())


# Para visualizar as linhas com notas ausentes:
# linhas_incompletas = dados[
#     dados[["nota1", "nota2"]].isna().any(axis=1)
# ]
# display(linhas_incompletas)


# As notas ausentes serão substituídas pela média da respectiva coluna.
# media_nota1 = dados["nota1"].mean()
# media_nota2 = dados["nota2"].mean()


# dados["nota1"] = dados["nota1"].fillna(media_nota1)
# dados["nota2"] = dados["nota2"].fillna(media_nota2)
# Verificação:
# print(dados.isna().sum())


# As notas devem estar entre 0 e 10.
# notas_invalidas = dados[
#     ~dados["nota1"].between(0, 10) |
#     ~dados["nota2"].between(0, 10)
# ]


# display(notas_invalidas)
# Para limitar valores ao intervalo entre 0 e 10:
# dados["nota1"] = dados["nota1"].clip(0, 10)
# dados["nota2"] = dados["nota2"].clip(0, 10)


# calcular a média dos alunos
# dados["media"] = np.mean(
#     dados[["nota1", "nota2"]],
#     axis=1
# )


# dados["media"] = dados["media"].round(2)


# definir a situação
# dados["situacao"] = np.where(
#     dados["media"] >= 6,
#     "Aprovado",
#     "Reprovado"
# )
# Com três situações:
# condicoes = [
#     dados["media"] >= 6,
#     dados["media"] >= 4
# ]


# resultados = [
#     "Aprovado",
#     "Recuperação"
# ]


# dados["situacao"] = np.select(
#     condicoes,
#     resultados,
#     default="Reprovado"
# )
# Regras utilizadas:
# Média maior ou igual a 6: aprovado.
# Média entre 4 e 5,99: recuperação.
# Média menor que 4: reprovado.


# ordenar os alunos pela média
# dados = dados.sort_values(
#     by="media",
#     ascending=False
# )


# mostrar alunos aprovados
# aprovados = dados[
#     dados["situacao"] == "Aprovado"
# ]


# display(aprovados)


# mostrar alunos abaixo da média da turma
# media_turma = dados["media"].mean()
# abaixo_da_media = dados[
#     dados["media"] < media_turma
# ]
# print(f"Média da turma: {media_turma:.2f}")
# display(abaixo_da_media)


# calcular estatísticas
# print(f"Média geral: {dados['media'].mean():.2f}")
# print(f"Maior média: {dados['media'].max():.2f}")
# print(f"Menor média: {dados['media'].min():.2f}")
# print(f"Mediana: {dados['media'].median():.2f}")
# print(f"Desvio padrão: {dados['media'].std():.2f}")


# Para mostrar um resumo estatístico:
# dados[["nota1", "nota2", "media"]].describe()
# localizar o aluno com maior média
# indice_maior_media = dados["media"].idxmax()
# melhor_aluno = dados.loc[indice_maior_media]
# print("Aluno com maior média:")
# print(melhor_aluno)


# contar as situações
# quantidades = dados["situacao"].value_counts()
# print(quantidades)


# Para calcular o percentual:
# percentuais = dados["situacao"].value_counts(
#     normalize=True
# ).mul(100).round(2)
# print(percentuais)


# criar um resumo
# resumo = pd.DataFrame({
#     "Indicador": [
#         "Quantidade de alunos",
#         "Média da turma",
#         "Maior média",
#         "Menor média",
#         "Quantidade de aprovados",
#         "Quantidade em recuperação",
#         "Quantidade de reprovados"
#     ],
#     "Resultado": [
#         len(dados),
#         round(dados["media"].mean(), 2),
#         round(dados["media"].max(), 2),
#         round(dados["media"].min(), 2),
#         (dados["situacao"] == "Aprovado").sum(),
#         (dados["situacao"] == "Recuperação").sum(),
#         (dados["situacao"] == "Reprovado").sum()
#     ]
# })


# display(resumo)


# criar um gráfico
# import matplotlib.pyplot as plt
# dados.plot(
#     x="aluno",
#     y="media",
#     kind="bar",
#     color="steelblue",
#     legend=False,
#     figsize=(10, 5)
# )
# plt.axhline(
#     y=6,
#     color="red",
#     linestyle="--",
#     label="Média para aprovação"
# )
# plt.title("Média dos alunos")
# plt.xlabel("Aluno")
# plt.ylabel("Média")
# plt.xticks(rotation=45)
# plt.ylim(0, 10)
# plt.legend()
# plt.tight_layout()
# plt.show()


# exportar o resultado para Excel
# nome_saida = "relatorio_notas.xlsx"
# with pd.ExcelWriter(nome_saida) as escritor:
#     dados.to_excel(
#         escritor,
#         sheet_name="Alunos",
#         index=False
#     )
#     resumo.to_excel(
#         escritor,
#         sheet_name="Resumo",
#         index=False
#     )
# baixar o relatório
# from google.colab import files
# files.download("relatorio_notas.xlsx")




