import networkx as nx 
import matplotlib.pyplot as plt
from equip_handler import Equipamento
import os

eqps = []
g = nx.Graph()
edges = []

def getEqps():
    files = []
    for root, dir, f in os.walk("equipamentos"):
        files = f

    for f in files:
        a = Equipamento()
        a.loadEqpByName("equipamentos/" + f)
        label = str(a.eqp["Id"]) + ":" + a.eqp["Nome"]
        #idt = a.eqp["Id"]
        eqps.append([label, {'equip': a}])
        #print(eqps[idt].eqp)
        
    #print(eqps)

    print("===============")

    

def createGraph():
    if(eqps == {}):
        print("HEHEEHEHEHEH")
        getEqps()
    
    #print(eqps)

    g.add_nodes_from(eqps)
    #READ EDGE FILE HERE MAYBE

    #g.add_edges_from(edges)

    print("++++++++++++")
    print(g.nodes(data=True))
    
    color = {
        1: "r",
        2: "g",
        3: "b"
    }
    nodesColor = []
    for n in g.nodes(data=True):
        nodesColor.append(color.get(n[1]["equip"].eqp["Layer"], "y"))
        print(n[1]["equip"].eqp)

    print(nodesColor)
    
    nx.draw(g, with_labels=True, node_color=nodesColor)
    plt.show()
