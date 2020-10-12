films = {
    "finding Dory": [3, 5],
    "Bourne": [18, 5],
    "Tarzan": [15, 1],
    "Ghost Busters": [12, 2]
}

while True:
    choice = input("What film would you like to watch? ").strip().title()
    if choice in films:
        age = int(input("How old are you? ").strip())
        #check user age
        if age >= films[choice][0]:
            #check enough seats
            if films[choice][1] > 0:
                print("Enjoy the film.")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Seats not available")
        else:
            print("You're not old enough.")

    else:
        print("Film not available")
