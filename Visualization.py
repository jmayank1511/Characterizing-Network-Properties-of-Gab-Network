import pickle
import matplotlib.pyplot as plt

with open("eigenVectorCentrality.pkl", "rb") as input:
    data = pickle.load(input)
with open("eigenVectorCentrality.pkl", "rb") as input:
    hateful = pickle.load(input)
x=[]
y=[]
for i in range(len(data)):
    x.append(i)
    y.append(data[i])

plt.plot(x,y)

plt.xlabel('User')
# naming the y axis
plt.ylabel('Degree')

# giving a title to my graph
plt.title('Eigen Vector Centrality Of Users')

# function to show the plot
plt.show()

plt.savefig("eigen_vector_centralities.png")
"""
with open("HatefulnNonHatefulUsersTuple.pkl","rb") as i:
    data = pickle.load(i)
print(len(data[0]))
with open("graph.pkl", "rb") as input:
    graph  = pickle.load(input)




v = graph.Full(3)
v_list = []
for vertex in data[0]:
    if v[vertex]!= None:
        v_list.append(vertex)

print("Data0 : ",len(data[0]))
print("v_list : ",len(v_list))
exit(0)
outdegree = graph.degree(data[0],mode =1)
print(outdegree)
"""