import json
json1_file = open('user_follower_following.json')
json1_str = json1_file.read()
json1_data = json.loads(json1_str)
import pickle
with open("UserFollower_FollowingDict.pkl","wb")as o:
    pickle.dump(json1_data,o)