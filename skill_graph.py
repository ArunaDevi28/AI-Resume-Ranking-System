import networkx as nx

def build_skill_graph(skills):

    G = nx.Graph()

    for skill in skills:

        G.add_node(skill)

    for i in range(len(skills)-1):

        G.add_edge(skills[i], skills[i+1])

    return G
