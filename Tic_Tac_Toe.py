board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
empty = [0, 1, 2, 3, 4, 5, 6, 7, 8]
p1="a"
p2="b"
#flag = True
def display():
    print('  |   |   ')
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('  |   |   ')
    print('---------')
    print('  |   |   ')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('  |   |   ')
    print('---------')
    print('  |   |   ')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('  |   |   ')

def start_game():
    global p1
    global p2
    print('Enter name of Player 1 :')
    p1 = input()
    print('Enter name of Player 2 :')
    p2 = input()
    print("Symbol of " + p1 + " is :  X")
    print("Symbol of " + p2 + " is :  O")

def input_game(player):
    if player==0:
        print("\n" + p1 + "  Turn : ")
    else:
        print("\n" + p2 + "  Turn : ")
    correct_input = True
    print("Enter the position where you want to place your symbol :")
    position = int(input())-1

    if board[position] == 'X' or board[position] == 'O':
        correct_input = False

    if not correct_input:
        print("Position already equipped")
        #print("Re-enter new position :")
        input_game(player)
    else:
        empty.remove(position)
        if player==0:
           board[position]='X'
        else:
            board[position]='O'
        #flag=False
        return 1

def check_win():
    player_symbol = ['X', 'O']
    pos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for check in pos:
        first_symbol = board[check[0]]
        if first_symbol != ' ':
            won = True
            for point in check:
                if board[point] != first_symbol:
                    won = False
                    break
            if won:
                if first_symbol == player_symbol[0]:
                    display()
                    print(p1 + " Won")
                else:
                    print(p2 + " Won")
                break
        else:
            won = False

    if won:
        return 0
    else:
        return 1

def play():
    player = 0
    start_game()
    while empty and check_win():

        display()
        input_game(player)
        player = int(not player)
    if not empty:
        print(" TIE ")


play()




