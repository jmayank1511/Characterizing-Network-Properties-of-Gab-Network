import json
with open('hate_annotation_2.json', 'r') as f:
    dict = json.load(f)
HatefulUsers =set()
NonHatefulUsers = set()
for i in dict:
    if(dict[i]['hate'] == 0):
        NonHatefulUsers.add(i)
    elif(dict[i]['hate'] == 1):
        HatefulUsers.add(i)
print(len(HatefulUsers))
file = open('hateful_nonHatefulUsers.txt', 'r')
line = file.readline()
count =0
cnt = 0
while line:
    count+=1
    x = line.split(':')
    line = file.readline()
    print(x[1].strip())
    if(x[1].strip()!="not-hate"):
        HatefulUsers.add(x[0])
        print(cnt)
        cnt+=1
    else:
        NonHatefulUsers.add(x[0])
print(list(HatefulUsers),"\n",len(HatefulUsers))
print((list(NonHatefulUsers)))
#exit(0)
import pickle
with open("HatefulnNonHatefulUsersTuple.pkl","wb") as o:
    pickle.dump((list(HatefulUsers),list(NonHatefulUsers)),o,pickle.HIGHEST_PROTOCOL)