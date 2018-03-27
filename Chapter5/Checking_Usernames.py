current_users = ['user1', 'user2', 'user3', 'user4', 'user5']
new_users = ['user6', 'user7', 'user8', 'user2', 'user1']

for user in current_users:
    if user in new_users:
        print("The name is availble")
    else:
        print("The name is taken")