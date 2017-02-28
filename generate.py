import networkx as nx
el=open("higgs-retweet_network.edgelist", 'r')
G=nx.read_weighted_edgelist(el)
el.close()
nx.write_gexf(G, "test.gexf")