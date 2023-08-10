from pyfiglet import Figlet
def show():
    for row in game_board :
        for col in row :
            print(col,end="")
        print()
def check_game() :
    if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X" :
        print("barande shodid !!")
    elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
        print("shoma barande shodid!!!")
    elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
        print("shoma barande shodid!!!")
    elif game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O":
        print("shoma barande shodid!!!")
    elif game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O":
        print("shoma barande shodid!!!")
    elif game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O":
        print("shoma barande shodid!!!")
    
f = Figlet(font='slant')
print(f.renderText('Tic Tac Toe'))
print("Tic Tac Toe")
game_board = [["_","_","_"],
              ["_","_","_"],
              ["_","_","_"]]
show()
while True :
    # player 1 
    print("player 1")
    row = int(input("Enter row : "))
    col = int(input("Enter col : "))
    if 0 <= row <3 and 0 <= col < 3 : 
        if game_board[row][col] == "_" :
            game_board[row][col] = "X"
            show()
            check_game()
            break
        else :
            print("ye entekhab dige bokhon.")
            row = int(input("Enter row : "))
            col = int(input("Enter col : "))
            if 0 <= row <3 and 0 <= col < 3 : 
                if game_board[row][col] == "_" :
                    game_board[row][col] = "X"
                    show()
                    check_game()
                    break
                else :
                    print("dige shoma hagh entekhab nadari nobat player 2 ast.")
            else :
                print("dige shoma hagh entekhab nadari nobat player 2 ast.")              
    else :
        print("beyn 0 to 2 entekhab kon.")
        row = int(input("Enter row : "))
        col = int(input("Enter col : "))
        if 0 <= row <3 and 0 <= col < 3 : 
            if game_board[row][col] == "_" :
                game_board[row][col] = "X"
                show()
                check_game()
                break
            else :
                print("dige shoma hagh entekhab nadari nobat player 2 ast.")
        else :
            print("dige shoma hagh entekhab nadari nobat player 2 ast.")      


    # player 2
    print("player 2")
    while True :
        row = int(input("Enter row : "))
        col = int(input("Enter col : "))
        if 0 <= row <3 and 0 <= col < 3 : 
            if game_board[row][col] == "_" :
                game_board[row][col] = "X"
                show()
                check_game()
                break
            else :
                print("ye entekhab dige bokhon.")
                row = int(input("Enter row : "))
                col = int(input("Enter col : "))
                if 0 <= row <3 and 0 <= col < 3 : 
                    if game_board[row][col] == "_" :
                        game_board[row][col] = "X"
                        show()
                        check_game()
                        break
                    else :
                        print("dige shoma hagh entekhab nadari nobat player 2 ast.")
                else :
                    print("dige shoma hagh entekhab nadari nobat player 2 ast.")              
        else :
            print("beyn 0 to 2 entekhab kon.")
            row = int(input("Enter row : "))
            col = int(input("Enter col : "))
            if 0 <= row <3 and 0 <= col < 3 : 
                if game_board[row][col] == "_" :
                    game_board[row][col] = "X"
                    show()
                    check_game()
                    break
                else :
                    print("dige shoma hagh entekhab nadari nobat player 2 ast.")
            else :
                print("dige shoma hagh entekhab nadari nobat player 2 ast.") 
    