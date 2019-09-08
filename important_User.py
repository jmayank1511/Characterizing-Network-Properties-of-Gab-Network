import pickle


with open("allUsersData_degree_distribution.pkl","rb") as input_list:
    all_user_list = pickle.load(input_list)


with open("HatefulnNonHatefulUsersTuple.pkl","rb") as input_list:
    hatful_non_hateful_user = pickle.load(input_list)

hateful = hatful_non_hateful_user[0]
nonHatful = hatful_non_hateful_user[1]

imp_hatful = []

for user in hateful:
    if user in all_user_list:
        imp_hatful.append(user)

print(len(imp_hatful))
print(len(hateful))

with open("hateful_user_list.pkl", "wb") as output:
    pickle.dump(imp_hatful, output)
