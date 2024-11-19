import networkx as nx
import matplotlib.pyplot as plt

#Define a simple network topology
def create_network():
    G = nx.Graph()
    G.add_edges_from([(1, 2), (2, 3), (2, 4)]) #Nodes represent devices
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue")
    plt.show()
    return G, pos

network, positions = create_network()

#Simulate TCP communication
import socket
import threading

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 12345))
    s.listen(1)
    print("Server is listening . . .")
    conn, addr = s.accept()
    print(f"Connection established with {addr}")
    conn.sendall(b'Hello, Client! TCP Handshake Complete')
    conn.close()

#client node
def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 12345))
    print("Received from server:", s.recv(1024).decode())
    s.close()

#run server and client
server_thread = threading.Thread(target=server)
client_thread = threading.Thread(target=client)

server_thread.start()
client_thread.start()
server_thread.join()
client_thread.join()
#this creates a basic TCP connection and exchanges a message

def highlight_path(G, pos, path):
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue")
    edges = [(path[i], path[i+1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)
    plt.title("Packet Flow Visualization")
    plt.show()


#Example path from node 1 to node 3
#highlight_path(network, positions, [1,2, 3])



#Simulate Packet Transfer: Update the graph dynamically to show the packet's journey
import time

def dynamic_packet_flow(G, pos, path):
    for i in range(len(path) - 1):
        edges = [(path[i], path[i+1])]
        print(f"Packet moving from Node {path[i]} to Node {path[i + 1]}")  # Add this
        nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue")
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='green', width=2)
        plt.pause(1) #simulate delay for packet transmission
        plt.clf()

    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue")
    plt.title("Packet Flow Complete")
    plt.show()

dynamic_packet_flow(network, positions, [3, 2, 4])

