known_users = ["rahul", "rutu", "alice", "dan", "harry"]
while True:
    print("Hi, My name is Travis")
    name = input("What is your name? ").strip()
    if name.lower() in known_users:
        print("Welcome, {}".format(name))
        remove = input("Would you like to be removed? ").strip().lower()
        if remove == "yes" or remove == "y":
            known_users.remove(name)
            print("User {} has been removed from the system".format(name))
        print("Known Users {}".format(known_users))
    else:
        print("Sorry, I don't know you")
        add = input("Would you like to be added?").strip().lower()
        if add == "yes" or add == "y":
            known_users.append(name)
            print("User {} successfully added to the system.".format(name))
            print(known_users)

