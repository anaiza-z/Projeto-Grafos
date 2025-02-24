import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo
file_path = "br_anatel_banda_larga_fixa_backhaul.csv"

# Carregar o arquivo CSV
df = pd.read_csv(file_path, encoding="latin1")

# Obter lista de tecnologias
tecnologias = df["tecnologia"].str.lower().unique()

# Criar um dicionário para armazenar os grafos
grafos = {}

for tecnologia in tecnologias:
    # Filtrar apenas os dados da tecnologia atual
    df_tecnologia = df[df["tecnologia"].str.lower() == tecnologia]

    # Agrupar os dados por Estado e somar a capacidade_backhaul
    df_tecnologia_grouped = df_tecnologia.groupby("sigla_uf")["capacidade_backhaul"].sum().reset_index()

    # Criar um novo grafo direcionado
    G = nx.DiGraph()

    # Adicionar nós (Estados)
    estados = df["sigla_uf"].unique()
    G.add_nodes_from(estados, type="Estado")

    # Adicionar arestas para os estados atendidos pela tecnologia atual
    for _, row in df_tecnologia_grouped.iterrows():
        estado = row["sigla_uf"]
        capacidade = row["capacidade_backhaul"]

        if not pd.isna(capacidade):  # Evitar valores NaN
            G.add_edge(tecnologia.capitalize(), estado, weight=capacidade)

    # Armazenar o grafo no dicionário
    grafos[tecnologia] = G

    # Visualizar o grafo
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", edge_color="gray", font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{d['weight']:.0f} Mbps" for u, v, d in G.edges(data=True)}, font_size=8)
    plt.title(f"Grafo da Tecnologia {tecnologia.capitalize()} por Estado")
    plt.show()
