import networkx as nx
import numpy as np
import matplotlib.pyplot as plt




G1=nx.DiGraph() # graf objemizi ouşturduk
#Düğümleri ve 5gen şeklinde görünmesi için pos değerleri atıyoruz
G1.add_node(0, pos=(2,6))
G1.add_node(1, pos=(4,3))
G1.add_node(2, pos=(3,0))
G1.add_node(3, pos=(1,0))
G1.add_node(4, pos=(0,3))

# manuel olarak varsa node'lar arası  ağırlıkları atıyorum
G1.add_edge(0,1,weight=5)
G1.add_edge(0,2,weight=3)
G1.add_edge(0,4,weight=2)
G1.add_edge(1,2,weight=2)
G1.add_edge(1,3,weight=6)
G1.add_edge(2,1,weight=1)
G1.add_edge(2,3,weight=2)
G1.add_edge(4,1,weight=6)
G1.add_edge(4,2,weight=10)
G1.add_edge(4,3,weight=4)

pos=nx.get_node_attributes(G1,'pos')



nx.draw_networkx(G1, pos,node_color="red",node_size=600)
edge_labels=dict([((u,v,),d['weight'])for u,v,d in G1.edges(data=True)])
nx.draw_networkx_edge_labels(G1, pos, edge_labels=edge_labels, label_pos=0.3)


plt.axis("off")
plt.title("Graf:")
# Çizge:
plt.show()


# Bu fonksiyon istenen düğümden kendisine bir path mümkün olan diğer tüm düğümlere en kısa yolu ve bu yolun uzunluğunu yazdırıyor
def dijkstra(startNode):
    for var in range(len(G1.nodes())):
        if var!=startNode :
            try:
                print(str(startNode)+". Düğümden "+str(var)+". düğüme  en kısa yol: ")
                print(nx.dijkstra_path(G1,source=startNode,target=var))
                print("Uzaklık: "+str(nx.dijkstra_path_length(G1,source=startNode,target=var)))
                print()
            except Exception as ex:
                print(str(startNode)+". düğümden "+str(var)+". düğüme bir yok mevcut değil..")
                print()

dijkstra(4) #4 numaralı node için çalıştırıyoruz

G1.remove_node(1)#1 numaralı node silinip tekrar çizgeyi yazdırıyoruz



nx.draw_networkx(G1, pos,node_color="red",node_size=600)
edge_labels=dict([((u,v,),d['weight'])for u,v,d in G1.edges(data=True)])
nx.draw_networkx_edge_labels(G1, pos, edge_labels=edge_labels, label_pos=0.3, font_size=7)




plt.title("1 numaralı node silindi")
plt.show()

