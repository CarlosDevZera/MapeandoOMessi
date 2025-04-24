import pandas as pd
import matplotlib.pyplot as plt


# Leitura do arquivo CSV
df = pd.read_csv("D:/PyProjetos/pjt001/MapeandoOMessi/data.csv", encoding='utf-8')

# Corrige caracteres corrompidos
df['Competition'] = df['Competition'].apply(lambda x: x.replace('�', 'é'))


# Padronização de nomes de competições
mapeamento_competicoes = {
    'Champions League': 'UEFA Champions League',
    'Champions Legue': 'UEFA Champions League',
    'Uefa Champions League': 'UEFA Champions League',
    'UEFA Champions Legue': 'UEFA Champions League'
    # Adicione outras variações se houver
}

df['Competition'] = df['Competition'].replace(mapeamento_competicoes)

# ===== GRÁFICO 1: Gols por Competição =====
gols_por_competicao = df.groupby('Competition')['Result'].count().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
ax1 = gols_por_competicao.plot(kind='bar', color='skyblue')

# Adiciona os valores em cima de cada barra
for i, valor in enumerate(gols_por_competicao):
    ax1.text(i, valor + 1, str(valor), ha='center', va='bottom', fontsize=9)

plt.title('Gols por Competição')
plt.xlabel('Competição')
plt.ylabel('Número de Gols')
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()


# Corrige os nomes errados das temporadas
df['Season'] = df['Season'].replace({
    '11-Dec': '11/12',
    'Dec-13': '12/13'
})

# Agora a temporada 12/13 está com nome correto, e você pode remover a errada se quiser
# (exemplo: se tiver alguma temporada com erro real)
# df = df[df['Season'] != 'algum_erro']

# Gols por temporada
gols_por_temporada = df.groupby('Season')['Result'].count().sort_index()

plt.figure(figsize=(10, 6))
ax2 = plt.gca()
ax2.plot(gols_por_temporada.index, gols_por_temporada.values, marker='o', color='orange')

# Adiciona os valores em cima dos pontos
for i, valor in enumerate(gols_por_temporada.values):
    ax2.text(i, valor + 1, str(valor), ha='center', va='bottom', fontsize=9)

plt.title('Gols por Temporada')
plt.xlabel('Temporada')
plt.ylabel('Número de Gols')
plt.xticks(ticks=range(len(gols_por_temporada.index)), labels=gols_por_temporada.index, rotation=75)
plt.grid(True)
plt.tight_layout()
plt.show()



# Contagem de assistências por jogador
assistencias_por_jogador = df['Goal_assist'].value_counts()

# Exibindo as 10 maiores assistências
top_10_assistencias = assistencias_por_jogador.head(5)

# Criando o gráfico
plt.figure(figsize=(10, 6))
ax = top_10_assistencias.plot(kind='bar', color='lightcoral')

# Adicionando os valores em cima de cada barra
for i, valor in enumerate(top_10_assistencias):
    ax.text(i, valor + 1, str(valor), ha='center', va='bottom', fontsize=9)

plt.title('Top 5 Jogadores com Mais Assistências para Messi')
plt.xlabel('Jogador')
plt.ylabel('Número de Assistências')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()



# Normaliza os tipos de finalização
df['Type'] = df['Type'].astype(str).str.strip().str.lower()

# Categorias principais (os que você quer mostrar no gráfico)
categorias_principais = {
    'left-footed shot': 'Pé Esquerdo',
    'right-footed shot': 'Pé Direito',
    'header': 'Cabeça',
    'penalty': 'Pênalti',
    'penalty rebound': 'Pênalti',
    'direct free kick': 'Falta'
}

# Filtra apenas os tipos que estão nas categorias principais
df_filtrado = df[df['Type'].isin(categorias_principais.keys())].copy()

# Aplica o mapeamento
df_filtrado['Tipo Agrupado'] = df_filtrado['Type'].map(categorias_principais)

# Contagem por tipo agrupado
contagem_agrupada = df_filtrado['Tipo Agrupado'].value_counts()

# === Gráfico ===
plt.figure(figsize=(8, 6))
ax = contagem_agrupada.plot(kind='bar', color='tomato', edgecolor='black')

# Adiciona os valores em cima das barras
for i, valor in enumerate(contagem_agrupada):
    ax.text(i, valor + 1, str(valor), ha='center', va='bottom', fontsize=10)

plt.title('Gols de Messi por Parte do Corpo / Tipo de Finalização')
plt.xlabel('Parte do Corpo / Tipo')
plt.ylabel('Quantidade de Gols')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# Filtrar apenas os gols
gols = df[df['Minute'].notna()]

# Contar os gols em casa e fora
gols_por_local = gols['Venue'].value_counts()
gols_casa = gols_por_local.get('H', 0)
gols_fora = gols_por_local.get('A', 0)


# Dados para o gráfico
labels = ['Casa', 'Fora']
valores = [gols_casa, gols_fora]

# Criando o gráfico
plt.bar(labels, valores, color=['blue', 'green'], alpha=0.7)

# Adicionando os números acima das barras
for i, valor in enumerate(valores):
    plt.text(i, valor + 5, str(valor), ha='center', va='bottom', fontweight='bold')

plt.title('Gols do Messi em Casa vs Fora')
plt.ylabel('Quantidade de Gols')
plt.xlabel('Local da Partida')
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Exibir o gráfico
plt.tight_layout()
plt.show()

