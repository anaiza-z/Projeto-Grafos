import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo
file_path = "br_anatel_banda_larga_fixa_backhaul.csv"

# Carregar o arquivo CSV
df = pd.read_csv(file_path, encoding="latin1")

# Agrupar os dados por Estado e Tecnologia e somar a capacidade_backhaul
df_grouped = df.groupby(["sigla_uf", "tecnologia"])["capacidade_backhaul"].sum().reset_index()

# Selecionar apenas a tecnologia mais eficiente para cada estado (com maior capacidade)
df_max_tech = df_grouped.loc[df_grouped.groupby("sigla_uf")["capacidade_backhaul"].idxmax()]

# Criar um novo grafo direcionado
G = nx.DiGraph()

# Adicionar nós (Estados e Tecnologias)
estados = df_max_tech["sigla_uf"].unique()
tecnologias = df_max_tech["tecnologia"].unique()

G.add_nodes_from(estados, type="Estado")
G.add_nodes_from(tecnologias, type="Tecnologia")

# Adicionar arestas apenas para a tecnologia mais eficiente por estado
for _, row in df_max_tech.iterrows():
    estado = row["sigla_uf"]
    tecnologia = row["tecnologia"]
    capacidade = row["capacidade_backhaul"]

    if not pd.isna(capacidade):  # Evitar valores NaN
        G.add_edge(tecnologia, estado, weight=capacidade)

# Visualizar o grafo filtrado
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", edge_color="gray", font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d['weight']:.0f} Mbps" for u, v, d in G.edges(data=True)}, font_size=8)
plt.title("Grafo da Tecnologia Mais Eficiente por Estado")
plt.show()
