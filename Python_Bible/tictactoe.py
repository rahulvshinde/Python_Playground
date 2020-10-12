board = [" " for _ in range(9)]
# 1 2 3
# 4 5 6
# 7 8 9
solutions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
players = {"X": [], "O": []}


def display_game():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def play_game(icon):
    if icon == "X":
        move = int(input("Player 1: ").strip())
        for positions in players.values():
            print(positions)
            # for position in positions:
            #     print(position)
            if move != positions:
                print ("*********** {}".format(move))
                board[move - 1] = icon
                players[icon].append(move)
            else:
                print("Place already taken")

    elif icon == "O":
        move = int(input("Player 2: ").strip())
        for positions in players.values():
            for position in positions:
                if move != position:
                    print("$$$$$$$$$ {}".format(move))
                    board[move - 1] = icon
                    players[icon].append(move)
                else:
                    print("Place already taken")

    # player_pos = {"X": [1, 2, 3], "O": [4, 5, 6]}
    # for value in player_pos.values():
    #     for i in value:
    #         if 9 == i:
    #             print(i)

    for keys, values in players.items():
        print(keys ,":", values)


while True:
    display_game()
    play_game("X")
    display_game()
    play_game("O")
    # display_game()
