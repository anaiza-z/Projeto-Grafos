import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Dicionário para mapear estados às regiões
regioes = {
    "Norte": ["AC", "AM", "AP", "PA", "RO", "RR", "TO"],
    "Nordeste": ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"],
    "Centro-Oeste": ["DF", "GO", "MT", "MS"],
    "Sudeste": ["ES", "MG", "RJ", "SP"],
    "Sul": ["PR", "RS", "SC"]
}

# Carregar o arquivo CSV
file_path = "br_anatel_banda_larga_fixa_backhaul.csv"
df = pd.read_csv(file_path, encoding="latin1")

# Agrupar os dados por Estado e Tecnologia e somar a capacidade_backhaul
df_grouped = df.groupby(["sigla_uf", "tecnologia"])["capacidade_backhaul"].sum().reset_index()

# Criar um grafo bipartido para cada região
for regiao, estados_lista in regioes.items():
    # Filtrar apenas os estados da região atual
    df_regiao = df_grouped[df_grouped["sigla_uf"].isin(estados_lista)]

    # Criar um grafo bipartido para essa região
    B = nx.Graph()

    # Obter conjuntos de nós
    estados = df_regiao["sigla_uf"].unique()
    tecnologias = df_regiao["tecnologia"].unique()

    # Adicionar nós ao grafo com atributo bipartite
    B.add_nodes_from(estados, bipartite=0)  # Conjunto 0 (Estados)
    B.add_nodes_from(tecnologias, bipartite=1)  # Conjunto 1 (Tecnologias)

    # Adicionar arestas com pesos (capacidade do backhaul)
    for _, row in df_regiao.iterrows():
        estado = row["sigla_uf"]
        tecnologia = row["tecnologia"]
        capacidade = row["capacidade_backhaul"]

        if not pd.isna(capacidade):  # Evitar valores NaN
            B.add_edge(estado, tecnologia, weight=capacidade)

    # Gerar a posição dos nós para um grafo bipartido
    pos = nx.bipartite_layout(B, estados)

    # Criar a figura e desenhar o grafo
    plt.figure(figsize=(12, 8))
    edges = B.edges(data=True)

    # Desenhar nós e arestas
    nx.draw(B, pos, with_labels=True, node_size=3000, node_color="lightblue", edge_color="gray", font_size=10)
    nx.draw_networkx_edge_labels(B, pos, edge_labels={(u, v): f"{d['weight']:.0f} Mbps" for u, v, d in edges}, font_size=8)

    # Título com o nome da região
    plt.title(f"Grafo Bipartido - Tecnologias de Backhaul na Região {regiao}")
    plt.show()
