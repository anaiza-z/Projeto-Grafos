# 📊 Projeto de Teoria dos Grafos

Este projeto visa analisar a capacidade de backhaul da banda larga fixa nos estados brasileiros através da modelagem e visualização de grafos. Utilizando dados fornecidos pela Anatel, o projeto busca identificar padrões e insights sobre a infraestrutura de internet no país.

## 🎲 Fonte de Dados

Os dados utilizados neste projeto foram obtidos do portal [Base dos Dados](https://basedosdados.org/dataset/4ba41417-ba19-4022-bc24-6837db973009?table=f8fd49ab-cf6e-40dc-9344-d251c22ee4ab).

## 💠 Funcionalidades


1. **Análise de Grafos Bipartidos (`bipartido.py`)**:
   - **Objetivo**: Modelar a relação entre estados e tecnologias de backhaul como um grafo bipartido.
   - **Funcionalidades**:
     - Carregamento e limpeza dos dados.
     - Construção de um grafo bipartido onde os nós representam estados e tecnologias.
     - Visualização do grafo para identificar quais tecnologias são utilizadas em cada estado.

2. **Cálculo de Centralidade (`centralidade.py`)**:
   - **Objetivo**: Avaliar a importância relativa de cada estado e tecnologia na rede de backhaul.
   - **Funcionalidades**:
     - Construção de um grafo direcionado representando as conexões entre tecnologias e estados.
     - Cálculo de métricas de centralidade (peso da aresta) para identificar os nós mais influentes na rede.
     - Visualização do grafo destacando os nós com maior centralidade.

3. **Identificação de Componentes Desconexos (`desconexo.py`)**:
   - **Objetivo**: Detectar partes da rede que estão isoladas ou desconectadas do restante.
   - **Funcionalidades**:
     - Construção do grafo representando a infraestrutura de backhaul.
     - Identificação de componentes conectados e desconexos dentro do grafo.
     - Visualização dos componentes desconexos para entender possíveis lacunas na infraestrutura.
