import igraph
import pickle

with open("Data/graph.pkl", "rb") as input:
    graph  = pickle.load(input)

"""
data2 = graph.eigenvector_centrality(directed=True, scale=True,weights=None,return_eigenvalue =False)

with open("eigenVectorCentrality.pkl", "rb") as input:
    data2 = pickle.load(input)

with open("Data/hateful_user_list.pkl", "rb") as input:
    hateful_user = pickle.load(input)

eigen_vector_centralities_hateful_user = []

list1 = []
for user in hateful_user:
    list1.append(graph.eigenvector_centrality(user))

print(len(list1))

with open("Data/eigenvector_centrality_hateful_user.pkl", "wb") as o:
    pickle.dump(hateful_user, o)

"""
with open("Data/hateful_user_list.pkl", "rb") as input:
    hateful_user = pickle.load(input)

hub = graph.eccentricity(vertices = hateful_user)



with open("Data/LocalEccentricity.pkl", "wb") as o:
    pickle.dump(hub, o)