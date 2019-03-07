import networkx as nx
import matplotlib.pyplot as plt
import json
import equip_handler as eqph
import graph_handler as gph

"""
metadata = {
    "Tipo de equipamento": ["sw", "rt"]
}

jsonMetadata = json.dumps(metadata, indent=2, sort_keys=True)
print(jsonMetadata)
print(type(jsonMetadata))

data = json.loads(jsonMetadata)
print(data)
print(type(data))

print(data['Tipo de equipamento'][0])
"""
i = input()
print(i)

i = input()
print(i)

eqps = []

portas = ["g1", "g2", "g3"]

eqps.append(eqph.Equipamento("teste0", 2, portas))
eqps.append(eqph.Equipamento("teste1", "a", portas))
eqps.append(eqph.Equipamento(2, 2, portas))
eqps.append(eqph.Equipamento("teste3", 1, 5))
eqps.append(eqph.Equipamento("teste4", 2, portas))
eqps.append(eqph.Equipamento("teste5", 3, portas))
eqps.append(eqph.Equipamento("teste6", 1, portas))
eqps.append(eqph.Equipamento())

for eqp in eqps:
    eqp.saveEqp()

eqps[7].loadEqp(0)

for eqp in eqps:
    eqp.saveEqp()

eqps[5].loadEqp(1)
eqps[6].loadEqp(2)


eqps[5].saveEqp

gph.getEqps()
gph.createGraph()

"""
#Create empty graph
g=nx.Graph()

#Create graph from file
g2=nx.read_edgelist('one.txt', create_using=nx.Graph(), nodetype=int)

#add nodes
g.add_node(2)
g.add_node(5)

#add edges between nodes
g.add_edge(2,5)
g.add_edge(4,1)

#add edges from list of pair of nodes
#not existing nodes will be created
g.add_edges_from([(2,5), (1,3)])
g.add_edges_from([(10,11), (11,12), (12,10)])

nx.write_edgelist(g, 'edgelist.txt', delimiter=":")

#g2.add_node(g)
#g2.add_edge(6, g.nodes[0])

#print graph info
#print(nx.info(g))
print(nx.info(g2))

#draw graph
#nx.draw(g)
nx.draw(g2, with_labels=True)

#plot graph
plt.show()
"""
