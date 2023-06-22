import random
import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image
import glob
import os

def make_gif(folder):
    frames = [Image.open(image) for image in glob.glob(f"{folder}/*.JPG")]
    frame_one = frames[0]
    frame_one.save(r".\random_walk.gif", format="GIF", 
                append_images=frames, save_all=True, duration=1000, loop=0)

def random_walk(edges, t):
    graph = nx.erdos_renyi_graph(edges,0.5)
    pos = nx.circular_layout(graph)  
    position = random.randrange(1,edges)
    nx.draw_circular(graph)
    for k in range(t):
        p = graph.degree[position]
        next = random.randrange(p)
        p_path = [n for n in graph.neighbors(position)]
        position = p_path[next]
        nx.draw_networkx_nodes(graph, pos)    
        nx.draw_networkx_nodes(graph, pos, nodelist=[position], node_color="tab:red")
        plt.savefig(rf"D:\studia\semestr_2\programowanie\lista_4\graphs\graph{k}.jpg")
    make_gif(rf"D:\studia\semestr_2\programowanie\lista_4\graphs")
    for l in range(t):
        os.remove(rf"D:\studia\semestr_2\programowanie\lista_4\graphs\graph{l}.jpg")



random_walk(10,50)