
import pickle
with open("UserFollower_FollowingDict.pkl", "rb") as i:
    data = pickle.load(i)

for i in data:
    print(i)

