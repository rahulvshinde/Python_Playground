#
# board = [" " for _ in range(9)]
# soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
# player_pos = {"X": [], "O": []}
# def print_board():
#     row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
#     row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
#     row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])
#     print()
#     print(row1)
#     print(row2)
#     print(row3)
#     print()
#
# def player_move(icon):
#     if icon == "X":
#         player_pos["X"] = int(input("Player 1 [1-9]: ").strip())
#     elif icon == "O":
#         player_pos["O"] = int(input("Player 2 [1-9]: ").strip())
#     if board[choice - 1] == " ":
#         board[choice - 1] = icon
#     else:
#         print()
#         print("That space is taken")
#
# def is_victory(icon):
#     if (board[0:9])
#
#
# def play_game():
#     while True:
#         print_board()
#         player_move("X")
#         print_board()
#         player_move("O")
#
# play_game()
#
# 0 1 2
# 3 4 5
# 6 7 8



player_pos = {"X": [1,2,3], "O": [4,5,6]}
for value in player_pos.values():
    for i in value:
        if 9 == i:
            print(i)